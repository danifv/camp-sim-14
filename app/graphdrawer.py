'''
Created on Jul 27, 2014

@author: daniel
'''
from flask import make_response

from cStringIO import StringIO

from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure

import unicodedata
from werkzeug.debug.console import Console

class GraphDrawer(object):
    
    @staticmethod
    def plotter(func, x, *args):
        figure = Figure()
        axis = figure.add_subplot(111)
        y = func(x, *args)
        axis.plot(x, y)
        
        canvas = FigureCanvasAgg(figure)
        output = StringIO()
        canvas.print_png(output)
        response = make_response(output.getvalue())
        response.mimetype = 'image/png'
        return response

    
    @staticmethod
    def linear(x, a, m):
        y = []
        print a
        print m
        for val in x:
            y.append(float(a) + float(m)*float(val))
        return y
        
        
    