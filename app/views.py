'''
Created on Jul 27, 2014

@author: daniel
'''
from flask import render_template, request
from app import app
from app import testsimform
from app import popsimform
from app import graphdrawer
from app.populationsim import PopulationSim

@app.route('/')
@app.route('/index')
def index():
    #Should be changed to DB store
    links = [
             {
              'name': 'Populacio szimulalas',
              'url': '/populationsim'
              }            
             ]    
    return render_template("index.html",
        title = 'Simulation list',
        links = links)



@app.route('/testsim', methods = ['GET', 'POST'])
def testsim():
    form = testsimform.TestSimForm()
    return render_template("testsim.html",
        title = 'Test simulation',
        form = form)
    
@app.route('/populationsim', methods = ['GET', 'POST'])
def populationSim():
    form = popsimform.PopSimForm()
    return render_template("populationsim.html",
        title = 'Vadaszat',
        form = form)
    
@app.route('/populationsimchart')
def populationSimChart():
    huntStart = request.args.get('huntStart')
    numberOfHunters = request.args.get('numberOfHunters')
    huntRabbits = request.args.get('huntRabbits')
    huntFoxes = request.args.get('huntFoxes')
    xMin = 0
    xMax = 300
    
    populationSim = PopulationSim(huntStart, numberOfHunters, huntRabbits, huntFoxes, 300)
    simResults = populationSim.simulate()
    
    return graphdrawer.GraphDrawer.plotter(xMin, xMax, simResults)
    
    
    
    
    print populationSim.simulate()

# @app.route('/linfigure')
# def linfigure():
#     a = request.args.get('aField')
#     m = request.args.get('mField')
#     xMin = request.args.get('xMinField')
#     xMax = request.args.get('xMaxField')
#     iterations = request.args.get('iterations')
#     if xMin is None:
#         xMin = 0
#     if xMax is None:
#         xMax = iterations
#     return graphdrawer.GraphDrawer.plotter(graphdrawer.GraphDrawer.linear, xMin, xMax, a, m, iterations)
        