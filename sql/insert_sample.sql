INSERT INTO dorm (
    name,
    adress,
    district,
    postcode,
    place
)
VALUES (
    'Studentenwohnheim Mitte',
    'Musterstraße 12',
    'Mitte',
    '10115',
    'Berlin'
);

INSERT INTO users (
    email,
    password_hash,
    username,
    first_name,
    last_name,
    profile_picture,
    bio,
    dorm_id,
    is_cook,
    phone_number
)
VALUES (
    'max.mustermann@example.com',
    'Password_123',
    'max123',
    'Max',
    'Mustermann',
    'https://example.com/profile.jpg',
    'Hey, ich heiße Max und bin Student an der HWR Berlin ',
    1,
    TRUE,
    '+49123456789'
);

INSERT INTO language (name)
VALUES ('Deutsch');

INSERT INTO language (name)
VALUES ('English');

INSERT INTO users_language (
    users_id,
    language_id
)
VALUES
    (1, 1),
    (1, 2);