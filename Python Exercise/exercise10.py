#function to plot f(x) = sin^2(x-2)e^-(x^2)
import numpy as np
import matplotlib.pylab as py

x = np.linspace(0,2)    #creates an interval
y1 = np.sin(x-2)**2     #for sin^2(x-2)
y2 = np.exp(-(x**2))    #for e^-(x^2)
y = y1*y2               #combines the function
py.plot(x,y,'k--')      #plots the function, 'k--' is the line with color - black and style - double dash
py.xlabel('INTERVAL')   #for naming x-axis
py.ylabel('FUNCTION - f(x)')      #for naming y-axis
py.title('PLOTTING A FUNCTION USING \'matplotlib\'')    #for naming the title of the graph
py.show()               #to show the graph/plot
