from src.Individual import *
import random
import time

class GeneticAlgorythm:
    def __init__(self, halfPopulationCount, roadLength, stopsCount, popularPlaces, mutationProbability = 0.05, iterationCount=10000,minStopsDistance=3,maxStopsDistance=7,bannedAreas=[]):
        self.m_PopulationCount = 2 * halfPopulationCount
        self.m_RoadLength = roadLength
        self.m_StopsCount = stopsCount
        self.m_PopularPlaces = popularPlaces
        self.m_Population = []
        self.m_IterationCount = iterationCount
        self.m_MutationProbability = mutationProbability
        self.m_MinStopsDistance=minStopsDistance
        self.m_MaxStopsDistance=maxStopsDistance
        self.m_bannedAreas=bannedAreas
        self.m_AlfaMale = Individual(self.m_StopsCount, self.m_RoadLength, self.m_MutationProbability,self.m_MinStopsDistance,self.m_MaxStopsDistance,self.m_bannedAreas)
        self.m_AlfaMale.m_Quality = math.inf

    def ConstructPopulation(self):
        for _ in range(self.m_PopulationCount):
            individual = Individual(self.m_StopsCount, self.m_RoadLength, self.m_MutationProbability,self.m_MinStopsDistance,self.m_MaxStopsDistance,self.m_bannedAreas)
            individual.CreateIndividual()
            self.m_Population.append(individual)

    def PrintPopulation(self):
        for i in range(self.m_PopulationCount):
            print(self.m_Population[i].m_Chromosome, self.m_Population[i].m_Quality)
        print('\n')

    def Solve(self,method='rksi'):
        self.ConstructPopulation()
        endCondition = 0
        alfaMaleData=[]
        bestIndividuals=[]
        mean=[]
        crossOverTime=[]
        mutateTime=[]
        crossOverChanges=[]
        mutateChanges=[]
        while(endCondition<self.m_IterationCount):
            self.CalculateQuality()
            if method=="RankSelection":
                self.RankSelection()
            if method=="RankSelectionDependentOnIteration":
                self.RankSelectionDependentOnIteration(endCondition)
            if method=="RouletteSelection":
                self.RouletteSelection()
            if method=="TournamentSelection":
                self.TournamentSelection()
            # self.PrintPopulation()
            bestIndividuals.append(self.m_Population[0].m_Quality)
            startCrossOver = time.time()
            self.CrossOver()
            crossOverTime.append(time.time() - startCrossOver)
            self.CalculateQuality()
            maxGFc=min(self.m_Population,key=lambda x:x.m_Quality).m_Quality
            crossOverChanges.append(maxGFc-bestIndividuals[-1])
            startMutate = time.time()
            self.Mutate()
            mutateTime.append(time.time()-startMutate)
            self.CalculateQuality()
            maxGFm=min(self.m_Population,key=lambda x:x.m_Quality).m_Quality
            mutateChanges.append(maxGFm-bestIndividuals[-1]-crossOverChanges[-1])
            # self.PrintPopulation()
            alfaMaleData.append(self.m_AlfaMale.m_Quality)
            mean.append(self.GetGoalFunctionMean())
            endCondition+= 1
        return alfaMaleData,bestIndividuals, mean, crossOverTime, mutateTime,crossOverChanges,mutateChanges

    def CalculateQuality(self):
        for i in range(self.m_PopulationCount):
            if self.m_Population[i]!=math.inf:
                self.m_Population[i].m_Quality = self.GoalFunction(self.m_Population[i])

    def GoalFunction(self, individual):
        if individual.m_Quality==math.inf:
            return math.inf
        chromosome=individual.m_Chromosome
        sum = 0
        index = 0
        for j in range(len(self.m_PopularPlaces)):
            while index<self.m_StopsCount-1 and self.m_PopularPlaces[j]>(chromosome[index]+chromosome[index+1])/2:
                index+=1
            sum+=abs(chromosome[index]-self.m_PopularPlaces[j])

        return sum

    def RankSelection(self):
        x = lambda a: a.m_Quality
        self.m_Population.sort(key=x)

        for i in range(int(self.m_PopulationCount/2), self.m_PopulationCount):
            self.m_Population[i] = Individual(self.m_StopsCount, self.m_RoadLength, self.m_MutationProbability,self.m_MinStopsDistance,self.m_MaxStopsDistance,self.m_bannedAreas)
            self.m_Population[i].CreateIndividual()
            self.m_Population[i].m_Quality = self.GoalFunction(self.m_Population[i])

        self.m_Population.sort(key=x)

        if self.m_Population[0].m_Quality < self.m_AlfaMale.m_Quality:
            self.m_AlfaMale.m_Chromosome = self.m_Population[0].m_Chromosome[:]
            self.m_AlfaMale.m_Quality= self.m_Population[0].m_Quality


    def RankSelectionDependentOnIteration(self, currentIteration):
        x = lambda a: a.m_Quality
        self.m_Population.sort(key=x)

        for i in range(int(currentIteration/self.m_IterationCount * self.m_PopulationCount), self.m_PopulationCount):
            self.m_Population[i] = Individual(self.m_StopsCount, self.m_RoadLength, self.m_MutationProbability,self.m_MinStopsDistance,self.m_MaxStopsDistance,self.m_bannedAreas)
            self.m_Population[i].CreateIndividual()
            self.m_Population[i].m_Quality = self.GoalFunction(self.m_Population[i])

        self.m_Population.sort(key=x)

        if self.m_Population[0].m_Quality < self.m_AlfaMale.m_Quality:
            self.m_AlfaMale.m_Chromosome = self.m_Population[0].m_Chromosome[:]
            self.m_AlfaMale.m_Quality= self.m_Population[0].m_Quality

    def RouletteSelection(self):
        goalFunctionSum = 0
        for i in range(0, self.m_PopulationCount):
            goalFunctionSum += self.m_Population[i].m_Quality
        
        for i in range(0, self.m_PopulationCount):
            if random.random() < self.m_Population[i].m_Quality/goalFunctionSum:
                self.m_Population[i] = Individual(self.m_StopsCount, self.m_RoadLength, self.m_MutationProbability,self.m_MinStopsDistance,self.m_MaxStopsDistance,self.m_bannedAreas)
                self.m_Population[i].CreateIndividual()
                self.m_Population[i].m_Quality = self.GoalFunction(self.m_Population[i])

        x = lambda a: a.m_Quality
        self.m_Population.sort(key=x)

        if self.m_Population[0].m_Quality < self.m_AlfaMale.m_Quality:
            self.m_AlfaMale.m_Chromosome = self.m_Population[0].m_Chromosome[:]
            self.m_AlfaMale.m_Quality= self.m_Population[0].m_Quality

    def TournamentSelection(self):
        usedStops = []
        newPopulation = []
        while len(usedStops) < self.m_PopulationCount:
            firstChallanger = random.randint(0,self.m_PopulationCount - 1)
            secondChallanger = random.randint(0,self.m_PopulationCount - 1)
            if(firstChallanger not in usedStops and secondChallanger not in usedStops):
                usedStops.append(firstChallanger)
                usedStops.append(secondChallanger)
                if self.m_Population[firstChallanger].m_Quality >= self.m_Population[secondChallanger].m_Quality:
                    newPopulation.append(self.m_Population[firstChallanger])
                else: 
                    newPopulation.append(self.m_Population[secondChallanger])
        
        self.m_Population = newPopulation

        for i in range(int(self.m_PopulationCount/2), self.m_PopulationCount):
            self.m_Population.append(Individual(self.m_StopsCount, self.m_RoadLength, self.m_MutationProbability,self.m_MinStopsDistance,self.m_MaxStopsDistance,self.m_bannedAreas))
            self.m_Population[i].CreateIndividual()
            self.m_Population[i].m_Quality = self.GoalFunction(self.m_Population[i])

        x = lambda a: a.m_Quality
        self.m_Population.sort(key=x)

        if self.m_Population[0].m_Quality < self.m_AlfaMale.m_Quality:
            self.m_AlfaMale.m_Chromosome = self.m_Population[0].m_Chromosome[:]
            self.m_AlfaMale.m_Quality= self.m_Population[0].m_Quality


    def ShowAlfa(self):
        print(self.m_AlfaMale.m_Chromosome, self.m_AlfaMale.m_Quality)

    def CrossOver(self):
        for i in range(0, self.m_PopulationCount, 2):
            crossover_index = random.randint(0,self.m_StopsCount - 2)
            self.m_Population[i].m_Chromosome[crossover_index:-1], self.m_Population[i+1].m_Chromosome[crossover_index:-1] = self.m_Population[i+1].m_Chromosome[crossover_index:-1], self.m_Population[i].m_Chromosome[crossover_index:-1]
            self.m_Population[i].Repair()
            self.m_Population[i+1].Repair()

    def Mutate(self):
        for i in range(self.m_PopulationCount):
            self.m_Population[i].Mutate()

    def GetGoalFunctionMean(self):
        gfList = []
        for individual in self.m_Population:
            if individual.m_Quality != math.inf:
                gfList.append(individual.m_Quality)
        return sum(gfList)/len(gfList) if len(gfList) != 0 else math.inf
