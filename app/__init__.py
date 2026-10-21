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
# Cake recipe
#-----------------------------------------------------------
@app.get("/recipe/cake")
def show_cake_recipe():
    return render_template("pages/cake.jinja")


#===========================================================
# Configure the app
#===========================================================
#-----------------------------------------------------------
# Bread recipe
#-----------------------------------------------------------
@app.get("/recipe/bread")
def show_bread_recipe():
    return render_template("pages/bread.jinja")
#-----------------------------------------------------------
# Muffin recipe
#-----------------------------------------------------------
@app.get("/recipe/muffin")
def show_muffin_recipe():
    return render_template("pages/muffin.jinja")

load_dotenv()
app.config.from_prefixed_env()
init_logging(app)
init_text_filters(app)
init_date_filters(app)
init_error_handlers(app)

