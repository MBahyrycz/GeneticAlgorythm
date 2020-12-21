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

    def Plot(self, cols=3, size=1):
        rows = 1 if len(self.m_tplList)//cols < 1 else len(self.m_tplList)//cols
        plt.figure(figsize=(cols*3, rows*3))
        for i, tpl in enumerate(self.m_tplList):
            plt.subplot(int(str(rows)+str(cols)+str(i+1)))
            plt.plot(tpl[0], tpl[1], 'ro', markersize = size)
            plt.title(tpl[2])
            plt.xlabel(str(tpl[3]))
            plt.ylabel(str(tpl[4]))
        plt.tight_layout()
        plt.show()

    def PlotMultiple(self, title, *args, size=1):

        plt.figure(figsize=(3, 3))
        plt.subplot(111)
        if len(args) == 2:
            plt.plot(self.m_tplList[args[0]][0], self.m_tplList[args[0]][1], 'ro', self.m_tplList[args[1]][1], 'bo', markersize = size) 
            plt.title(title)
            plt.xlabel(str(self.m_tplList[args[0]][3]))
        elif len(args) == 3:
            plt.plot(self.m_tplList[args[0]][0], self.m_tplList[args[0]][1], 'ro', self.m_tplList[args[1]][1], 'bo', self.m_tplList[args[2]][1], 'go', markersize = size) 
            plt.title(title)
            plt.xlabel(str(self.m_tplList[args[0]][3]))
        elif len(args) == 4:
            plt.plot(self.m_tplList[args[0]][0], self.m_tplList[args[0]][1], 'ro', self.m_tplList[args[1]][1], 'bo', 
            self.m_tplList[args[2]][1], 'go', self.m_tplList[args[3]][1], 'yo', markersize = size) 
            plt.title(title)
            plt.xlabel(str(self.m_tplList[args[0]][3]))
        plt.show()

    def AddPlots(self, *args):
        for dataList in args:
            for data in dataList:
                self.m_tplList.append(data)

    def GetTuples(self):
        return self.m_tplList




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

