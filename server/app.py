from flask import Flask, request
from flask_migrate import Migrate
from models import Type, Keyword, Company, Country, associations

from config import app, db

with app.app_context():
    db.create_all()
    print("Tables created!")

@app.get('/')
def index():
    return "Hello world"