import csv
from flask import Flask
from models import db, Category, Item, Manufacturer

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'

db.init_app(app)

def create_db():
    # read in csv file using csv module
    with open('info.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        rows = list(reader)

    # lowercase column names and replace spaces with underscores
    for row in rows:
        row['name'] = row.pop('Name')
        row['description'] = row.pop('Description')
        row['price'] = float(row.pop('Price').replace(',', '.'))
        row['quantity'] = int(row.pop('Quantity'))
        row['category'] = row.pop('Category')
        row['manufacturer'] = row.pop('Manufacturer')

    # create database
    with app.app_context():
        db.create_all()

        # add categories to database
        categories = set(row['category'] for row in rows)
        for name in categories:
            category = Category(name=name)
            db.session.add(category)

        # add manufacturers to database
        manufacturers = set(row['manufacturer'] for row in rows)
        for name in manufacturers:
            manufacturer = Manufacturer(name=name)
            db.session.add(manufacturer)

        # add items to database
        for row in rows:
            item = Item(name=row['name'], description=row['description'], price=row['price'], quantity=row['quantity'])
            # set category relationship
            category_name = row['category']
            category = Category.query.filter_by(name=category_name).first()
            item.category = category
            # set manufacturer relationship
            manufacturer_name = row['manufacturer']
            manufacturer = Manufacturer.query.filter_by(name=manufacturer_name).first()
            item.manufacturers.append(manufacturer)
            db.session.add(item)

        db.session.commit()

        return "Database created successfully!"

if __name__ == "__main__":
    with app.app_context():
        create_db()