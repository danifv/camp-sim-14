'''
Created on Jul 27, 2014

@author: daniel
'''
from flask import make_response

from cStringIO import StringIO

from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure

class GraphDrawer(object):
    
    @staticmethod
    def plotter(xMin, xMax, dataSeries):
        figure = Figure()
        axes = figure.add_subplot(111)

        x = range(xMin, xMax)
        plots = []
        
        for serie in dataSeries.values():
            pls, = axes.plot(x, serie)
            plots.append(pls)
            
        figure.legend(plots, dataSeries.keys()) 
        
        axes.set_xlim(float(xMin), float(xMax))
        axes.set_ylim(0, 1000)


        canvas = FigureCanvasAgg(figure)
        output = StringIO()
        canvas.print_png(output)
        response = make_response(output.getvalue())
        response.mimetype = 'image/png'
        return response

    @staticmethod
    def linear(x, a, m):
        y = []
        for val in x:
            y.append(float(a) + float(m)*val)
        return y