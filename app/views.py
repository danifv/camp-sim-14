'''
Created on Jul 27, 2014

@author: daniel
'''
from flask import render_template, send_file, request
from app import app
from app import testsimform
from app import graphdrawer

@app.route('/')
@app.route('/index')
def index():
    #Should be changed to DB store
    links = [
             {              
              'name': 'Test sim',
              'url': '/testsim'
              },
             {
              'name': 'sim2',
              'url': '/sim2'
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

@app.route('/linfigure')
def linfigure():
    a = request.args.get('aField')
    m = request.args.get('mField')
    xMin = request.args.get('xMinField')
    xMax = request.args.get('xMaxField')
    iterations = request.args.get('iterations')
    if xMin is None:
        xMin = 0
    if xMax is None:
        xMax = iterations
    return graphdrawer.GraphDrawer.plotter(graphdrawer.GraphDrawer.linear, xMin, xMax, a, m, iterations)
        