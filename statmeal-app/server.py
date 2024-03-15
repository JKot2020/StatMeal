# server.py
# Hosting directory for StatMeal

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home_page():
    return "<p>Test</p>"
    #return render_template('App.js')

if __name__ == "__main__":
    app.run(debug=True)