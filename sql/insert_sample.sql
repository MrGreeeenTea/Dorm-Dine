INSERT INTO dorm (name, adress, district, postcode, place)
VALUES ('Studentenwohnheim Mitte','Musterstraße 12', 'Mitte', '10115', 'Berlin');

INSERT INTO user ( email, password_hash, username, first_name, last_name, profile_picture, bio, dorm_id, is_cook, phone_number)
VALUES ('max.mustermann@example.com', 'Password_123', 'max123', 'Max', 'Mustermann', 'https://example.com/profile.jpg', 'Hey, my name is Max and I study Business Information Systems ', 1, TRUE, '+49123456789');

INSERT INTO language (name)
VALUES ('German');

INSERT INTO language (name)
VALUES ('English');

INSERT INTO user_language (user_id, language_id) VALUES (1, 1);
INSERT INTO user_language (user_id, language_id) VALUES (1, 2);