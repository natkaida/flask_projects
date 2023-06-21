from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, Category, Note

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes.db'
app.config['SECRET_KEY'] = 'your_secret_key_here'
db.init_app(app)


@app.route('/')
def index():
    notes = Note.query.all()
    return render_template('index.html', notes=notes)

@app.route('/note/<int:note_id>')
def note(note_id):
    note = Note.query.get_or_404(note_id)
    return render_template('note.html', note=note)

@app.route('/category/<int:category_id>')
def category(category_id):
    category = Category.query.get_or_404(category_id)
    return render_template('category.html', category=category)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        category_id = request.form['category']
        note = Note(title=title, content=content, category_id=category_id)
        db.session.add(note)
        db.session.commit()
        flash('Заметка успешно добавлена!')
        return redirect(url_for('index'))
    categories = Category.query.all()
    return render_template('add.html', categories=categories)

@app.route('/edit/<int:note_id>', methods=['GET', 'POST'])
def edit(note_id):
    note = Note.query.get_or_404(note_id)
    if request.method == 'POST':
        note.title = request.form['title']
        note.content = request.form['content']
        note.category_id = request.form['category']
        db.session.commit()
        flash('Заметка успешно обновлена!')
        return redirect(url_for('index'))
    categories = Category.query.all()
    return render_template('edit.html', note=note, categories=categories)

@app.route('/delete/<int:note_id>', methods=['GET', 'POST'])
def delete(note_id):
    note = Note.query.get_or_404(note_id)
    if request.method == 'POST':
        db.session.delete(note)
        db.session.commit()
        flash('Заметка удалена')
        return redirect(url_for('index'))
    return render_template('delete.html', note=note)

if __name__ == '__main__':
    app.run(debug=True)
