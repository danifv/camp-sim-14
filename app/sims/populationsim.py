'''
Created on Aug 4, 2014

@author: daniel
'''

import random

class TimeEvents(object):
    
    @staticmethod
    def TimeTick(rate, eventsPerTick, maxEvents):
        events = 0
        for i in range (eventsPerTick):
            if random.random() < rate:
                events += 1
        if events > maxEvents:
            events = maxEvents
        return events
    

class Rabbits(object):
    def __init__(self, currentPop, maxPop):
        self.currentPop = currentPop
        self.maxPop = maxPop
        
    def getBirths(self):
        return TimeEvents.TimeTick(1.0 - (float(self.currentPop)/float(self.maxPop)), self.currentPop, self.maxPop)        
        
    def getHunts(self, numberOfHunters):
        return TimeEvents.TimeTick((float(self.currentPop)/float(self.maxPop)), numberOfHunters, self.currentPop)             

class Foxes(object):
    def __init__(self, currentPop, birthRate, deathRate, maxPop):
        self.currentPop = currentPop
        self.birthRate = birthRate
        self.deathRate = deathRate
        self.maxPop = maxPop
        
    def getBirths(self, numberOfHunts):
        return TimeEvents.TimeTick(self.birthRate, numberOfHunts, min(self.maxPop, numberOfHunts))
    
    def getDeaths(self, numberOfHunts):
        return TimeEvents.TimeTick(self.deathRate, self.currentPop - numberOfHunts, self.currentPop)
    
    def getHunts(self, numberOfHunters):
        return TimeEvents.TimeTick(float(self.currentPop)/float(self.maxPop), numberOfHunters, self.currentPop)
    
class Hunters(object):
    def __init__(self, numberOfHunters, maxRabbitHunts, maxFoxHunts):
        self.numberOfHunters = numberOfHunters
        self.maxRabbitHunts = maxRabbitHunts
        self.maxFoxHunts = maxFoxHunts
    
    
class PopulationSim(object):
    rabbitStart = 500
    foxStart = 30
    foxBirthRate = 0.33
    foxDeathRate = 0.1
    
    maxRabbitPop = 1000
    maxFoxPop = 200
    
    
    def __init__(self, numberOfHunters, maxRabbitHunts, maxFoxHunts, seasonStart, simulationLength):
        self.rabbits = Rabbits(self.rabbitStart, self.maxRabbitPop)
        self.foxes = Foxes(self.foxStart, self.foxBirthRate, self.foxDeathRate, self.maxFoxPop)
        self.hunters = Hunters(int(numberOfHunters), int(maxRabbitHunts), int(maxFoxHunts))
        self.seasonStart = seasonStart
        
        self.simulationLength = simulationLength
    
    def simulate(self):
        totalRabbitHunts = 0
        totalFoxHunts = 0
        
        rabbitPopRecord = [self.rabbits.currentPop]
        foxPopRecord = [self.foxes.currentPop]
        
        for i in range(1, self.simulationLength ):
            rBirths = self.rabbits.getBirths()        
            rHunts = self.rabbits.getHunts(self.foxes.currentPop)
            
            fBirths = self.foxes.getBirths(rHunts)
            fDeaths = self.foxes.getDeaths(rHunts)
            
            hunterRabbitHunts = 0
            hunterFoxHunts = 0
            
            if self.isHuntingSeason(i):
                hunterRabbitHunts = self.hunterHunt(self.rabbits, totalRabbitHunts, self.hunters.maxRabbitHunts)
                hunterFoxHunts = self.hunterHunt(self.foxes, totalFoxHunts, self.hunters.maxFoxHunts)
            self.rabbits.currentPop = self.rabbits.currentPop + rBirths - rHunts - hunterRabbitHunts
            if self.rabbits.currentPop > self.maxRabbitPop:
                self.rabbits.currentPop = self.maxRabbitPop
            
            self.foxes.currentPop = self.foxes.currentPop + fBirths - fDeaths - hunterFoxHunts
            rabbitPopRecord.append(self.rabbits.currentPop)
            foxPopRecord.append(self.foxes.currentPop)
            
        return {'Nyulak': rabbitPopRecord, 'Rokak': foxPopRecord}
            
    
    def isHuntingSeason(self, time):
        return int(time) >= int(self.seasonStart)
    
    def hunterHunt(self, prey, totalHunterPreyHunts, maxPreyHunts):
        hunterPreyHunts = prey.getHunts(self.hunters.numberOfHunters)
        if hunterPreyHunts + totalHunterPreyHunts <= maxPreyHunts:
            totalHunterPreyHunts += hunterPreyHunts
        else:
            totalHunterPreyHunts = maxPreyHunts
            hunterPreyHunts = 0
        return hunterPreyHunts
