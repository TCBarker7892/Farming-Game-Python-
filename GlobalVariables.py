import os
import contextlib
with contextlib.redirect_stdout(None):
    import pygame

WIDTH, HEIGHT = (1280, 720)
TILESIZE = 64

#Get file locations
dataFolderLocation = os.path.join(os.path.dirname(__file__), 'dataFolder')
iconFolderLocation = os.path.join(os.path.dirname(__file__), 'gameIcons')
speciesFolderLocation = os.path.join(dataFolderLocation, 'speciesData')

#Convenience functions (catch 'None' value errors)
def readString(value):
    if value == 'None':
        tempVar = None
    else:
        tempVar = str(value)
    return tempVar

def readInteger(value):
    if value == 'None':
        tempVar = None
    else:
        tempVar = int(value)
    return tempVar

#Read data files

with open(os.path.join(dataFolderLocation, 'itemData.txt'), 'r') as f:
    itemType = {}
    buyPrice = {}
    sellPrice = {}
    unlockPrice = {}

    for line in f:
        lineData = line.strip().split(',')
        key = readString(lineData[0])

        itemType[key] = readString(lineData[1])
        buyPrice[key] = readInteger(lineData[2])
        sellPrice[key] = readInteger(lineData[3])
        unlockPrice[key] = readInteger(lineData[4])

with open(os.path.join(speciesFolderLocation, 'cropData.txt'), 'r') as f:

    cropSeedName = {}
    cropGrowTime = {}
    cropDehydrateTime = {}

    for line in f:
        lineData = line.strip().split(',')
        key = readString(lineData[0])

        cropSeedName[key] = readString(lineData[1])
        cropGrowTime[key] = readInteger(lineData[2])
        cropDehydrateTime[key] = readInteger(lineData[3])

with open(os.path.join(speciesFolderLocation, 'treeData.txt'), 'r') as f:
        
    treeSaplingName = {}
    treeGrowTime = {}
    treeFruitTime = {}

    for line in f:
        lineData = line.strip().split(',')
        key = readString(lineData[0])

        treeSaplingName[key] = readString(lineData[1])
        treeGrowTime[key] = readInteger(lineData[2])
        treeFruitTime[key] = readInteger(lineData[3])

with open(os.path.join(speciesFolderLocation, 'animalData.txt'), 'r') as f:
        
    animalBabyName = {}
    animalProduceName = {}
    animalMeatName = {}
    animalMatureTime = {}
    animalProduceTime = {}

    for line in f:
        lineData = line.strip().split(',')
        key = readString(lineData[0])

        animalBabyName[key] = readString(lineData[1])
        animalProduceName[key] = readString(lineData[2])
        animalMeatName[key] = readString(lineData[3])
        animalMatureTime[key] = readInteger(lineData[4])
        animalProduceTime[key] = readInteger(lineData[5])

#Import icon textures
fillerIcon = pygame.image.load(os.path.join(iconFolderLocation, 'filler.png'))
coinIcon = pygame.image.load(os.path.join(iconFolderLocation, 'coin.png'))

carrotIcon = pygame.image.load(os.path.join(iconFolderLocation, 'carrot.png'))
potatoIcon = pygame.image.load(os.path.join(iconFolderLocation, 'potato.png'))
wheatIcon = pygame.image.load(os.path.join(iconFolderLocation, 'wheat.png'))
beetrootIcon = pygame.image.load(os.path.join(iconFolderLocation, 'beetroot.png'))
melonIcon = pygame.image.load(os.path.join(iconFolderLocation, 'melon.png'))
bambooIcon = pygame.image.load(os.path.join(iconFolderLocation, 'bamboo.png'))
cherryIcon = pygame.image.load(os.path.join(iconFolderLocation, 'cherry.png'))
appleIcon = pygame.image.load(os.path.join(iconFolderLocation, 'apple.png'))

#Create icon library
iconLib = {key: fillerIcon for key in itemType.keys()}
iconLib['Coin'] = coinIcon
iconLib['Carrot'] = carrotIcon
iconLib['Potato'] = potatoIcon
iconLib['Wheat'] = wheatIcon
iconLib['Beetroot'] = beetrootIcon
iconLib['Melon'] = melonIcon
iconLib['Bamboo'] = bambooIcon
iconLib['Cherry'] = cherryIcon
iconLib['Apple'] = appleIcon

#Create dictionary of reference dictionaries
#Master Dictionary
masterDictionary = {
    'Item Type' : itemType, 
    'Item Buy Price' : buyPrice,
    'Item Sell Price' : sellPrice,
    'Item Unlock Price' : unlockPrice,
    'Crop Seed Name' : cropSeedName,
    'Crop Grow Time' : cropGrowTime,
    'Crop Dehydrate Time' : cropDehydrateTime,
    'Tree Sapling Name' : treeSaplingName,
    'Tree Grow Time' : treeGrowTime,
    'Tree Fruit Time' : treeFruitTime,
    'Animal Baby Name' : animalBabyName,
    'Animal Produce Name' : animalProduceName,
    'Animal Meat Name' : animalMeatName,
    'Animal Mature Time' : animalMatureTime,
    'Animal Produce Time' : animalProduceTime,
    'Icons' : iconLib,
} 

def getDict(dictionaryName):

    Dictionary = masterDictionary[dictionaryName]

    return Dictionary