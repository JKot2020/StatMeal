# server.py
# Hosting directory for StatMeal

from distutils.log import debug 
from fileinput import filename 
from flask import *

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home_page():
    return render_template('App.js')

if __name__ == "__main__":
    app.run(debug=True)