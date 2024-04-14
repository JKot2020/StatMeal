# server.py
# Hosting directory for StatMeal

from distutils.log import debug 
from fileinput import filename 
from flask import *
from readFile import *
from generateGraph import *

app = Flask(__name__, template_folder='templates')

@app.route('/')
def main():   
    return render_template('statmeal.html')

@app.route('/home')
def home():   
    return render_template('statmeal.html')
  
@app.route('/graph-maker', methods = ['POST'])   
def predict():
    if request.method == 'POST':   
        f = request.files['file'] 
        f.save(f.filename)
        return render_template("graphMaker.html", name = f.filename, column = get_file(f.filename))

@app.route('/predict-maker', methods = ['POST'])   
def graph():   
    if request.method == 'POST':   
        f = request.files['file'] 
        f.save(f.filename)
        return render_template("predictMaker.html", name = f.filename, column = get_file(f.filename))

@app.route('/graph-output', methods = ['POST'])
def graph_output():
    if request.method == 'POST':
        file = request.form.get('file')
        columns = request.form.get('columns')
        graph = request.form.get('graph')
        return render_template('graphMakerOutput.html', output_graph = sort_graph_data(file, columns, graph), test_graph = graph)

if __name__ == '__main__':   
    app.run(debug=True)