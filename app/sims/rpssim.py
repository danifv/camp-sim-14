'''
Created on Aug 8, 2014

@author: daniel
'''


import random

class InvalidChancesError(Exception):
    
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return "A valoszinusegek osszege legyen 1!"

class RpsSim(object):    
    
    def __init__(self, sameChance, strongerChance):
        self.playerWins = 0.0
        self.compWins = 0.0        
        self.sameChance = float(sameChance)
        self.strongerChance = float(strongerChance)
        
        if self.sameChance + self.strongerChance > 1.0:
            raise InvalidChancesError()
        else:
            self.weakerChance = 1.0 - self.sameChance - self.strongerChance
            
    def simulate(self):
            
        playerFirstPlay = self.getRandomPlay()
        compFirstPlay = self.getRandomPlay()
        allPlayerWins = []
        allCompWins = []
        
        winner = self.determineWinner(playerFirstPlay, compFirstPlay)
        if winner == 'A': self.playerWins += 1        
        elif winner == 'B': self.compWins += 1
        allPlayerWins.append(self.playerWins)
        allCompWins.append(self.compWins)
        
        playerPrevPlay = playerFirstPlay
        compPrevPlay = compFirstPlay
        
        for i in range (1, 1000):
            compRoll = self.compDecide()
            playerRoll = self.playerDecide()
            
            compPlay = self.simulatePlay(compRoll, playerPrevPlay)
            playerPlay = self.simulatePlay(playerRoll, playerPrevPlay)            
            winner = self.determineWinner(playerPlay, compPlay)
            playerPrevPlay = playerPlay
            compPrevPlay = compPlay            
            
            if winner == 'A': 
                self.playerWins += 1                
            elif winner == 'B': 
                self.compWins += 1                
            allPlayerWins.append(self.playerWins)
            allCompWins.append(self.compWins)
        return {'Jatekos gyozelmei': allPlayerWins, 'Gep gyozelmei': allCompWins}

        
    def compDecide(self):
        hand = random.random()        
        if hand < 2.0/6.0: roll = 'same'
        elif hand < 5.0/6.0: roll = 'stronger'
        else: roll = 'weaker'
        return roll
        
    def playerDecide(self):
        hand = random.random()
        if hand < self.sameChance: roll = 'same'
        elif hand < self.sameChance + self.strongerChance: roll = 'stronger'
        else: roll = 'weaker'
        return roll
    
    def simulatePlay(self, previousPlayerAHand, playerBRoll):
        if previousPlayerAHand == 'same':
            playerAPlay = playerBRoll
        elif previousPlayerAHand == 'stronger':
            if playerBRoll == 'rock': playerAPlay = 'paper'
            elif playerBRoll == 'paper': playerAPlay = 'scissors'
            else: playerAPlay = 'rock'
        elif previousPlayerAHand == 'weaker':
            if playerBRoll == 'rock': playerAPlay = 'scissors'
            elif playerBRoll == 'paper': playerAPlay = 'rock'
            else: playerAPlay = 'paper'
        return playerAPlay
        
    def determineWinner(self, playerAPlay, playerBPlay):
        if playerAPlay == 'rock':
            if playerBPlay == 'scissors': return 'A'
            elif playerBPlay == 'paper': return 'B'
            else: return 'draw'
        if playerAPlay == 'paper':
            if playerBPlay == 'rock': return 'A'
            elif playerBPlay == 'scissors': return 'B'
            else: return 'draw'
        if playerAPlay == 'scissors':
            if playerBPlay == 'paper': return 'A'
            elif playerBPlay == 'rock': return 'B'
            else: return 'draw'
    
    def getRandomPlay(self):
        r = random.random()
        if r < 1.0/3.0: return 'rock'
        elif r < 2.0/3.0: return 'paper'
        else: return 'scissors'
        
    