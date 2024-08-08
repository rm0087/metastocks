# server/app.py

from flask import Flask, request
from flask_migrate import Migrate

from config import app, db