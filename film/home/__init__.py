from flask import Blueprint
 
home = Blueprint('home',__name__)

import film.home.views
