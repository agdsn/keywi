from datetime import datetime

import pdfkit
from psycopg2._range import DateTimeTZRange
from sqlalchemy import func, not_

from lib.crud import create_object, REFERENCED_OBJ, delete_object, edit_object
from model import Rental, User, Location, Key, utcnow
from model.session import with_transaction, session
from jinja2 import Environment, FileSystemLoader, select_autoescape


class RentalRangeOverlapException(Exception):
    pass


@with_transaction
def create_rental(key: Key, user: User, issuing_user: User, processor: User, begin: datetime = None,
                  end: datetime = None, allowed_by: str = None, note: str = None):
    args = locals()

    begin = begin if begin else utcnow()
    timerange = DateTimeTZRange(begin, end, bounds='[]')

    other_rental = session.query(Rental).filter(
        Rental.key == key,
        not_(Rental.deleted),
        func.tstzrange(Rental.begin, Rental.end, '[]').op('&&')(timerange)
    ).first()

    if other_rental is not None:
        raise RentalRangeOverlapException("Key has an other rental in this timerange.")

    return create_object(Rental,
                         log_keys=['issuing_user_id', 'allowed_by', 'note', 'begin'],
                         log_params={'rental': REFERENCED_OBJ,
                                     'key': key,
                                     'user': user},
                         **args)


@with_transaction
def edit_rental(rental: Rental, processor: User, **kwargs):
    begin = kwargs.get('begin', rental.begin)
    end = kwargs.get('end', rental.end)
    key = kwargs.get('key', rental.key)

    timerange = DateTimeTZRange(begin, end, bounds='[]')

    other_rental = session.query(Rental).filter(
        Rental.key == key,
        not_(Rental.deleted),
        func.tstzrange(Rental.begin, Rental.end, '[]').op('&&')(timerange),
        Rental.id != rental.id,
    ).first()

    if other_rental is not None:
        raise RentalRangeOverlapException("Key has an other rental in this timerange.")

    return edit_object(rental, processor, log_params={'rental': REFERENCED_OBJ,
                                                      'key': rental.key,
                                                      'user': rental.user}, **kwargs)


@with_transaction
def delete_rental(rental: Rental, processor: User):
    return delete_object(rental, processor, log_params={'rental': REFERENCED_OBJ})


def create_user_pdf(user: User, processor: User):
    env = Environment(
        loader=FileSystemLoader('lib/templates/'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    user_template = env.get_template('user.html')

    rentals = session.query(Rental).filter_by(user=user, deleted=False).order_by(Rental.begin).all()

    html = user_template.render(
        now=utcnow().strftime("%Y-%m-%d %H:%M"),
        user=user,
        processor=processor,
        rentals=rentals
    )

    pdf = pdfkit.from_string(html, False)

    return pdf
