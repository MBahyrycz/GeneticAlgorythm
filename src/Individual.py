import random

class Individual:
    def __init__(self, stopsCount, roadLength, mutationProbability,minStopsDistance,maxStopsDistance):
        self.m_StopsCount = stopsCount
        self.m_RoadLength = roadLength
        self.m_Chromosome = []
        self.m_Quality = 0.0
        self.m_minStopsDistance=minStopsDistance
        self.m_maxStopsDistance=maxStopsDistance
        self.m_MutationProbability = mutationProbability

    def CreateIndividual(self):
        for i in range(self.m_StopsCount):
            leftBorder=0
            rightBorder=self.m_RoadLength
            if i==0:
                leftBorder=self.m_minStopsDistance
                rightBorder=self.m_maxStopsDistance
            else:
                leftBorder=self.m_minStopsDistance+self.m_Chromosome[i-1]
                rightBorder=self.m_maxStopsDistance+self.m_Chromosome[i-1]
            leftFromEnd = self.m_RoadLength-(self.m_StopsCount-i)*self.m_maxStopsDistance
            rightFromEnd = self.m_RoadLength-(self.m_StopsCount-i)*self.m_minStopsDistance
            leftBorder=max(leftFromEnd,leftBorder)
            rightBorder=min(rightFromEnd,rightBorder)
            self.m_Chromosome.append(random.random()*(rightBorder-leftBorder)+leftBorder)
            
    
    def StopsBorders(self,index):
        leftBorder=0
        rightBorder=self.m_RoadLength
        if index==0:
            leftBorder=max(self.m_minStopsDistance,self.m_Chromosome[1]-self.m_maxStopsDistance)
            rightBorder=min(self.m_maxStopsDistance,self.m_Chromosome[1]-self.m_minStopsDistance)
        elif index==self.m_StopsCount-1:
            leftBorder=max(self.m_Chromosome[index-1]+self.m_minStopsDistance,self.m_RoadLength-self.m_maxStopsDistance)
            rightBorder=min(self.m_Chromosome[index-1]+self.m_maxStopsDistance,self.m_RoadLength-self.m_minStopsDistance)
        else:
            leftBorder=max(self.m_Chromosome[index-1]+self.m_minStopsDistance,self.m_Chromosome[index+1]-self.m_maxStopsDistance)
            rightBorder=min(self.m_Chromosome[index-1]+self.m_maxStopsDistance,self.m_Chromosome[index+1]-self.m_minStopsDistance)
        return leftBorder,rightBorder
    
    def Mutate(self):
        if random.random() < self.m_MutationProbability:
            index = random.randint(0,self.m_StopsCount - 1)
            leftBorder,rightBorder=self.StopsBorders(index)
            self.m_Chromosome[0]=random.random()*(rightBorder-leftBorder)+leftBorder
    
    def Repair(self):
        for i in range(self.m_StopsCount):
            leftBorder,rightBorder=self.StopsBorders(i)
            if leftBorder>rightBorder:
                if i==0:
                    leftBorder=self.m_minStopsDistance
                    rightBorder=self.m_maxStopsDistance
                else:
                    leftBorder=self.m_minStopsDistance+self.m_Chromosome[i-1]
                    rightBorder=self.m_maxStopsDistance+self.m_Chromosome[i-1]
                leftFromEnd = self.m_RoadLength-(self.m_StopsCount-i)*self.m_maxStopsDistance
                rightFromEnd = self.m_RoadLength-(self.m_StopsCount-i)*self.m_minStopsDistance
                leftBorder=max(leftFromEnd,leftBorder)
                rightBorder=min(rightFromEnd,rightBorder)
                self.m_Chromosome[i]=random.random()*(rightBorder-leftBorder)+leftBorder
            else:
                if self.m_Chromosome[i]<leftBorder:
                    self.m_Chromosome[i]=leftBorder
                if self.m_Chromosome[i]>rightBorder:
                    self.m_Chromosome[i]=rightBorder
            
            
                
            