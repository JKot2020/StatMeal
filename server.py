# server.py
# Hosting directory for StatMeal

from distutils.log import debug 
from fileinput import filename 
from flask import *
from readFile import get_file

app = Flask(__name__, template_folder='templates')

@app.route('/')   
def main():   
    return render_template('statmeal.html')
  
@app.route('/success', methods = ['POST'])   
def success():   
    if request.method == 'POST':   
        f = request.files['file'] 
        f.save(f.filename)
        return render_template("graphMaker.html",name = f.filename, column = get_file(f.filename))
  
if __name__ == '__main__':   
    app.run(debug=True)