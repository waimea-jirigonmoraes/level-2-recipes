#===========================================================
# recepies
# By Julia Irigon Moraes 
#===========================================================

from flask import Flask, request, session, render_template, flash, redirect, send_file, make_response
from dotenv import load_dotenv
from os import getenv
from io import BytesIO
import html
from app.helpers import *


# Create the app
app = Flask(__name__)


#===========================================================
# App Routes Handlers
#===========================================================

#-----------------------------------------------------------
# Home page
#-----------------------------------------------------------
@app.get("/")
def show_home():
    return render_template("pages/home.jinja")

#-----------------------------------------------------------
# rECIPE LIST
#-----------------------------------------------------------
@app.get("/recipes")
def show_recipe_list():
    return render_template("pages/list.jinja")


#-----------------------------------------------------------
# Chocolate Cake 
#-----------------------------------------------------------
@app.get("/recipe/chocolate")
def show_choc_recipe():
    return render_template("pages/chocolate.jinja")


#===========================================================
# Configure the app
#===========================================================
#-----------------------------------------------------------
# Carrot cake
#-----------------------------------------------------------
@app.get("/recipe/carrot")
def show_carrot_recipe():
    return render_template("pages/carrot.jinja")
#-----------------------------------------------------------
# Ciabatta Bread
#-----------------------------------------------------------
@app.get("/recipe/ciabata")
def show_ciabata_recipe():
    return render_template("pages/ciabata.jinja")

load_dotenv()
app.config.from_prefixed_env()
init_logging(app)
init_text_filters(app)
init_date_filters(app)
init_error_handlers(app)

