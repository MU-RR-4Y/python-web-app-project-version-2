from flask import Flask, render_template, redirect, request
from flask import Blueprint
from models.country import Country
from models.destination import Destination
from models.wishlists import Wishlist
import repositories.country_repository as country_repo
import repositories.destination_respository as destination_repo
import repositories.user_repository as user_repo
import repositories.wishlist_repo as wishlist_repo
import repositories.visit_repository as visit_repo

destinations_blueprint = Blueprint('destinations', __name__)

# INDEX ('/') GET
@destinations_blueprint.route('/destinations')
def destinations():
    destinations = destination_repo.select_all()
    countries = country_repo.select_all() 
    wishlist_destination =wishlist_repo.most_wishlisted_destintion()
    visited_destination = visit_repo.most_most_visited_destination()

    return render_template('/destinations/index.html', destinations = destinations, countries = countries, wishlist_destination = wishlist_destination, visited_destination = visited_destination)

# NEW ('/new') GET
# request form to add destination from destination page - new.html
@destinations_blueprint.route('/destinations/new')
def add_destintion():
    countries =country_repo.select_all()
    return render_template('/destinations/new.html', countries = countries)


# request form to add destination from a country page - new2.html
@destinations_blueprint.route('/destinations/new/<id>')
def add_destintion_to_country(id):
    country = country_repo.select((int(id)))
    return render_template('/destinations/new2.html', country = country)
    


# CREATE ('/') POST
# Add a destination from the destination page
@destinations_blueprint.route('/destinations/create', methods =['POST'])
def create_destination():
    name = request.form['name']
    information =request.form['info']
    country_form = request.form['country']
    countries = country_repo.select_all()
    for country_item in countries:
        if country_form == country_item.name:
            country = country_item

    destination = Destination(name,country,information)
    destination_repo.save(destination)
    return redirect('/destinations')
    

# Add a destination from a country page
@destinations_blueprint.route('/destinations/create/<id>', methods =['POST'])
def create_destination_country_page(id):
    name = request.form['name']
    information =request.form['info']
    country = country_repo.select(int(id))
    destination = Destination(name,country,information)
    destination_repo.save(destination)
    return redirect('/countries')




# SHOW ('/id') GET
@destinations_blueprint.route('/destinations/show/<id>')
def show_destination(id):
    destination = destination_repo.select(id)
    users = user_repo.visited_on_destinations(destination)
    return render_template('/destinations/show.html', destination = destination, users = users)





# EDIT ('/id/edit') GET
# UPDATE ('/id') POST

# DELETE ('/id/delete') POST
#Delete from destination page
@destinations_blueprint.route('/destination/<id>/delete', methods=['POST'])
def delete_destination(id):
    destination_repo.delete(id)
    return redirect('/destinations')

#delete from country page
@destinations_blueprint.route('/destination/<id>/delete/country', methods=['POST'])
def delete_destination_from_country(id):
    destination_repo.delete(id)
    return redirect(request.referrer)