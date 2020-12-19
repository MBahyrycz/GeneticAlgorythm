from src.GeneticAlgorythm import *
from src.Plotter import *
import time
import numpy as np

if __name__ == "__main__":
    methods=["RankSelection", "RankSelectionDependentOnIteration", "RouletteSelection", "TournamentSelection"]
    iterCount = 1000
    for method in methods:
        print()
        print('Metoda : ',method)
        print()
        #zbierznosici funkcji celu i najlepsze osobniki
        
        #popular = [1.0, 2.0, 2.14, 3.6, 11.23, 23.51, 17.2, 12.3, 19.2, 7.7]
        popular=[3,11,15,23]
        popular.sort()
        alg = GeneticAlgorythm(20, 24, 4, popular,bannedAreas=[(1,4),(15,19)],iterationCount=iterCount)
        start=time.time()
        alfaMaleData,bestIndividuals=alg.Solve(method)
        #print(len(alfaMaleData))

        plt = Plotter()
        plt.DisplayGoalFunctionOfIteration(alfaMaleData, method)
        
        # print("zbiernosici funkcji celu")
        # # print(alfaMaleData)#z tego ma byci wykres
        # print("najlepsze osobniki")
        # print(bestIndividuals)#z tego tesz
        
        alg.ShowAlfa()
        print("Czas obliczeń : ",time.time()-start)
        
        repeats=10
        
        #dla rurznych mutate
        mutate=(np.linspace(0.0,1.0,num=20)).tolist()
        
        popular = [1.0, 2.0, 2.14, 3.6, 11.23, 23.51, 17.2, 12.3, 19.2, 7.7]
        popular.sort()
        
        solveTime=mutate[:]
        goalFunctions=mutate[:]
        
        for index,m in enumerate(mutate):
            solveTime[index]=0
            goalFunctions[index]=0
            for i in range(repeats):
                alg = GeneticAlgorythm(20, 24, 4, popular,bannedAreas=[(1,4),(17,20)],iterationCount=100,mutationProbability=m)
                start=time.time()
                alg.Solve(method)
                solveTime[index]+=time.time()-start
                goalFunctions[index]+=alg.m_AlfaMale.m_Quality
            solveTime[index]/=repeats
            goalFunctions[index]/=repeats
            
        plt.TimePlot(solveTime,mutate,'Prawdopodobieństwo mutacji',method)
        plt.GoalFunctionOfValues(goalFunctions,mutate,'Prawdopodobieństwo mutacji',method)
        
        #dla rurznych populationCount
        halfPop=range(1,30)
        
        popular = [1.0, 2.0, 2.14, 3.6, 11.23, 23.51, 17.2, 12.3, 19.2, 7.7]
        popular.sort()
        
        solveTime=list(halfPop[:])
        goalFunctions=list(halfPop[:])
        
        for index,hp in enumerate(halfPop):
            solveTime[index]=0
            goalFunctions[index]=0
            for i in range(repeats):
                alg = GeneticAlgorythm(hp, 24, 4, popular,bannedAreas=[(1,4),(17,20)],iterationCount=100)
                start=time.time()
                alg.Solve(method)
                solveTime[index]+=time.time()-start
                goalFunctions[index]+=alg.m_AlfaMale.m_Quality
            solveTime[index]/=repeats
            goalFunctions[index]/=repeats
            
        plt.TimePlot(solveTime,2*np.array(halfPop),'Populacja',method)
        plt.GoalFunctionOfValues(goalFunctions,2*np.array(halfPop),'Populacja',method)
        
        
            
        
    