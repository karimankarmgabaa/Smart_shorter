from flask import Flask
from mongoframes import *
from pymongo import MongoClient

app = Flask(__name__)
app.mongo = MongoClient('mongodb+srv://admin:OhmDv6f5xifFKRsl@appgaintechnical-svuqh.mongodb.net/test?retryWrites=true')
Frame._client = app.mongo
