INSERT INTO dorm (name, adress, district, postcode, place)
VALUES ('Studentenwohnheim Mitte','Musterstraße 12', 'Mitte', '10115', 'Berlin');

INSERT INTO user ( email, password_hash, username, first_name, last_name, profile_picture, bio, dorm_id, is_cook, phone_number)
VALUES ('max.mustermann@example.com', 'Password_123', 'max123', 'Max', 'Mustermann', 'https://example.com/profile.jpg', 'Hey, my name is Max and I study Business Information Systems ', 1, TRUE, '+49123456789');

INSERT INTO language (name) VALUES ('German');

INSERT INTO language (name) VALUES ('English');

INSERT INTO user_language (user_id, language_id) VALUES (1, 1);
INSERT INTO user_language (user_id, language_id) VALUES (1, 2);

INSERT INTO dish (cook_id, name, description, price, total_portions, pickup_time, status)
VALUES (1, 'Lasagne', 'Traditional Italian pasta baked with rich meat sauce, layered with creamy béchamel and Gouda cheese.', 2.00, 6, '2026-06-16 17:15:00' , 'scheduled' );

INSERT INTO dish_order (buyer_id, dish_id, portions, message, status)
VALUES (2, 1, 2, 'Thank you!', 'pending');

INSERT INTO message (sender_id, receiver_id, order_id, content)
VALUES (2, 1, 1, 'Where do you want to meet up? :)');

INSERT INTO tag (name) VALUES ('Italian');
INSERT INTO tag (name) VALUES ('vegan');
INSERT INTO tag (name) VALUES ('vegetarian');
INSERT INTO tag (name) VALUES ('comfort food');
INSERT INTO tag (name) VALUES ('soul food');
INSERT INTO tag (name) VALUES ('spicy(mild)');
INSERT INTO tag (name) VALUES ('spicy(hot)');
INSERT INTO tag (name) VALUES ('spicy(very hot)');
INSERT INTO tag (name) VALUES ('from scratch');
INSERT INTO tag (name) VALUES ('Korean');
INSERT INTO tag (name) VALUES ('Chinese');
INSERT INTO tag (name) VALUES ('Indian');
INSERT INTO dish_tag (dish_id, tag_id) VALUES (1, 1);