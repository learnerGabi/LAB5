#Make this file a minimalist API endpoint that randomly offers a random pick out of 
#15 meal recommendations along with a price
#The endpoint delivers 1 meal recommendation in JSON format

#from html(API) and put the data to database (JSON)
import os
from optparse import Values
from flask import Flask, jsonify
import random
import json
import psycopg2

app = Flask(__name__)

#input from API
#@app.route('/pickMeal', methods=['GET'])

# def get_db_connect():
#     return psycopg2.connect(host=os.environ.get('DB_HOST'), port, database, user, password)

def get_rec_from_db():
    q = """
    SELECT MealName, MealPrice FROM meals ...
    
    """

    conn = get_db_connect()
    cursor = conn.cursor()
    cursor.execute(q)
    mr = cursor.fetchall()

    conn.cloase()
    return mr

def get_meal_recommendation():
    meals = [
        {'name': 'Krusty Burger', 'price':4.99},
        {'name': 'Krusty Burger2', 'price':6.99},
        {'name': 'Double Krusty Burger', 'price':8.99},
        {'name': 'Deep Fried Krusty Burger', 'price':12.99},
        {'name': 'Mother Nature Burger', 'price':7.99},
        {'name': 'Double Double Double Double', 'price':12.99},
        {'name': 'Meat-Flavored Sandwich', 'price':0.99},
        {'name': 'The Clogger', 'price':3.99},
        {'name': 'Whatchamachicken', 'price':4.99},
        {'name': 'Krusty Popcorn', 'price':8.99},
        {'name': 'Soda', 'price':2.99},
        {'name': 'Mega Sugar Soda', 'price':2.99},
        {'name': 'Krusty-Partially-Gelatinated-Non-Dairy-Gum-Based-Beverage', 'price':8.99},
        {'name': 'Hot Lettuce Injection', 'price':8.99},
    ]
    
    return meals[random.randint(0,(len(meals)-1))]

@app.route('/')
@app.route('/recommendation/')
def index():
    return jsonify(get_meal_recommendation())


app.run(host='0.0.0.0', port=os.environ.get("API_PORT"))