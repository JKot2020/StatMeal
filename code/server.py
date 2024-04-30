# server.py
# Hosting directory for StatMeal

from distutils.log import debug 
from fileinput import filename 
from fpdf import FPDF
from flask import *
from readFile import *
from generateGraph import *
from generatePredictive import *

app = Flask(__name__, template_folder='templates')

@app.route('/')
def main():   
    return render_template('statmeal.html')

@app.route('/home')
def home():   
    return render_template('statmeal.html')

@app.route('/graph-maker-landing')
def graph_landing():   
    return render_template('graphMakerLanding.html')
  
@app.route('/graph-maker', methods = ['POST'])   
def graph():
    if request.method == 'POST':   
        f = request.files['file'] 
        f.save(f.filename)
        return render_template("graphMaker.html", name = f.filename, column = get_file(f.filename))

@app.route('/graph-output', methods = ['POST'])
def graph_output():
    if request.method == 'POST':
        file = request.form.get('file')
        columns = request.form.get('columns')
        graph = request.form.get('graph')
        return render_template('graphMakerOutput.html', output_graph = sort_graph_data(file, columns, graph), test_graph = graph)
    
@app.route('/predict-maker-landing')
def predict_landing():
    return render_template('predictMakerLanding.html')
    
@app.route('/predict-maker', methods = ['POST'])   
def predict():   
    if request.method == 'POST':   
        f = request.files['file'] 
        f.save(f.filename)
        return render_template("predictMaker.html", name = f.filename, column = get_file(f.filename))
    
@app.route('/regression-output', methods = ['POST'])
def regression_output():
    if request.method == 'POST':
        file = request.form.get('file')
        columns = request.form.get('columns')
        make_regression(file, columns)

        pdf = FPDF()   
        pdf.add_page()
        pdf.set_font("Arial", size = 10)
        my_path = os.path.abspath(__file__)

        # Remove "/server.py" from file path
        my_path = my_path[:-9]

        # generate pdf file format
        f = open(my_path + "/static/Regression.txt", "r")
        for x in f:
            pdf.cell(200, 10, txt = x, ln = 1, align = 'L')
        pdf.set_font('Roboto')
        pdf.output(my_path + "/static/Regression.pdf")

        return render_template("regressionOutput.html")

@app.route('/predict-output', methods = ['POST'])
def predict_output():
    if request.method == 'POST':
        file = request.form.get('file')
        columns = request.form.get('columns')
        return render_template('predictOutput.html', predict_data = make_predictive(file, columns))

if __name__ == '__main__':   
    app.run(debug=True)