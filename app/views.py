'''
Created on Jul 27, 2014

@author: daniel
'''
from flask import render_template, request
from app import app
from app import graphdrawer
from app import rpssim
from app import populationsim
from app import rpssimform
from app import popsimform

@app.route('/')
@app.route('/index')
def index():
    #Should be changed to DB store
    links = [
             {
              'name': 'Populacio szimulalas',
              'url': '/populationsim'
              },
             {
              'name': 'Ko-papir-ollo',
              'url': '/rpssim'
              }                        
             ]    
    return render_template("index.html",
        title = 'Simulation list',
        links = links)

@app.route('/populationsim', methods = ['GET', 'POST'])
def populationSim():
    form = popsimform.PopSimForm()
    return render_template("populationsim.html",
        title = 'Vadaszat',
        form = form)
    
@app.route('/rpssim', methods = ['GET', 'POST'])
def rpsSim():
    form = rpssimform.RpsSimForm()
    return render_template("rpssim.html",
        title = 'Ko-papir-ollo',
        form = form)
    
@app.route('/rpssimchart')
def rpsSimChart():
    sameChance = request.args.get('same')
    strongerChance = request.args.get('stronger')
        
    rpsSim = rpssim.RpsSim(sameChance, strongerChance)    
    simResults = rpsSim.simulate()
    
    return graphdrawer.GraphDrawer.plotter(0, 1000, simResults)

    
@app.route('/populationsimchart')
def populationSimChart():
    huntStart = request.args.get('huntStart')
    numberOfHunters = request.args.get('numberOfHunters')
    huntRabbits = request.args.get('huntRabbits')
    huntFoxes = request.args.get('huntFoxes')
    xMin = 0
    xMax = 300
    
    populationSim = populationsim.PopulationSim(numberOfHunters, huntRabbits, huntFoxes, huntStart, 300)
    simResults = populationSim.simulate()
    
    return graphdrawer.GraphDrawer.plotter(xMin, xMax, simResults)