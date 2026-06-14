CREATE TABLE dorm (
    id INTEGER PRIMARY KEY, 
    name TEXT NOT NULL,
    adress TEXT NOT NULL,
    district TEXT NOT NULL,
    postcode TEXT NOT NULL,
    place TEXT NOT NULL
);

CREATE TABLE user (
    id INTEGER PRIMARY KEY,
    email TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    username  TEXT UNIQUE NOT NULL,
    first_name TEXT NOT NULL,
    last_name  TEXT NOT NULL,
    profile_picture TEXT,
    bio TEXT,
    dorm_id INTEGER,
    is_cook BOOLEAN DEFAULT FALSE,
    phone_number TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (dorm_id) REFERENCES dorm(id) ON DELETE SET NULL
);

CREATE TABLE language (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE user_language (
    language_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    PRIMARY KEY (language_id, user_id),
    FOREIGN KEY (language_id) REFERENCES language(id) ON DELETE CASCADE,
    FOREIGN KEY (user_id)  REFERENCES user(id)  ON DELETE CASCADE
);

CREATE TABLE icon (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    image_url TEXT NOT NULL
);

CREATE TABLE dish (
    id INTEGER PRIMARY KEY,
    cook_id INTEGER NOT NULL,
    icon_id INTEGER,
    name TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL,
    total_portions INTEGER NOT NULL,
    pickup_time TIMESTAMP NOT NULL, 
       status TEXT NOT NULL CHECK (
        status IN (
            'scheduled',
            'active',
            'sold_out',
            'cancelled',
            'completed'
        )
    ),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (cook_id) REFERENCES user(id) ON DELETE CASCADE,
    FOREIGN KEY (icon_id) REFERENCES icon(id) ON DELETE SET NULL
);

CREATE TABLE dish_photo (
    id INTEGER PRIMARY KEY,
    dish_id INTEGER NOT NULL,
    photo_url TEXT NOT NULL,
    is_primary BOOLEAN DEFAULT FALSE,   -- Hauptbild für Feed-Anzeige
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (dish_id) REFERENCES dish(id) ON DELETE CASCADE
);

CREATE TABLE tag (
    id INTEGER PRIMARY KEY,
    name TEXT UNIQUE NOT NULL    -- z.B. 'vegetarisch', 'vegan'
);

CREATE TABLE dish_tag (
    dish_id INTEGER NOT NULL,
    tag_id  INTEGER NOT NULL,
    PRIMARY KEY (dish_id, tag_id),
    FOREIGN KEY (dish_id) REFERENCES dish(id) ON DELETE CASCADE,
    FOREIGN KEY (tag_id)  REFERENCES tag(id)  ON DELETE CASCADE
);

CREATE TABLE dish_order (
    id INTEGER PRIMARY KEY,
    buyer_id INTEGER NOT NULL,
    dish_id INTEGER NOT NULL,
    portions INTEGER NOT NULL DEFAULT 1,
    message TEXT,             
    status TEXT NOT NULL DEFAULT 'pending' CHECK(
        status IN(
            'pending',
            'confirmed',
            'ready',
            'picked_up',
            'cancelled'
        )
    ),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (buyer_id) REFERENCES user(id) ON DELETE CASCADE,
    FOREIGN KEY (dish_id)  REFERENCES dish(id) ON DELETE CASCADE
);

-- Küchensauberkeits-Nachweise (Foto + handgeschriebener Zeitstempel)
CREATE TABLE kitchen_proof (
    id INTEGER PRIMARY KEY,
    dish_id INTEGER NOT NULL,
    cook_id INTEGER NOT NULL,
    photo_url TEXT NOT NULL,
    proof_type TEXT NOT NULL CHECK (proof_type IN ('before', 'after')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (dish_id) REFERENCES dish(id) ON DELETE CASCADE,
    FOREIGN KEY (cook_id) REFERENCES user(id) ON DELETE CASCADE
);

CREATE TABLE message (
    id INTEGER PRIMARY KEY,
    sender_id INTEGER NOT NULL,
    receiver_id INTEGER NOT NULL,
    order_id INTEGER,                    
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (sender_id) REFERENCES user(id) ON DELETE CASCADE,
    FOREIGN KEY (receiver_id) REFERENCES user(id) ON DELETE CASCADE,
    FOREIGN KEY (order_id) REFERENCES dish_order(id) ON DELETE SET NULL
);

CREATE TABLE notification (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    order_id INTEGER,
    types TEXT NOT NULL CHECK(
        types IN(
            'new_order',
            'order_confirmed',
            'dish_ready',
            'order_cancelled'
        )
    ),
    message TEXT NOT NULL,
    is_read BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES user(id) ON DELETE CASCADE,
    FOREIGN KEY (order_id) REFERENCES dish_order(id) ON DELETE SET NULL
);