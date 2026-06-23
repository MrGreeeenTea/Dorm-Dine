from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash

db = SQLAlchemy()

def insert_sample():
    from models.dorm import Dorm
    from models.user import User
    from models.dish import Dish
    from models.tag import Tag
    from models.dish_tag import DishTag
    from models.language import Language
    from models.user_language import UserLanguage

    # Alle bestehenden Daten löschen
    db.session.execute(db.delete(UserLanguage))
    db.session.execute(db.delete(DishTag))
    db.session.execute(db.delete(Dish))
    db.session.execute(db.delete(User))
    db.session.execute(db.delete(Dorm))
    db.session.execute(db.delete(Tag))
    db.session.execute(db.delete(Language))

    # Beispieldaten erstellen
    dorm1 = Dorm(name='Wohnheim Nollendorfstraße', address='Nollendorfstraße 21a', district='Tempelhof-Schöneberg', postcode='10777', place='Berlin')
    dorm2 = Dorm(name='Wohnheim Halbauer Weg', address='Halbauer Weg 19-21', district='Lankwitz-Steglitz', postcode='12249', place='Berlin')
    dorm3 = Dorm(name='Wohnheim Franz-Mehring-Platz', address='Franz-Mehring-Platz 2, 3', district='Friedrichshain-Kreuzberg', postcode='10243', place='Berlin')

    user1 = User(email='max.mustermann@example.com', password_hash=generate_password_hash('Password_123'), username='max123', first_name='Max', last_name='Mustermann', bio='Hey, my name is Max and I study Business Information Systems!', is_cook=True, phone_number='+49123456789')
    user1.dorm = dorm1
    user2 = User(email='lisa.meier@example.com', password_hash=generate_password_hash('Password_112'), username='lisa112', first_name='Lisa', last_name='Meier', bio='Hey, my name is Lisa and I study Computer Science!', is_cook=False, phone_number='+49123456788')
    user2.dorm = dorm2
    user3 = User(email='anna.schmidt@example.com', password_hash=generate_password_hash('Password_113'), username='anna113', first_name='Anna', last_name='Schmidt', bio='Hey, my name is Anna and I study Psychology!', is_cook=True, phone_number='+49123456787')
    user3.dorm = dorm3

    tag1 = Tag(name='Italian')
    tag2 = Tag(name='comfort food')

    lang1 = Language(name='German')
    lang2 = Language(name='English')

    db.session.add_all([dorm1, dorm2, dorm3, user1, user2, tag1, tag2, lang1, lang2])
    db.session.commit()

    from datetime import datetime
    dish1 = Dish(cook_id=user1.id, name='Lasagne',
                 description='Traditional Italian pasta baked with rich meat sauce, layered with creamy bechamel and Gouda cheese.', price='2.00', total_portions=6, left_portions=6,pickup_time=datetime(2026, 6, 30, 17, 15), pickup_timeend=datetime(2026, 6, 30, 18, 0), status='scheduled')
    db.session.add(dish1)
    db.session.commit()

    db.session.add_all([
        DishTag(dish_id=dish1.id, tag_id=tag1.id),
        DishTag(dish_id=dish1.id, tag_id=tag2.id),
        UserLanguage(user_id=user1.id, language_id=lang1.id),
        UserLanguage(user_id=user1.id, language_id=lang2.id),
    ])
    db.session.commit()