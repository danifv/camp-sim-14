'''
Created on Jul 27, 2014

@author: daniel
'''

import numpy
from matplotlib import pyplot
from cStringIO import StringIO

class GraphDrawer(object):
    
    @staticmethod
    def plotter(func, x, *args):
        
        y = func(x, *args)
        pyplot.plot(x, y)
        f = StringIO()
        pyplot.savefig(f, format='png')
        return f
    
    @staticmethod
    def linear(x, a, m):
        y = []
        for val in x:
            y.append(a + m*val)
        return y
        
        
    