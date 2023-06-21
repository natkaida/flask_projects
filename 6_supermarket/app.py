from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from models import db, Grocery

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///groceries.db'
db.init_app(app)

@app.route('/', methods=['GET'])
def index():
    groceries = Grocery.query.all()
    return render_template('index.html', groceries=groceries)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        desc = request.form['description']
        weight = request.form['weight']
        quantity = request.form['quantity']
        price = request.form['price']
        new_item = Grocery(name=name, description=desc, weight=weight, quantity=quantity, price=price)
        db.session.add(new_item)
        db.session.commit()
        return redirect('/')
    return render_template('add.html')

if __name__ == '__main__':
    app.run(debug=True)