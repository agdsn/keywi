FROM python:3.12

ARG UID=1000
ARG GID=1000
ENV LANG=C.UTF-8 DEBIAN_FRONTEND=noninteractive PYTHONUNBUFFERED=1

RUN groupadd --force --gid $GID app \
    && useradd --non-unique --home-dir /opt/app --create-home --uid $UID --gid $GID --comment "Application" app

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        libpango-1.0-0 libpangoft2-1.0-0 libharfbuzz-subset0 fonts-texgyre \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /opt/app

COPY --chown=app:app ./keywi/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY --chown=app:app ./keywi/ ./

USER app

CMD ["python", "-m", "keywi"]
