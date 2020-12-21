from src.GeneticAlgorythm import *
from src.Plotter import *
import time
import numpy as np

if __name__ == "__main__":
    methods=["RankSelection", "RankSelectionDependentOnIteration", "RouletteSelection", "TournamentSelection"]
    iterCount = 1000
    plt = Plotter()
    meanPlt = Plotter()

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
        alfaMaleData,bestIndividuals, mean=alg.Solve(method)

        
        plt.AddValues(range(iterCount), alfaMaleData, method, "Numer iteracji", "Wartość funkcji celu")
        meanPlt.AddValues(range(iterCount), mean, method, "Numer iteracji", "Średnia wartość funkcji celu")
        
        alg.ShowAlfa()
        print("Czas obliczeń : ",time.time()-start)
        
    plt.AddPlots(meanPlt.GetTuples())
    plt.Plot(4)

        # solveTime=list(halfPop[:])
        # goalFunctions=list(halfPop[:])
        
        # for index,hp in enumerate(halfPop):
        #     solveTime[index]=0
        #     goalFunctions[index]=0
        #     for i in range(repeats):
        #         alg = GeneticAlgorythm(hp, 24, 4, popular,bannedAreas=[(1,4),(17,20)],iterationCount=100)
        #         start=time.time()
        #         alg.Solve(method)
        #         solveTime[index]+=time.time()-start
        #         goalFunctions[index]+=alg.m_AlfaMale.m_Quality
        #     solveTime[index]/=repeats
        #     goalFunctions[index]/=repeats
            
        # plt.TimePlot(solveTime,2*np.array(halfPop),'Populacja',method)
        # plt.GoalFunctionOfValues(goalFunctions,2*np.array(halfPop),'Populacja',method)

        
    iterCount=100
    repeats=10
    popular = [1.0, 2.0, 2.14, 3.6, 11.23, 23.51, 17.2, 12.3, 19.2, 7.7]
    popular.sort()
    
    # #dla rurznych mutate 
    pltMutateTime=Plotter()
    pltMutateGF=Plotter()
    mutate=(np.linspace(0.0,1.0,num=20)).tolist()
    for method in methods:
        print()
        print('Metoda : ',method)
        print()
        
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
        
        pltMutateTime.AddValues(mutate,solveTime,method,'Prawdopodobieństwo mutacji','Czas obliczeń')
        pltMutateGF.AddValues(mutate,goalFunctions,method,'Prawdopodobieństwo mutacji','Funkcja celu')
    pltMutateTime.AddPlots(pltMutateGF.GetTuples())
    pltMutateTime.Plot(4)
    # pltMutateTime.Plot(2)
    # pltMutateGF.Plot(2)
    
    # dla rurznych populationCount
    halfPop=range(1,30)
    pltPopTime=Plotter()
    pltPopGF=Plotter()
    for method in methods:
        print()
        print('Metoda : ',method)
        print()
        
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
         
        pltPopTime.AddValues(2*np.array(halfPop),solveTime,method,'Populacja','Czas obliczeń')
        pltPopGF.AddValues(2*np.array(halfPop),goalFunctions,method,'Populacja','Funkcja celu')
    
    pltPopTime.AddPlots(pltPopGF.GetTuples())
    # pltPopTime.Plot(2)
    # pltPopGF.Plot(2)
    pltPopTime.Plot(4)
    
