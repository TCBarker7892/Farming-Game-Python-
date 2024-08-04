import contextlib
import os
with contextlib.redirect_stdout(None):
    import pygame

from GlobalVariables import WIDTH, HEIGHT, TILESIZE, iconFolderLocation, getDict

#Retrieve dictionaries
buyPrice = getDict('Item Buy Price')
sellPrice = getDict('Item Sell Price')
unlockPrice = getDict('Item Unlock Price')
cropSeedName = getDict('Crop Seed Name')
iconLib = getDict('Icons')

pygame.init()

#Define colours
colourDict = {
    'Light Grey' : (180, 180, 180),
    'Dark Grey 1' : (110, 110, 110),
    'Dark Grey 2' : (70, 70, 70),
    'Green 1' : (5,250,150),
    'Green 2' : (4, 200, 120),
    'Green 3' : (3, 150, 90),
    'Green 4' : (2, 100, 60),
    #'farmlandWet' : (97, 54, 19), not in use
    #'farmlandDry' : (153, 121, 80), not in use
}

#Import tool icons
wateringCanIcon = pygame.image.load(os.path.join(iconFolderLocation, 'watering_can.png'))
shearsIcon = pygame.image.load(os.path.join(iconFolderLocation, 'shears.png'))
bucketIcon = pygame.image.load(os.path.join(iconFolderLocation, 'bucket.png'))
hoeIcon = pygame.image.load(os.path.join(iconFolderLocation, 'hoe.png'))

ui_sheet = pygame.image.load(os.path.join(iconFolderLocation, 'ui_sheet.png'))
hotbar = ui_sheet.subsurface(pygame.Rect(96, 320, 208, 32))
hotbar = pygame.transform.scale(hotbar, (728, 112))

#Create fonts
purseBalanceFont = pygame.font.SysFont(('arial'), 36)
helpPageFont = pygame.font.SysFont(('Calibri'), 36)
font1 = pygame.font.SysFont(('bookmanoldstyle', 'bookantiqua', 'arial'), 30)
font2 = pygame.font.SysFont(('baskervilleoldface', 'arial'), 60)

#Load and scale textures
stonePathTexture = pygame.transform.scale(pygame.image.load(os.path.join(iconFolderLocation, 'stone_path.png')), (TILESIZE, TILESIZE)) #ID_0
grassTexture1 = pygame.transform.scale(pygame.image.load(os.path.join(iconFolderLocation, 'grass1.png')), (TILESIZE, TILESIZE)) #ID_1
grassTexture2 = pygame.transform.scale(pygame.image.load(os.path.join(iconFolderLocation, 'grass2.png')), (TILESIZE, TILESIZE)) #ID_2
grassTexture3 = pygame.transform.scale(pygame.image.load(os.path.join(iconFolderLocation, 'grass3.png')), (TILESIZE, TILESIZE)) #ID_3
farmlandDryTexture = pygame.transform.scale(pygame.image.load(os.path.join(iconFolderLocation, 'farmland_dry.png')), (TILESIZE, TILESIZE)) #ID_4
farmlandWetTexture = pygame.transform.scale(pygame.image.load(os.path.join(iconFolderLocation, 'farmland_wet.png')), (TILESIZE, TILESIZE)) #ID_5

treeTexture = pygame.transform.scale(pygame.image.load(os.path.join(iconFolderLocation, 'tree.png')), (TILESIZE, TILESIZE)) #ID_1
signTexture = pygame.transform.scale(pygame.image.load(os.path.join(iconFolderLocation, 'sign.png')), (TILESIZE, TILESIZE)) #ID_3
cowYoungTexture = pygame.transform.scale(pygame.image.load(os.path.join(iconFolderLocation, 'cow_young.png')), (TILESIZE, TILESIZE)) #ID_5

def baseScreen():
    Surface = pygame.Surface((WIDTH, HEIGHT))
    Surface.fill(colourDict['Green 1'])
    pygame.draw.rect(Surface, colourDict['Green 2'], [60, 60, 1160, 600], 0)
    pygame.draw.rect(Surface, colourDict['Green 3'], [80, 80, 80, 80], 0)
    Surface.blit(font1.render('Back', True, 'black'), (83, 100))
    return Surface

def createGameGUI(HeldItem):

    #Create Game Gui template
    Surface = pygame.Surface((WIDTH, HEIGHT))
    Surface.set_colorkey((0,0,1))
    Surface.fill((0,0,1))

    #Empty Hotbar
    Surface.blit(hotbar, (280, 600))

    #Hotbar Items
    Surface.blit(pygame.transform.scale(wateringCanIcon, (56, 56)), (350, 590))
    Surface.blit(pygame.transform.scale(shearsIcon, (56, 56)), (470, 590))
    Surface.blit(pygame.transform.scale(bucketIcon, (56, 56)), (600, 600))
    Surface.blit(pygame.transform.scale(hoeIcon, (56, 56)), (720, 600))

    #Blank Balance Display
    pygame.draw.rect(Surface, colourDict['Light Grey'], [30, 30, 200, 50], 0)
    pygame.draw.rect(Surface, colourDict['Dark Grey 1'], [34, 34, 192, 42], 0)
    Surface.blit(pygame.transform.scale(iconLib['Coin'], (60, 60)), (30, 25))

    #Side Buttons
    pygame.draw.rect(Surface, colourDict['Light Grey'], [1155, 25, 100, 100], 0)
    pygame.draw.rect(Surface, colourDict['Light Grey'], [1155, 145, 100, 100], 0)
    Surface.blit(font1.render('Menu', True, 'black'), (1165, 55))
    Surface.blit(font1.render('Shop', True, 'black'), (1165, 175))

    return Surface

baseTilemapDict = {
    0 : stonePathTexture,
    1 : grassTexture1,
    2 : grassTexture2,
    3 : grassTexture3,
    4 : farmlandDryTexture,
    5 : farmlandWetTexture,
}

detailTilemapDict = {
    1 : treeTexture,
    3 : signTexture,
    5 : cowYoungTexture,
}

def renderTilemaps(baseMap, detailMap, playerX, playerY, playerRendX, playerRendY):

    baseTileSurface = pygame.Surface((WIDTH, HEIGHT))
    detailTileSurface = pygame.Surface((WIDTH, HEIGHT))
    detailTileSurface.set_colorkey((0, 0, 1))
    detailTileSurface.fill((0, 0, 1))

    for i in range(playerX - 10, playerX + 11):
        for j in range(playerY - 5, playerY + 7):
            baseTileSurface.blit(baseTilemapDict[baseMap[i,j]], (playerRendX - TILESIZE*(playerX - i), playerRendY - TILESIZE*(playerY - j)))         
                        
            if detailMap[i,j] != 0:
                detailTileSurface.blit(detailTilemapDict[detailMap[i,j]], (playerRendX - TILESIZE*(playerX - i), playerRendY - TILESIZE*(playerY - j)))
        
    baseTileSurface.blit(detailTileSurface, (0,0))
    return baseTileSurface

def createGuideScreen():
    
    Surface = baseScreen()
    Surface.blit(font2.render('Quick Start Guide', True, 'black'), (200, 95))

    Surface.blit(pygame.transform.scale(hoeIcon, (100,100)), (100,300))
    Surface.blit(helpPageFont.render('Hoe description', True, 'black'), (200,300))

    return Surface
            
def createMenuScreen():

    Surface = baseScreen()

    pygame.draw.rect(Surface, 'white', [900, 180, 300, 460], 0)
    Surface.blit(font2.render('Paused', True, 'black'), (200, 95))

    pygame.draw.rect(Surface, colourDict['Green 3'], [80, 180, 800, 100], 0)
    Surface.blit(font2.render('Settings', True, 'black'), (110,205))

    pygame.draw.rect(Surface, colourDict['Green 3'], [80, 300, 800, 100], 0)
    Surface.blit(font2.render('Controls', True, 'black'), (110,325))

    pygame.draw.rect(Surface, colourDict['Green 3'], [80, 420, 800, 100], 0)
    Surface.blit(font2.render('Stats', True, 'black'), (110,445))

    pygame.draw.rect(Surface, colourDict['Green 3'], [80, 540, 800, 100], 0)
    Surface.blit(font2.render('Quick start guide', True, 'black'), (110,565))

    pygame.draw.rect(Surface, colourDict['Green 3'], [800, 80, 80, 80], 0)
    Surface.blit(font1.render('Save', True, 'black'), (803,100))

    pygame.draw.rect(Surface, colourDict['Green 3'], [900, 80, 300, 80], 0)    
    Surface.blit(font1.render('Save & Quit to Title', True, 'black'), (900,100))

    return Surface

def createInventoryScreen():
    
    Surface = baseScreen()
    Surface.blit(font2.render('Inventory!', True, 'black'), (200, 95))

    Surface.blit(pygame.transform.scale(iconLib['Carrot'], (40, 40)), (100, 200))
    Surface.blit(pygame.transform.scale(iconLib['Potato'], (40, 40)), (100, 250))
    Surface.blit(pygame.transform.scale(iconLib['Wheat'], (40, 40)), (100, 300))
    Surface.blit(pygame.transform.scale(iconLib['Beetroot'], (40, 40)), (100, 350))
    Surface.blit(pygame.transform.scale(iconLib['Melon'], (40, 40)), (100, 400))
    Surface.blit(pygame.transform.scale(iconLib['Bamboo'], (40, 40)), (100, 450))
    Surface.blit(pygame.transform.scale(iconLib['Cherry'], (40, 40)), (100, 500))
    Surface.blit(pygame.transform.scale(iconLib['Apple'], (40, 40)), (100, 550))

    return Surface

def createStatsScreen():
    Surface = baseScreen()

    return Surface

def createTitleScreen():
    Surface = baseScreen()

    return Surface

def createControlsScreen():
    Surface = baseScreen()

    return Surface

def createSettingsScreen():
    Surface = baseScreen()

    return Surface

def createShopScreen():
                
    Surface = baseScreen()
    Surface.blit(font2.render('Shop', True, 'black'), (200, 95))

    pygame.draw.rect(Surface, colourDict['Green 1'], [80, 180, 260, 460], 0)
    pygame.draw.rect(Surface, colourDict['Green 1'], [365, 180, 260, 460], 0)
    pygame.draw.rect(Surface, colourDict['Green 1'], [650, 180, 260, 460], 0)
    pygame.draw.rect(Surface, colourDict['Green 1'], [935, 180, 260, 460], 0)

    #Crop Menu
    Surface.blit(font1.render('Crops:', True, 'black'), (100, 200))
    pygame.draw.rect(Surface, colourDict['Green 3'], [100, 280, 100, 100], 0)
    pygame.draw.rect(Surface, colourDict['Green 3'], [220, 280, 100, 100], 0)
    pygame.draw.rect(Surface, colourDict['Green 3'], [100, 400, 100, 100], 0)
    pygame.draw.rect(Surface, colourDict['Green 3'], [220, 400, 100, 100], 0)
    pygame.draw.rect(Surface, colourDict['Green 3'], [100, 520, 100, 100], 0)
    pygame.draw.rect(Surface, colourDict['Green 3'], [220, 520, 100, 100], 0)
    Surface.blit(pygame.transform.scale(iconLib['Carrot'], (100, 100)), (100, 280))
    Surface.blit(pygame.transform.scale(iconLib['Potato'], (100, 100)), (220, 280))
    Surface.blit(pygame.transform.scale(iconLib['Wheat'], (100, 100)), (100, 400))
    Surface.blit(pygame.transform.scale(iconLib['Beetroot'], (100, 100)), (220, 400))
    Surface.blit(pygame.transform.scale(iconLib['Melon'], (100, 100)), (100, 520))
    Surface.blit(pygame.transform.scale(iconLib['Bamboo'], (100, 100)), (220, 520))

    #Tree Menu
    Surface.blit(font1.render('Trees:', True, 'black'), (385, 200))
    pygame.draw.rect(Surface, colourDict['Green 3'], [385, 280, 100, 100], 0)
    pygame.draw.rect(Surface, colourDict['Green 3'], [505, 280, 100, 100], 0)
    Surface.blit(pygame.transform.scale(iconLib['Cherry'], (100, 100)), (385, 280))
    Surface.blit(pygame.transform.scale(iconLib['Apple'], (100, 100)), (505, 280))
    
    #Animal Menu
    Surface.blit(font1.render('Animals:', True, 'black'), (670, 200))
    pygame.draw.rect(Surface, colourDict['Green 3'], [670, 280, 100, 100], 0)
    pygame.draw.rect(Surface, colourDict['Green 3'], [790, 280, 100, 100], 0)
    pygame.draw.rect(Surface, colourDict['Green 3'], [670, 400, 100, 100], 0)
    pygame.draw.rect(Surface, colourDict['Green 3'], [790, 400, 100, 100], 0)
    Surface.blit(pygame.transform.scale(iconLib['Chicken'], (100, 100)), (670, 280)) #Chicken
    Surface.blit(pygame.transform.scale(iconLib['Goat'], (100, 100)), (790, 280)) #Goat
    Surface.blit(pygame.transform.scale(iconLib['Sheep'], (100, 100)), (670, 400)) #Sheep
    Surface.blit(pygame.transform.scale(iconLib['Cow'], (100, 100)), (790, 400)) #Cow

    #Decorations Menu
    Surface.blit(font1.render('Decorations:', True, 'black'), (955, 200))
    pygame.draw.rect(Surface, colourDict['Green 3'], [955, 280, 100, 100], 0)
    pygame.draw.rect(Surface, colourDict['Green 3'], [1075, 280, 100, 100], 0)
    pygame.draw.rect(Surface, colourDict['Green 3'], [955, 400, 100, 100], 0)
    Surface.blit(pygame.transform.scale(iconLib['Fence'], (100, 100)), (955, 280)) #Fence
    Surface.blit(pygame.transform.scale(iconLib['Sign'], (100, 100)), (1075, 280)) #Sign
    Surface.blit(pygame.transform.scale(iconLib['Stone Path'], (100, 100)), (955, 400)) #Stone Path
    
    #Coin Balance Area
    pygame.draw.rect(Surface, colourDict['Light Grey'], [970, 80, 200, 50], 0)
    pygame.draw.rect(Surface, colourDict['Dark Grey 1'], [974, 84, 192, 42], 0)
    Surface.blit(pygame.transform.scale(iconLib['Coin'], (60, 60)), (970, 75))

    return Surface

def createCropShopScreen(cropName, unlockStatus):

    Surface = baseScreen()

    pygame.draw.rect(Surface, colourDict['Green 1'], [750, 150, 450, 350], 0)
    Surface.blit(pygame.transform.scale(iconLib[cropName], (250, 250)), (850, 200))

    #Coin Balance
    pygame.draw.rect(Surface, colourDict['Light Grey'], [970, 80, 200, 50], 0)
    pygame.draw.rect(Surface, colourDict['Dark Grey 1'], [974, 84, 192, 42], 0)
    Surface.blit(pygame.transform.scale(iconLib['Coin'], (60, 60)), (970, 75))

    if unlockStatus:
        pygame.draw.rect(Surface, colourDict['Green 1'], [80, 180, 650, 460], 0)
        Surface.blit(font2.render(cropName, True, 'black'), (200, 95))
        pygame.draw.rect(Surface, colourDict['Green 3'], [750, 520, 215, 120], 0)
        pygame.draw.rect(Surface, colourDict['Green 3'], [985, 520, 215, 120], 0)
        Surface.blit(font1.render('Buy Seeds:', True, 'black'), (770, 545))
        Surface.blit(font1.render('Sell Crops:', True, 'black'), (1005, 545))
        Surface.blit(font1.render('$' + str(buyPrice[cropSeedName[cropName]]), True, 'black'), (770, 575))
        Surface.blit(font1.render('$' + str(sellPrice[cropName]), True, 'black'), (1005, 575))
    else:
        pygame.draw.rect(Surface, colourDict['Green 4'], [80, 180, 650, 460], 0)

        #Drawing padlock symbol
        pygame.draw.circle(Surface, colourDict['Green 3'], (405, 300), 80, 0)
        pygame.draw.circle(Surface, colourDict['Green 4'], (405, 300), 50, 0)
        pygame.draw.rect(Surface, colourDict['Green 4'], [305, 300, 200, 70], 0)
        pygame.draw.rect(Surface, colourDict['Green 3'], [325, 300, 30, 70], 0)
        pygame.draw.rect(Surface, colourDict['Green 3'], [455, 300, 30, 70], 0)
        pygame.draw.rect(Surface, colourDict['Green 3'], [305, 370, 200, 200], 0)

        Surface.blit(font2.render(cropName + ' (Locked)', True, 'black'), (200, 95))
        pygame.draw.rect(Surface, colourDict['Green 3'], [750, 520, 450, 120], 0)
        Surface.blit(font1.render('Unlock: $' + str(unlockPrice[cropName]), True, 'black'), (770, 550))
        
    return Surface

def createTreeShopScreen(treeName, unlockStatus):

    Surface = baseScreen()

    return Surface

def createAnimalShopScreen(animalName, unlockStatus):

    Surface = baseScreen()

    return Surface

def createDecorationShopScreen(decorationName, unlockStatus):

    Surface = baseScreen()

    return Surface

inventoryScreen = createInventoryScreen()
shopScreen = createShopScreen()
menuScreen = createMenuScreen()
guideScreen = createGuideScreen()
statsScreen = createStatsScreen()
titleScreen = createTitleScreen()
controlsScreen = createControlsScreen()
settingsScreen = createSettingsScreen()

carrotShopLocked = createCropShopScreen('Carrot', False)
carrotShopUnlocked = createCropShopScreen('Carrot', True)
potatoShopLocked = createCropShopScreen('Potato', False)
potatoShopUnlocked = createCropShopScreen('Potato', True)
wheatShopLocked = createCropShopScreen('Wheat', False)
wheatShopUnlocked = createCropShopScreen('Wheat', True)
beetrootShopLocked = createCropShopScreen('Beetroot', False)
beetrootShopUnlocked = createCropShopScreen('Beetroot', True)
melonShopLocked = createCropShopScreen('Melon', False)
melonShopUnlocked = createCropShopScreen('Melon', True)
bambooShopLocked = createCropShopScreen('Bamboo', False)
bambooShopUnlocked = createCropShopScreen('Bamboo', True)

cherryShopLocked = createTreeShopScreen('Cherry', False)
cherryShopUnlocked = createTreeShopScreen('Cherry', True)
appleShopLocked = createTreeShopScreen('Apple', False)
appleShopUnlocked = createTreeShopScreen('Apple', True)

chickenShopLocked = createAnimalShopScreen('Chicken', False)
chickenShopUnlocked = createAnimalShopScreen('Chicken', True)
goatShopLocked = createAnimalShopScreen('Goat', False)
goatShopUnlocked = createAnimalShopScreen('Goat', True)
sheepShopLocked = createAnimalShopScreen('Sheep', False)
sheepShopUnlocked = createAnimalShopScreen('Sheep', True)
cowShopLocked = createAnimalShopScreen('Cow', False)
cowShopUnlocked = createAnimalShopScreen('Cow', True)

fenceShopLocked = createDecorationShopScreen('Fence', False)
fenceShopUnlocked = createDecorationShopScreen('Fence', True)
signShopLocked = createDecorationShopScreen('Sign', False)
signShopUnlocked = createDecorationShopScreen('Sign', True)
stonePathShopLocked = createDecorationShopScreen('Stone Path', False)
stonePathShopUnlocked = createDecorationShopScreen('Stone Path', True)


screenDict = {
    'Stats' : statsScreen,
    'Title' : titleScreen,
    'Controls' : controlsScreen,
    'Settings' : settingsScreen,
    'Guide' : guideScreen,
    'Menu' : menuScreen,
    'Inventory' : inventoryScreen,
    'Shop' : shopScreen,
    'Carrot_ShopLocked' : carrotShopLocked,
    'Carrot_ShopUnlocked' : carrotShopUnlocked,
    'Potato_ShopLocked' : potatoShopLocked,
    'Potato_ShopUnlocked' : potatoShopUnlocked,
    'Wheat_ShopLocked' : wheatShopLocked,
    'Wheat_ShopUnlocked' : wheatShopUnlocked,
    'Beetroot_ShopLocked' : beetrootShopLocked,
    'Beetroot_ShopUnlocked' : beetrootShopUnlocked,
    'Melon_ShopLocked' : melonShopLocked,
    'Melon_ShopUnlocked' : melonShopUnlocked,
    'Bamboo_ShopLocked' : bambooShopLocked,
    'Bamboo_ShopUnlocked' : bambooShopUnlocked,
    'Cherry_ShopLocked' : cherryShopLocked,
    'Cherry_ShopUnlocked' : cherryShopUnlocked,
    'Apple_ShopLocked' : appleShopLocked,
    'Apple_ShopUnlocked' : appleShopUnlocked,
    'Chicken_ShopLocked' : chickenShopLocked,
    'Chicken_ShopUnlocked' : chickenShopUnlocked,
    'Goat_ShopLocked' : goatShopLocked,
    'Goat_ShopUnlocked' : goatShopUnlocked,
    'Sheep_ShopLocked' : sheepShopLocked,
    'Sheep_ShopUnlocked' : sheepShopUnlocked,
    'Cow_ShopLocked' : cowShopLocked,
    'Cow_ShopUnlocked' : cowShopUnlocked,
    'Fence_ShopLocked' : fenceShopLocked,
    'Fence_ShopUnlocked' : fenceShopUnlocked,
    'Sign_ShopLocked' : signShopLocked,
    'Sign_ShopUnlocked' : signShopUnlocked,
    'Stone Path_ShopLocked' : stonePathShopLocked,
    'Stone Path_ShopUnlocked' : stonePathShopUnlocked,
}


#Temporary blit handling (rough code)
class tempBlits:

    def __init__(self):
        self.list = []
        self.surface = pygame.Surface((WIDTH, HEIGHT))

    def addBlit(self, surface, duration, position, currentTime):
        instance = [surface, position, currentTime + (duration*1000)] # [blitSurface, blitPosition, blitEndtime]
        self.list.append(instance)

    def update(self, currentTime):
        listChangedBool = False

        for instance in self.list:
            if instance[2] > currentTime:
                self.list.remove(instance)
                listChangedBool = True
        
        if listChangedBool:
            self.surface = pygame.Surface((WIDTH, HEIGHT))
            for instance in self.list:
                self.surface.blit(instance[0], instance[1])


                
