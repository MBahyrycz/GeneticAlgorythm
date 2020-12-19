from src.GeneticAlgorythm import *
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Plotter:

    def DisplayGoalFunctionOfIteration(self, qualityList, method):
        
        iterationCount = list(range(len(qualityList)))
        root = tk.Tk()
        figure = plt.Figure(figsize=(5,4), dpi=100)
        ax3 = figure.add_subplot(111)
        ax3.scatter(iterationCount, qualityList, color = 'g')
        scatter = FigureCanvasTkAgg(figure, root) 
        scatter.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
        ax3.legend(['Wartość funkcji celu']) 
        ax3.set_xlabel('Numer iteracji')
        ax3.set_title('Wykres dla ' +  method)
        root.mainloop()
        
    def TimePlot(self,solvingTimes,values,valueName,methodName):
        root = tk.Tk()
        figure = plt.Figure(figsize=(5,4), dpi=100)
        ax3 = figure.add_subplot(111)
        ax3.scatter(values, solvingTimes, color = 'y')
        scatter = FigureCanvasTkAgg(figure, root) 
        scatter.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
        #ax3.legend(['Czas obliczeń dla '+valueName]) 
        ax3.set_xlabel(valueName)
        ax3.set_ylabel('Czas obliczeń')
        ax3.set_title('Czas obliczeń dla ' +  methodName)
        root.mainloop()
        
    def GoalFunctionOfValues(self,goalFunctions,values,valueName,methodName):
        root = tk.Tk()
        figure = plt.Figure(figsize=(5,4), dpi=100)
        ax3 = figure.add_subplot(111)
        ax3.scatter(values, goalFunctions, color = 'b')
        scatter = FigureCanvasTkAgg(figure, root) 
        scatter.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
        #ax3.legend(['Czas obliczeń dla '+valueName]) 
        ax3.set_xlabel(valueName)
        ax3.set_ylabel('Funkcja celu')
        ax3.set_title('Funkcja celu dla ' +  methodName)
        root.mainloop()