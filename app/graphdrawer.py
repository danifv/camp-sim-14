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
    def plotter(func, xMin, xMax, a, m, iterations):
        figure = Figure()
        axes = figure.add_subplot(111)

        x = [0]
        for i in range(1, int(iterations)+1):
            x.append(i)
        y = func(x, a, m)
        axes.plot(x, y)
        axes.set_xlim(float(xMin), float(xMax))
        axes.set_ybound(float(y[0]), float(y[-1]))

        #for debug
        print('minimum y value: ' + str(y[0]))
        print('maximum y value: ' + str(y[-1]))

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