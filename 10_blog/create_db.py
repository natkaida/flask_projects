from flask import Flask
from models import Post, Tag, Category, db
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db.init_app(app)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

        # Создаем примеры категорий
        category1 = Category(name='Разработка')
        category2 = Category(name='Обучение')
        category3 = Category(name='Хобби')

        # Добавляем категории в базу
        db.session.add(category1)
        db.session.add(category2)
        db.session.add(category3)
        db.session.commit()

        # Создаем примеры тегов
        tag1 = Tag(name='Python')
        tag2 = Tag(name='JavaScript')
        tag3 = Tag(name='Кино')

        # Добавляем теги в базу
        db.session.add(tag1)
        db.session.add(tag2)
        db.session.add(tag3)
        db.session.commit()

        # Тестовые посты
        post1 = Post(title='Начинаем изучать Flask', 
            content='Flask - это Python-фреймворк для быстрой разработки веб-приложений.', 
            date=datetime.utcnow(), category_id=category1.id)
        post2 = Post(title='Пишем первое приложение на JavaScript', 
            content='Напишем калькулятор на JavaScript с нуля.', 
            date=datetime.utcnow(), category_id=category2.id)
        post3 = Post(title='10 фильмов про роботов и ИИ', 
            content='Пересмотрели все фильмы про ИИ и роботов? Эти вы точно еще не смотрели.', 
            date=datetime.utcnow(), category_id=category3.id)

        # Добавляем теги к постам
        post1.tags.append(tag1)
        post2.tags.append(tag2)
        post3.tags.append(tag3)

        # Сохраняем посты в БД
        db.session.add(post1)
        db.session.add(post2)
        db.session.add(post3)
        db.session.commit()