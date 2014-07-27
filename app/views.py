'''
Created on Jul 27, 2014

@author: daniel
'''
from flask import render_template
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
    if form.validate_on_submit():
        f = graphdrawer.GraphDrawer.plotter(graphdrawer.GraphDrawer.linear, [0,1,2,3,4], form.aField, form.mField)
        f.seek(0)
        data = f.read()
        return data
    return render_template("testsim.html",
        title = 'Test simulation',
        form = form)