from flask import Flask, render_template, redirect, request
from flask import Blueprint
from models.country import Country
import repositories.country_repository as country_repo
import repositories.destination_respository as destination_repo

countries_blueprint = Blueprint('countries', __name__)

# INDEX ('/') GET
@countries_blueprint.route('/countries')
def countries():
    destinations = destination_repo.select_all()
    countries = country_repo.select_all()
    return render_template('countries/index.html', countries = countries, destinations =destinations)


# NEW ('/new') GET
@countries_blueprint.route('/countries/new')
def new_country():
    return render_template('countries/new.html')

# CREATE ('/') POST
@countries_blueprint.route('/countries/create', methods=['POST'])
def add_country():
    name = request.form['name']
    country = Country(name)
    country_repo.save(country)
    return redirect('/countries')


# SHOW ('/id') GET
@countries_blueprint.route('/countries/show/<id>')
def show_country(id):
    country = country_repo.select(id)
    destinations = destination_repo.select_all()
    destination_list = destination_repo.select_all()
    destinations=[]
    for destination in destination_list:
        if destination.country.id == int(country.id):
            destinations.append(destination)
    return render_template('/countries/show.html', selected_country = country, destinations = destinations)

    


# EDIT ('/id/edit') GET
# UPDATE ('/id') POST
# DELETE ('/id/delete') POST
