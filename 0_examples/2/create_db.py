from flask import Flask
from models import Artist, Album, Song, db
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///music.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

        # создаем тестовых исполнителей
        artist1 = Artist(name='The Rolling Stones')
        artist2 = Artist(name='Jefferson Airplane')
        artist3 = Artist(name='Nine Inch Nails')
        artist4 = Artist(name='Tool')
        db.session.add_all([artist1, artist2, artist3, artist4])
        db.session.commit()

        # создаем тестовые альбомы
        album1 = Album(title='Aftermath', year='1966', artist=artist1)
        album2 = Album(title='Beggars Banquet', year='1968', artist=artist1)
        album3 = Album(title='Surrealistic Pillow', year='1967', artist=artist2)
        album4 = Album(title='Broken', year='1992', artist=artist3)
        album5 = Album(title='The Fragile', year='1999', artist=artist3)
        album6 = Album(title='Lateralus', year='2001', artist=artist4) 
        album7 = Album(title='AEnima', year='1996', artist=artist4) 
        album8 = Album(title='10,000 Days', year='2006', artist=artist4) 

        # создаем тестовые песни
        song1 = Song(title='Paint it Black', length='4:20', track_number=1, album=album1)
        song2 = Song(title='Sympathy For The Devil', length='3:53', track_number=2, album=album1)
        song3 = Song(title='White Rabbit', length='3:42', track_number=5, album=album3)
        song4 = Song(title='Wish', length='3:46', track_number=6, album=album4)
        song5 = Song(title='Strafuckers, Inc.', length='5:00', track_number=1, album=album5)
        song6 = Song(title='Schism', length='6:46', track_number=7, album=album6)
        song7 = Song(title='Eulogy', length='8:29', track_number=3, album=album7)
        song8 = Song(title='Vicarious', length='7:07', track_number=5, album=album8)
        db.session.add_all([album1, album2, album3, album4, album5, album6, album7, album8, song1, song2, song3, song4, song5, song6, song7, song8])
        db.session.commit()