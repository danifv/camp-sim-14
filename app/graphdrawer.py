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
    def plotter(func, x, *args):
        figure = Figure()
        axes = figure.add_subplot(111)
        

        y = func(x, *args)
        axes.plot(x, y)
        print x[0]
        print x[-1]
        axes.set_ylim(ymin=x[0], ymax=x[-1])        
        axes.set_xlim(xmin=x[0], xmax=x[-1])
        
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
    