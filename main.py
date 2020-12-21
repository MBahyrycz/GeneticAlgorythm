from src.GeneticAlgorythm import *
from src.Plotter import *
import time
import numpy as np

if __name__ == "__main__":
    methods=["RankSelection", "RankSelectionDependentOnIteration", "RouletteSelection", "TournamentSelection"]
    iterCount = 1000
    plt = Plotter()
    meanPlt = Plotter()
    crossOverPlt = Plotter()
    mutatePlt = Plotter()
    bestIndividualsPlt = Plotter()

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
        alfaMaleData, bestIndividuals, mean, crossOverTime, mutateTime = alg.Solve(method)

        
        plt.AddValues(range(iterCount), alfaMaleData, method, "Numer iteracji", "Wartość funkcji celu")
        meanPlt.AddValues(range(iterCount), mean, method, "Numer iteracji", "Średnia wartość funkcji celu")
        crossOverPlt.AddValues(range(iterCount), crossOverTime, method, "Numer iteracji", "Czas krzyżowania")
        mutatePlt.AddValues(range(iterCount), mutateTime, method, "Numer iteracji", "Czas mutacji")
        bestIndividualsPlt.AddValues(range(iterCount), bestIndividuals, method, "Numer iteracji", "Wartość funkcji celu")
        
        alg.ShowAlfa()
        print("Czas obliczeń : ",time.time()-start)
        print("Średni czas mutacji : ", sum(mutateTime)/len(mutateTime))
        print("Średni czas krzyżowania : ", sum(crossOverTime)/len(crossOverTime))
        
    plt.AddPlots(meanPlt.GetTuples())
    plt.Plot(4)

    bestIndividualsPlt.Plot(2)

        
    
    
    
    iterCount=100
    repeats=10
    popular = [1.0, 2.0, 2.14, 3.6, 11.23, 23.51, 17.2, 12.3, 19.2, 7.7]
    popular.sort()
    
    # dla rurznych banned
    pltBannedTime=Plotter()
    bannedCount=list(range(2,30))
    for method in methods:
        print()
        print('Metoda : ',method)
        print()
        
        solveTime=bannedCount[:]
        
        for index,ban in enumerate(bannedCount):
            solveTime[index]=0
            banlist=np.linspace(0.0,24.0,num=2*ban)
            bannedList=[]
            for i in range(ban):
                bannedList.append((banlist[2*i],banlist[2*i+1]))
            for i in range(repeats):
                alg = GeneticAlgorythm(20, 24, 4, popular,bannedAreas=bannedList,iterationCount=iterCount)
                start=time.time()
                alg.Solve(method)
                solveTime[index]+=time.time()-start
            solveTime[index]/=repeats
        pltBannedTime.AddValues(bannedCount,solveTime,method,'Liczba miejsc zabronionych','Czas obliczeń')
    pltBannedTime.Plot(2)
    
    # dla rurznych popular
    pltPopTime=Plotter()
    popularCount=list(range(2,25))
    for method in methods:
        print()
        print('Metoda : ',method)
        print()
        
        solveTime=popularCount[:]
        
        for index,popc in enumerate(popularCount):
            solveTime[index]=0
            popularlist=np.logspace(0.0,24.0,num=popc)
            for i in range(repeats):
                alg = GeneticAlgorythm(20, 24, 4, popularlist,bannedAreas=[(1,4),(17,20)],iterationCount=iterCount)
                start=time.time()
                alg.Solve(method)
                solveTime[index]+=time.time()-start
            solveTime[index]/=repeats
        pltPopTime.AddValues(popularCount,solveTime,method,'Liczba miejsc popularnych','Czas obliczeń')
    pltPopTime.Plot(2)
    
    # dla rurznych stopCount 
    pltStopsTime=Plotter()
    pltStopsGF=Plotter()
    stopCounts=list(range(3,30))
    for method in methods:
        print()
        print('Metoda : ',method)
        print()
        
        solveTime=stopCounts[:]
        goalFunctions=stopCounts[:]
        
        for index,stops in enumerate(stopCounts):
            solveTime[index]=0
            goalFunctions[index]=0
            for i in range(repeats):
                alg = GeneticAlgorythm(20, 24, stops, popular,bannedAreas=[(1,4),(17,20)],iterationCount=iterCount,minStopsDistance=5/stops,maxStopsDistance=40/stops)
                start=time.time()
                alg.Solve(method)
                solveTime[index]+=time.time()-start
                goalFunctions[index]+=alg.m_AlfaMale.m_Quality
            solveTime[index]/=repeats
            goalFunctions[index]/=repeats
        #print(goalFunctions)
        pltStopsTime.AddValues(stopCounts,solveTime,method,'Liczba przystanków','Czas obliczeń')
        pltStopsGF.AddValues(stopCounts,goalFunctions,method,'Liczba przystanków','Funkcja celu')
    pltStopsTime.AddPlots(pltStopsGF.GetTuples())
    pltStopsTime.Plot(4)
    
    # dla rurznych mutate 
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
                alg = GeneticAlgorythm(20, 24, 4, popular,bannedAreas=[(1,4),(17,20)],iterationCount=iterCount,mutationProbability=m)
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
                alg = GeneticAlgorythm(hp, 24, 4, popular,bannedAreas=[(1,4),(17,20)],iterationCount=iterCount)
                start=time.time()
                alg.Solve(method)
                solveTime[index]+=time.time()-start
                goalFunctions[index]+=alg.m_AlfaMale.m_Quality
            solveTime[index]/=repeats
            goalFunctions[index]/=repeats
         
        pltPopTime.AddValues(2*np.array(halfPop),solveTime,method,'Populacja','Czas obliczeń')
        pltPopGF.AddValues(2*np.array(halfPop),goalFunctions,method,'Populacja','Funkcja celu')
    
    pltPopTime.AddPlots(pltPopGF.GetTuples())
    pltPopTime.Plot(4)