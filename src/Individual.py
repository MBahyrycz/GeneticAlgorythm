import random
import math


class Individual:
    def __init__(self, stopsCount, roadLength, mutationProbability,minStopsDistance,maxStopsDistance,bannedAreas):
        self.m_StopsCount = stopsCount
        self.m_RoadLength = roadLength
        self.m_Chromosome = []
        self.m_Quality = 0.0
        self.m_minStopsDistance=minStopsDistance
        self.m_maxStopsDistance=maxStopsDistance
        self.m_MutationProbability = mutationProbability
        self.m_bannedAreas=bannedAreas

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
            if leftBorder>rightBorder:
                raise ValueError("Incorrect stop distances (%f,%f)"%(self.m_minStopsDistance,self.m_maxStopsDistance))
            self.PlaceInBorders(i,leftBorder,rightBorder)
            #self.m_Chromosome.append(random.random()*(rightBorder-leftBorder)+leftBorder)
            
    def PlaceInBorders(self,index,leftBorder,rightBorder):
        availibleAreas=[]
        currentLeftBorder=leftBorder
        for area in self.m_bannedAreas:
            if currentLeftBorder<area[1]:
                if currentLeftBorder<area[0]:
                    if area[0]<rightBorder:
                        availibleAreas.append((currentLeftBorder,area[0]))
                    else:
                        availibleAreas.append((currentLeftBorder,rightBorder))
                currentLeftBorder=area[1]
            if area[1]>rightBorder:
                break;
        if len(self.m_bannedAreas)==0:
            availibleAreas=[(leftBorder,rightBorder)]
        else:
            if self.m_bannedAreas[-1][1]<rightBorder:
                if self.m_bannedAreas[-1][1]<leftBorder:
                    availibleAreas.append((leftBorder,rightBorder))
                else:
                    availibleAreas.append((self.m_bannedAreas[-1][1],rightBorder))
        #print(leftBorder,rightBorder,availibleAreas)
        if len(availibleAreas)==0:
            self.m_Quality=math.inf
            if index>=len(self.m_Chromosome):
                self.m_Chromosome.append(random.random()*(rightBorder-leftBorder)+leftBorder)
            else:
                self.m_Chromosome[index]=random.random()*(rightBorder-leftBorder)+leftBorder
            return
            #raise ValueError("Cannot place stop between (%f,%f)"%(leftBorder,rightBorder))
        randArea=availibleAreas[random.randint(0,len(availibleAreas)-1)]
        if index>=len(self.m_Chromosome):
            self.m_Chromosome.append(random.random()*(randArea[1]-randArea[0])+randArea[0])
        else:
            self.m_Chromosome[index]=random.random()*(randArea[1]-randArea[0])+randArea[0]
    
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
            self.PlaceInBorders(index,leftBorder,rightBorder)
    
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
                self.PlaceInBorders(i,leftBorder,rightBorder)
            else:
                if self.m_Chromosome[i]<leftBorder:
                    self.m_Chromosome[i]=leftBorder
                    for area in self.m_bannedAreas:
                        if area[0]<self.m_Chromosome[i] and self.m_Chromosome[i]<area[1]:
                            self.m_Chromosome[i]=area[1]
                            break
                if self.m_Chromosome[i]>rightBorder:
                    self.m_Chromosome[i]=rightBorder
                    for area in self.m_bannedAreas:
                        if area[0]<self.m_Chromosome[i] and self.m_Chromosome[i]<area[1]:
                            self.m_Chromosome[i]=area[0]
                            break
            
            
                
            