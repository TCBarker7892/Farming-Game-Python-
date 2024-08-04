import os
import contextlib
with contextlib.redirect_stdout(None):
    import pygame
from pygame.sprite import Sprite, Group

from GlobalVariables import iconFolderLocation
from GlobalVariables import animalProduceTime, animalMatureTime

animalSpritesheet = pygame.image.load(os.path.join(iconFolderLocation, 'animalSpritesheet.png'))
cowSprites = Group()

#Move to data folder eventually
animalSheetDict = {
    'Adult Chicken' : (0, 0, 320, 16),
    'Baby Chicken' : (0, 16, 320, 16),
    'Adult Cow' : (0, 32, 480, 24),
    'Baby Cow' : (0, 56, 420, 21),
    'Adult Goat' : (0, 77, 380, 19),
    'Baby Goat' : (0, 96, 320, 16),
    'Adult Pig' : (0, 116, 400, 20),
    'Baby Pig' : (0, 136, 320, 16),
    'Adult Sheep' : (0, 152, 340, 17),
    'Baby Sheep' : (0, 169, 320, 16),
}

class Cow(Sprite):
    def __init__(self, name,  xPos, yPos):
        super().__init__()
        ### Add to cow and animal sprite groups!!

        #Movement Data
        self.facing = 0
        self.movementStage = 0
        self.x = xPos
        self.y = yPos
        #Timer info
        self.maturity = False
        self.maturationTimer = animalMatureTime['Cow']
        self.produceTimer = animalProduceTime['Cow']
        #Stats and cosmetics
        self.age = 0
        self.nickname = name
        self.lifetimeProduction = 0
        self.lifetimePets = 0
        #Rendering Data
        self.spritesheetAdult = animalSpritesheet.subsurface(animalSheetDict['Cow'])
        self.spritesheetBaby = animalSpritesheet.subsurface(animalSheetDict['Baby Cow'])
        self.change_texture()

    def update(self):
        output = False
        self.age += 1

        if self.maturity:
            self.produceTimer -= 1
            if self.produceTimer <= 0:
                self.lifetimeProduction += 1
                self.produceTimer = animalProduceTime['Cow']
                output = True
        else:
            self.maturationTimer -=1
            if self.maturationTimer <= 0:
                self.maturity = True
                self.maturationTimer = 0
                self.produceTimer = animalProduceTime['Cow']

        #OUTSIDE OF UPDATE FUNCTION:
        #for all cow instances:
        #If output = True: Add one to produce inventory
        return output
    
    def change_texture(self):
        spritesheetIndex = (4*self.facing) + self.movementStage

        if self.maturity:
            self.image = self.spritesheetAdult[spritesheetIndex]
        else:
            self.image = self.spritesheetBaby[spritesheetIndex]

        self.rect = self.image.get_rect()
    
    def move(self, newX, newY):
        self.x = newX
        self.y = newY


    #Legacy Code
        
    def stats(self):
        #Get stats for a stats screen in future
        statList = [self.name, self.animal, self.maturity, self.age, self.lifetimeProduction, self.pets]
        return statList
    
    def allInfo(self):
        #Get all properties for a game save
        info = [self.name, self.animal, str(self.maturity), str(self.age), str(self.maturationTimer), str(self.produceTimer), str(self.lifetimeProduction), str(self.pets), str(self.x), str(self.y)]
        toString = ','.join(info) + '\n'
        return toString
    
    def butcher(self):
        self.animal.matureInventory -= 1
        self.animal.meatInventory += 1
        animalStats = [self.name, self.animal, self.age, self.lifetimeProduction]
        del self
        return animalStats
    
    def sell(self):
        animalStats = [self.name, self.animal, self.age, self.lifetimeProduction]
        if self.maturity:
            self.animal.matureInventory -= 1
            sellValue = self.animal.maturePrice
            del self
        else:
            self.animal.youngInventory -= 1
            sellValue = self.animal.youngSellPrice
            del self
        return animalStats, sellValue