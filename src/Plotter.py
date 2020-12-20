# from src.GeneticAlgorythm import *
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Plotter:

    def __init__(self):
        self.m_tplList = []
    
    def AddValues(self, x, y, title):
        self.m_tplList.append((x, y, title))

    def Clear(self):
        self.m_tplList = []

    def Plot(self, cols=3):
        rows = 1 if len(self.m_tplList)//cols < 1 else len(self.m_tplList)//cols
        plt.figure(figsize=(cols*3, rows*3))
        i=1
        for tpl in self.m_tplList:
            plt.subplot(int(str(rows)+str(cols)+str(i)))
            plt.plot(tpl[0], tpl[1], 'ro')
            plt.title(tpl[2])
            i +=1
        plt.tight_layout()
        plt.show()

    def PlotMultiple(self, *args):
        pass


# pltt = Plotter()
# pltt.AddGraph([1,2,3,4],[1,1,1,1])
# pltt.AddGraph([6,5,4,3,2],[3,3,3,3,3])
# pltt.PlotGraphs()
