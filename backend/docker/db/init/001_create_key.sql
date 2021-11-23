INSERT INTO "user"(login, name, email) VALUES ('abc', 'Test User 1', 'user1@mail.de'),
                                            ('def', 'Test User 2', 'user2@mail.de');

INSERT INTO location(name, address, latitude, longitude) VALUES ('Test Location 1', 'Dresden', 0, 0),
                                                                ('Test Location 2', 'Leipzig', 0, 0);

INSERT INTO safe(name, location_id) VALUES ('Test Safe 1', (SELECT id FROM location LIMIT 1)),
                                           ('Test Safe 2', (SELECT id FROM location LIMIT 1));

INSERT INTO lock(name, owner, location_id) VALUES ('Test Lock 1', (SELECT id FROM "user" LIMIT 1), (SELECT id FROM location LIMIT 1)),
                                                  ('Test Lock 2', (SELECT id FROM "user" LIMIT 1), (SELECT id FROM location LIMIT 1));

INSERT INTO key(number, lock_id, safe_id) VALUES (2, (SELECT id FROM lock LIMIT 1), (SELECT id FROM safe LIMIT 1)),
                                                 (3, (SELECT id FROM lock LIMIT 1), (SELECT id FROM safe LIMIT 1));