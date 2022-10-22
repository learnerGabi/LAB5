# Make this file a minimalist API consumer 
# that displays the random meal recommendation 
# along with the price 
# (use a HTML template)

from flask import Flask, render_template
import os
import json
from urllib.request import urlopen


app = Flask(__name__)

@app.route('/')
@app.route('/index')
def get_reccomendation():
    url = "http://{api_host}:{api_port}/recommendation/".format(api_host = os.environ.get("API_HOST"),
                                                                api_port = os.environ.get("API_PORT"))
    response = urlopen(url)
    data = response.read()
    dict = json.loads(data)
    #r = requests.get('http://api:6000/pickMeal')
    
    return render_template('index.html', meal=dict['name'], price=dict['price'])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ.get("CON_PORT"))