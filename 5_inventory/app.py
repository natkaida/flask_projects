from flask import Flask, render_template
from models import db, Manufacturer, Category, Item

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
db.init_app(app)

@app.route('/')
def index():
    manufacturers = Manufacturer.query.all()
    return render_template('index.html', manufacturers=manufacturers)

@app.route('/<manufacturer>/categories')
def show_categories(manufacturer):
    manufacturer = Manufacturer.query.filter_by(name=manufacturer).first()
    items = manufacturer.items
    categories = set(item.category for item in items)
    return render_template('categories.html', manufacturer=manufacturer, categories=categories)

@app.route('/<manufacturer>/<category>')
def show_items(manufacturer, category):
    items = Item.query.join(Item.manufacturers).join(Item.category).\
                filter(Manufacturer.name == manufacturer).\
                filter(Category.name == category).all()
    return render_template('items.html', manufacturer=manufacturer, category=category, items=items)

if __name__ == '__main__':
    app.run(debug=True)