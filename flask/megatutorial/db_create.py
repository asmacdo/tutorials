#!/home/austin/.virtualenvs/flask_mega/bin/python

from migrate.versioning import api
from config import SQLALCHEMY_DATABASE_URI
from config import SQLALCHEMY_MIGRAGE_REPO
from app import db
import os.path

db.create_all()
if not os.path.exists(SQLALCHEMY_MIGRAGE_REPO):
    api.create(SQLALCHEMY_MIGRAGE_REPO, 'database repository')
    api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRAGE_REPO)
else:
    api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRAGE_REPO, api.version(SQLALCHEMY_MIGRAGE_REPO))