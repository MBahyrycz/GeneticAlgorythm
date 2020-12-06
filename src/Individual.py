import random

class Individual:
    def __init__(self, stopsCount, roadLength, mutationProbability):
        self.m_StopsCount = stopsCount
        self.m_RoadLength = roadLength
        self.m_Chromosome = []
        self.m_Quality = 0.0
        self.m_MutationProbability = mutationProbability

    def CreateIndividual(self):
        for _ in range(self.m_StopsCount):
            self.m_Chromosome.append(random.random() * self.m_RoadLength)

        self.m_Chromosome.sort()

    def Mutate(self):
        if random.random() < self.m_MutationProbability:
            self.m_Chromosome[random.randint(0,self.m_StopsCount - 1)] = random.random() * self.m_RoadLength
            self.m_Chromosome.sort()