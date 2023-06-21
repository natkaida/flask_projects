from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from models import db, Patient

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///patients.db'
db.init_app(app)

@app.route('/')
def index():
    patients = Patient.query.all()
    return render_template('index.html', patients=patients)

@app.route('/add', methods=['GET', 'POST'])
def add_patient():
    if request.method == 'POST':
        name = request.form['name']
        details = request.form['details']
        weight = float(request.form['weight'])
        age = float(request.form['age'])
        owner_name = request.form['owner_name']
        patient = Patient(name=name, details=details, weight=weight, age=age, owner_name=owner_name)
        db.session.add(patient)
        db.session.commit()
        return redirect('/')
    return render_template('add.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_patient(id):
    patient = Patient.query.get_or_404(id)
    if request.method == 'POST':
        patient.name = request.form['name']
        patient.details = request.form['details']
        patient.weight = float(request.form['weight'])
        patient.age = float(request.form['age'])
        patient.owner_name = request.form['owner_name']
        db.session.commit()
        return redirect('/')
    return render_template('edit.html', patient=patient)

@app.route('/delete/<int:id>', methods=['POST'])
def delete_patient(id):
    patient = Patient.query.get_or_404(id)
    db.session.delete(patient)
    db.session.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)