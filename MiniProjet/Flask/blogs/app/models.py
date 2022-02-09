from datetime import datetime

from app import db


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True, )
    first_name= db.Column(db.String(64))
    last_name= db.Column(db.String(64))
    age= db.Column(db.Integer)
    inscription_date = db.Column(db.DateTime, default=datetime.now)
    _class = db.Column(db.Integer, db.ForeignKey('classe.class_id'))

    def __repr__(self):
        return f'<Student: {self.first_name}>'


class Courses(db.Model):
    course_id = db.Column(db.Integer, primary_key=True, )
    name = db.Column(db.String(64))
    chapter= db.Column(db.Integer)
    credits= db.Column(db.Integer)
    support = db.Column(db.String(200))
    _class = db.Column(db.Integer, db.ForeignKey('classe.class_id'))


class Classe(db.Model):
    class_id = db.Column(db.Integer, primary_key=True, )
    name= db.Column(db.String(64))
    is_exam=db.Column(db.Boolean)
    nombre_eleves = db.Column(db.Integer)
    student = db.relationship(Student, backref='classe', lazy='dynamic')
    course = db.relationship(Courses, backref='classe', lazy='dynamic')


from app import routes, app

