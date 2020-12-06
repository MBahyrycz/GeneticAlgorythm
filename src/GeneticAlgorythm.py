from src.Individual import *

import random
import math

class GeneticAlgorythm:
    def __init__(self, halfPopulationCount, roadLength, stopsCount, popularPlaces, mutationProbability = 0.05, iterationCount=10000,minStopsDistance=3,maxStopsDistance=7):
        self.m_PopulationCount = 2 * halfPopulationCount
        self.m_RoadLength = roadLength
        self.m_StopsCount = stopsCount
        self.m_PopularPlaces = popularPlaces
        self.m_Population = []
        self.m_IterationCount = iterationCount
        self.m_MutationProbability = mutationProbability
        self.minStopsDistance=minStopsDistance
        self.maxStopsDistance=maxStopsDistance
        self.m_AlfaMale = Individual(self.m_StopsCount, self.m_RoadLength, self.m_MutationProbability,self.minStopsDistance,self.maxStopsDistance)
        self.m_AlfaMale.m_Quality = math.inf

    def ConstructPopulation(self):
        for _ in range(self.m_PopulationCount):
            individual = Individual(self.m_StopsCount, self.m_RoadLength, self.m_MutationProbability,self.minStopsDistance,self.maxStopsDistance)
            individual.CreateIndividual()
            self.m_Population.append(individual)

    def PrintPopulation(self):
        for i in range(self.m_PopulationCount):
            print(self.m_Population[i].m_Chromosome, self.m_Population[i].m_Quality)
        print('\n')

    def Solve(self):
        self.ConstructPopulation()
        endCondition = 0
        while(endCondition<self.m_IterationCount):
            self.CalculateQuality()
            # self.DividePopulation()
            self.RouletteSelection()
            # self.PrintPopulation()
            self.CrossOver()
            self.Mutate()
            # self.PrintPopulation()
            endCondition+= 1

    def CalculateQuality(self):
        for i in range(self.m_PopulationCount):
            self.m_Population[i].m_Quality = self.GoalFunction(self.m_Population[i].m_Chromosome)

    def GoalFunction(self, chromosome):
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
            self.m_Population[i] = Individual(self.m_StopsCount, self.m_RoadLength, self.m_MutationProbability,self.minStopsDistance,self.maxStopsDistance)
            self.m_Population[i].CreateIndividual()
            self.m_Population[i].m_Quality = self.GoalFunction(self.m_Population[i].m_Chromosome)

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
                self.m_Population[i] = Individual(self.m_StopsCount, self.m_RoadLength, self.m_MutationProbability,self.minStopsDistance,self.maxStopsDistance)
                self.m_Population[i].CreateIndividual()
                self.m_Population[i].m_Quality = self.GoalFunction(self.m_Population[i].m_Chromosome)

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
