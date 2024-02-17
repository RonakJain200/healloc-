from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/db_name'
db = SQLAlchemy(app)

class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    specialization = db.Column(db.String(100))
    experience = db.Column(db.Integer)
    location = db.Column(db.String(100))
    pincode = db.Column(db.String(10))
    degree = db.Column(db.String(100))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        specialization = request.form['specialization']
        experience = request.form['experience']
        location = request.form['location']
        pincode = request.form['pincode']
        degree = request.files['degree'].filename
        
        doctor = Doctor(name=name, specialization=specialization, experience=experience, location=location, pincode=pincode, degree=degree)
        db.session.add(doctor)
        db.session.commit()
        
        flash('Doctor details added successfully!', 'success')

    return render_template('signup.html')

if __name__ == '__main__':
    app.secret_key = 'secret_key'
    app.run(debug=True)


