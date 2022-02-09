
from app import forms, db
from app import app as appli
from flask import render_template, request, redirect, flash, abort, url_for
import json
from app import models

list_of_cities=[]
@appli.route('/', methods=("GET","POST"))
@appli.route('/login', methods=("GET","POST"))
def login():
    my_form = forms.Form()
    if my_form.validate_on_submit():  # Check if the form has been filled
        username = my_form.username.data  # Get
        password = my_form.password.data  # The
        bio = my_form.bio.data  # Data

        print("Here is what I got from the form:")
        print("username:", username)
        print("password:", password)
        print("bio:", bio)
        # Do something with the data

        return redirect('/')
    return render_template('login.html', form=my_form)


@appli.route('/form', methods=('GET','POST'))
def get_data():
    #abort(404)
    if request.method == 'POST':
        city = request.form.get('city')
        country = request.form.get('country')
        population = request.form.get('population')
        area = request.form.get('city_area')
        longitude = request.form.get('longitude')
        latitude = request.form.get('latitude')
        capital = request.form.get('capital')
        print(city, country, population)
        print('end of post method')
        city= {'name': city,
               'country': country,
               'population':population,
               'area':area,
               'longitude': longitude,
               'latitude': latitude,
               'is_capital':capital}
        list_of_cities.append(city)
        with open('cities_around_the_world.json', 'w') as file:
            json.dump(list_of_cities, file)
        flash('Congratulations, you added a new city', 'error')


    print('inside get method')
    return render_template('add_cityyy.html')

@appli.route('/student', methods=('GET', 'POST'))
def student():
    form = forms.Inscription_Form()
    if form.validate_on_submit():  # Check if the form has been filled
        name = form.first_name.data  # Get
        last_name = form.last_name.data  # The
        age = form.age.data  # Data

        new_student= models.Student(id=6, first_name=name, last_name= last_name, age=age)
        db.session.add(new_student)
        db.session.commit()

        all_students = models.Student.query.all()
        print(all_students[1].first_name)
        print(all_students)
        flash(f'Welcome to our school {name}')
        return redirect(url_for('home'))
    return render_template('student_signin.html', form=form)


@appli.route('/home')
def home():
    all_students = models.Student.query.all()
    return render_template('home.html', students=all_students)
