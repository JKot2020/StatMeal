# StatMeal

StatMeal is a web-application that allows a user to convert spreadsheet files into custom graphs and predictive models. There are several example .csv files included in the "examples" folder.

### Installing

StatMeal can be run on Visual Studio or Github Codespaces.

### Executing program
* Ensure you have the latest version of Python installed
```
sudo apt install python3.10
python --version
```
* Run the server with the line below. By default, it will be locally hosted on port 5000.
```
python code/server.py
```
* To kill the port, run the line below. 
```
npx kill-port 5000
```

### Usage

When you first open StatMeal, the home page offers you two different upload choices: one for graphs and one for predictive models.

![statmeal_display1](https://github.com/JKot2020/StatMeal/assets/112009694/ebda6e25-683d-44c4-a25e-d65895aeb340)

You can upload any .csv or .xls file on your PC, but the repo offers a few example files for you to use.
Afterwards, the program will display the first 5 rows of the spreadsheet and the column names as selectable buttons.

![statmeal_display2](https://github.com/JKot2020/StatMeal/assets/112009694/a342f0b6-21af-40d3-8ceb-6a866816013a)

You can click the buttons to select the graph type and the associated column names as variables. When you do, they appear in the text areas below. You can only select one graph type at a time.
When you are satisfied with your choices, you can select the "Make Graph" button to generate your custom graph.

![statmeal_display3](https://github.com/JKot2020/StatMeal/assets/112009694/467931bf-abdf-4e33-8800-403e314c5e03)

Below is an example of a pie chart made from the data in the Balaji Fast Food data set.

![output1](https://github.com/JKot2020/StatMeal/assets/112009694/d9a43e7e-2b8f-4611-93d6-3b47c1caefe2)

StatMeal offers support for distribution plots, box plots, histograms, scatter plots, and pie charts.

In addition, you can also generate predictive models. The feature is still in beta, so it is not as polished as the graph making. The predictive model maker uses similar functionalities to the graph maker. However, for now, you should only use it if you have an understanding of statistical modelling and regression analysis.

Jason Kotowski
[JKot2020]
