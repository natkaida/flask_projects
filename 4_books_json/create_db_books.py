from flask import Flask
from models import Book, db
import json
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

        with open('books.json', encoding='utf-8') as f:
            books_data = json.load(f)

        for book_data in books_data:
            book = Book(title=book_data['название'], author=book_data['автор'], year=book_data['год публикации'], description=book_data['описание'])
            db.session.add(book)

        db.session.commit()
