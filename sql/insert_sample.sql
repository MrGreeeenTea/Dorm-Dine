INSERT INTO dorm (name, adress, district, postcode, place)
VALUES ('Studentenwohnheim Mitte','Musterstraße 12', 'Mitte', '10115', 'Berlin');

INSERT INTO user ( email, password_hash, username, first_name, last_name, profile_picture, bio, dorm_id, is_cook, phone_number)
VALUES ('max.mustermann@example.com', 'scrypt:32768:8:1$i9PkkwgjsDRxv0E1$03c3d203f3577552166108265343eb7be803d60dfc5b605e51f7ee596cb88e86a903efff5e96b126365c6108340a84c790a5e3bef3da62588d00fa355d457140', 'max123', 'Max', 'Mustermann', 'https://example.com/profile.jpg', 'Hey, my name is Max and I study Business Information Systems ', 1, TRUE, '+49123456789');

INSERT INTO language (name)
VALUES ('German');

INSERT INTO language (name)
VALUES ('English');

INSERT INTO user_language (user_id, language_id) VALUES (1, 1);
INSERT INTO user_language (user_id, language_id) VALUES (1, 2);