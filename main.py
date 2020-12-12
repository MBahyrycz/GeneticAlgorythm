from src.GeneticAlgorythm import *

if __name__ == "__main__":
    #popular = [1.0, 2.0, 2.14, 3.6, 11.23, 23.51, 17.2, 12.3, 19.2, 7.7]
    popular=[3,11,15,23]
    popular.sort()
    alg = GeneticAlgorythm(20, 24, 4, popular,bannedAreas=[(1,4),(15,19)],iterationCount=10000)
    alg.Solve()

    alg.ShowAlfa()

