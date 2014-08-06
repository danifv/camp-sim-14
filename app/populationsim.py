'''
Created on Aug 4, 2014

@author: daniel
'''

import random

class TimeEvents(object):
    
    @staticmethod
    def TimeTick(rate, eventsPerTick, maxEvents):
        events = 0
        for i in range (1, eventsPerTick):
            if random.random() < rate:
                events += 1
        if events > maxEvents:
            events = maxEvents
        return events
    

class Rabbits(object):
    def __init__(self, currentPop, birthRate):
        self.currentPop = currentPop
        self.birthRate = birthRate
        
    def getBirths(self):
        return TimeEvents.TimeTick(self.birthRate, self.currentPop, self.currentPop)        
        
    def getHunts(self, huntRate, numberOfHunters):
        return TimeEvents.TimeTick(huntRate, numberOfHunters, self.currentPop)             

class Foxes(object):
    def __init__(self, currentPop, birthRate, huntRate, deathRate):
        self.currentPop = currentPop
        self.birthRate = birthRate
        self.huntRate = huntRate
        self.deathRate = deathRate
        
    def getBirths(self, numberOfHunts):
        return TimeEvents.TimeTick(self.birthRate, numberOfHunts, numberOfHunts)
    
    def getDeaths(self):
        return TimeEvents.TimeTick(self.deathRate, self.currentPop, self.currentPop)
    
    def getHunts(self, huntRate, numberOfHunters):
        return TimeEvents.TimeTick(huntRate, numberOfHunters, self.currentPop)
    
class Hunters(object):
    def __init__(self, numberOfHunters, maxRabbitHunts, maxFoxHunts, huntRate):
        self.numberOfHunters = numberOfHunters
        self.maxRabbitHunts = maxRabbitHunts
        self.maxFoxHunts = maxFoxHunts
        self.huntRate = huntRate
    
    
class PopulationSim(object):
    def __init__(self, numberOfHunters, maxRabbitHunts, maxFoxHunts, seasonStart):
        self.rabbits = Rabbits(100, 0.5)
        self.foxes = Foxes(30, 0.4, 0.9, 0.1)
        self.hunters = Hunters(numberOfHunters, maxRabbitHunts, maxFoxHunts, 0.8)
        self.seasonStart = seasonStart
    
    def simulate(self):
        totalRabbitHunts = 0
        totalFoxHunts = 0
        
        rabbitPopRecord = [self.rabbits.currentPop]
        foxPopRecord = [self.foxes.currentPop]
        
        for i in range(1, 1000):
            rBirths = self.rabbits.getBirths()        
            rHunts = self.rabbits.getHunts(self.foxes.huntRate, self.foxes.currentPop)
            
            fBirths = self.foxes.getBirths(rHunts)
            fDeaths = self.foxes.getDeaths()
            
            hunterRabbitHunts = 0
            hunterFoxHunts = 0

            if self.isHuntingSeason(i):
                hunterRabbitHunts = self.hunterHunt(totalRabbitHunts)
                hunterFoxHunts = self.hunterHunt(totalFoxHunts)
            self.rabbits.currentPop = self.rabbits.currentPop + rBirths - rHunts - hunterRabbitHunts
            self.foxes.currentPop = self.foxes.currentPop + fBirths - fDeaths - hunterFoxHunts
            rabbitPopRecord.append(self.rabbits.currentPop)
            foxPopRecord.append(self.foxes.currentPop)
            
        return {'rabbitPop': rabbitPopRecord, 'foxPop': foxPopRecord}
            
    
    def isHuntingSeason(self, time):
        return time >= self.seasonStart
    
    def hunterHunt(self, totalHunterPreyHunts):
        hunterPreyHunts = self.rabbits.getHunts(self.hunters.huntRate, self.hunters.numberOfHunters)
        if hunterPreyHunts + totalHunterPreyHunts <= self.hunters.maxRabbitHunts:
            totalHunterPreyHunts += hunterPreyHunts
        else:
            totalHunterPreyHunts = self.hunters.maxRabbitHunts
            hunterPreyHunts = 0
        return hunterPreyHunts
    
                
        
    
