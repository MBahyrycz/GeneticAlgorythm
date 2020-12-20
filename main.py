from src.GeneticAlgorythm import *
from src.Plotter import *
import time

if __name__ == "__main__":
    methods=["RankSelection", "RankSelectionDependentOnIteration", "RouletteSelection", "TournamentSelection"]
    iterCount = 1000
    plt = Plotter()
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
        print(len(alfaMaleData))

        
        plt.AddValues(range(iterCount), alfaMaleData, method)
        
        # print("zbiernosici funkcji celu")
        # # print(alfaMaleData)#z tego ma byci wykres
        # print("najlepsze osobniki")
        # print(bestIndividuals)#z tego tesz
        
        alg.ShowAlfa()
        print("Czas obliczeń : ",time.time()-start)
        
        
        #dla rurznych mutate
        mutate=[0,0.01,0.1,0.25,0.5,1]#morzna zrobici wykres
        
        popular = [1.0, 2.0, 2.14, 3.6, 11.23, 23.51, 17.2, 12.3, 19.2, 7.7]
        popular.sort()
        
        # for m in mutate:
        #     alg = GeneticAlgorythm(20, 24, 4, popular,bannedAreas=[(1,4),(17,20)],iterationCount=1000,mutationProbability=m)
        #     start=time.time()
        #     alfaMaleData=alg.Solve(method)
        #     print("Prawdopodobienistwo mutacji : ",m)
        #     alg.ShowAlfa()
        #     print("Czas obliczeń : ",time.time()-start)
            
        # #dla rurznych populationCount
        # halfPop=[1,2,5,10,20]#morzna zrobici wykres
        
        # popular = [1.0, 2.0, 2.14, 3.6, 11.23, 23.51, 17.2, 12.3, 19.2, 7.7]
        # popular.sort()
        
        # for hp in halfPop:
        #     alg = GeneticAlgorythm(hp, 24, 4, popular,bannedAreas=[(1,4),(17,20)],iterationCount=1000)
        #     start=time.time()
        #     alfaMaleData=alg.Solve(method)
        #     print("Populacja : ",2*hp)
        #     alg.ShowAlfa()
        #     print("Czas obliczeń : ",time.time()-start)
    
    plt.Plot(1)
    