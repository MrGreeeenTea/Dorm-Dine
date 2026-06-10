BEGIN TRANSACTION;
DELETE from user;
DELETE from studentenwohnheim;
DELETE from sqlite_sequence;
INSERT INTO user (name, email, password_hash, studentenwohnheim_id) VALUES ("Tom", "tom@mail.com", "123456789", 1);
INSERT INTO studentenwohnheim (id) VALUES (1);
COMMIT;

