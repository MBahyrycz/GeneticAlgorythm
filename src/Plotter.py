# from src.GeneticAlgorythm import *
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Plotter:

    def __init__(self):
        self.m_tplList = []
    
    def AddValues(self, x, y, title, xlabel="x", ylabel="y"):
        self.m_tplList.append((x, y, title, xlabel, ylabel))

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
            plt.xlabel(str(tpl[3]))
            plt.ylabel(str(tpl[4]))
        plt.tight_layout()
        plt.show()

    def PlotMultiple(self, *args):
        pass


# pltt = Plotter()
# pltt.AddGraph([1,2,3,4],[1,1,1,1])
# pltt.AddGraph([6,5,4,3,2],[3,3,3,3,3])
# pltt.PlotGraphs()

    # def DisplayGoalFunctionOfIteration(self, qualityList, method):
        
    #     iterationCount = list(range(len(qualityList)))
    #     root = tk.Tk()
    #     figure = plt.Figure(figsize=(5,4), dpi=100)
    #     ax3 = figure.add_subplot(111)
    #     ax3.scatter(iterationCount, qualityList, color = 'g')
    #     scatter = FigureCanvasTkAgg(figure, root) 
    #     scatter.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    #     ax3.legend(['Wartość funkcji celu']) 
    #     ax3.set_xlabel('Numer iteracji')
    #     ax3.set_title('Wykres dla ' +  method)
    #     root.mainloop()
        
    # def TimePlot(self,solvingTimes,values,valueName,methodName):
    #     root = tk.Tk()
    #     figure = plt.Figure(figsize=(5,4), dpi=100)
    #     ax3 = figure.add_subplot(111)
    #     ax3.scatter(values, solvingTimes, color = 'y')
    #     scatter = FigureCanvasTkAgg(figure, root) 
    #     scatter.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    #     #ax3.legend(['Czas obliczeń dla '+valueName]) 
    #     ax3.set_xlabel(valueName)
    #     ax3.set_ylabel('Czas obliczeń')
    #     ax3.set_title('Czas obliczeń dla ' +  methodName)
    #     root.mainloop()
        
    # def GoalFunctionOfValues(self,goalFunctions,values,valueName,methodName):
    #     root = tk.Tk()
    #     figure = plt.Figure(figsize=(5,4), dpi=100)
    #     ax3 = figure.add_subplot(111)
    #     ax3.scatter(values, goalFunctions, color = 'b')
    #     scatter = FigureCanvasTkAgg(figure, root) 
    #     scatter.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    #     #ax3.legend(['Czas obliczeń dla '+valueName]) 
    #     ax3.set_xlabel(valueName)
    #     ax3.set_ylabel('Funkcja celu')
    #     ax3.set_title('Funkcja celu dla ' +  methodName)
    #     root.mainloop()

