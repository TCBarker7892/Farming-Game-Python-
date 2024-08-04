import os
import contextlib
with contextlib.redirect_stdout(None):
    import pygame
    
from Characters import Character
from Graphics import createGameGUI, renderTilemaps, screenDict, colourDict
from WorldGen import newWorld
from InputProcessing import screenChangeHandling, navigationButtonHandling, hotbarButtonHandling, shopActionButtonHandling
from GlobalVariables import WIDTH, HEIGHT, TILESIZE, iconFolderLocation

class Game:
    def __init__(self):
        #Basic setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('Farming Game')
        pygame.key.set_repeat(200,100)
    
    def reset(self):
        activeTimers = []

    def loadSave(self, saveData):
        self.tileMapBase = 0
        self.tileMapDetail = 0
        self.collisionMap = 0

        collisionMap = open('collisionMap.txt','r')
        #Read saveData array to game
        
    def save(self, saveFolderName, baseTilemap, detailTilemap):
        gameDirectory = os.path.dirname(__file__)
        
        saveFolder_path = os.path.join(gameDirectory, saveFolderName)
        if not os.path.exists(saveFolder_path):
            os.makedirs(saveFolder_path)

        with open(os.path.join(saveFolder_path, 'coreData.txt'), 'w') as f:
            f.write(' '.join(map(str, self.animalCounts)) + '\n')
            f.write(str(self.purseBalance) + '\n')
        
        with open(os.path.join(saveFolder_path, 'tilemapBase.txt'), 'w') as f:
            for i in range(len(baseTilemap[0,:])):
                f.write(' '.join(map(str, baseTilemap[i,:])) + '\n')

        with open(os.path.join(saveFolder_path, 'tileMapDetail.txt'), 'w') as f:
            #Collision map encoded as Bool tile_id % 2 == 0
            for i in range(len(detailTilemap[0,:])):
                f.write(' '.join(map(str, detailTilemap[i,:])) + '\n')
             
    def run(self):
        
        #initiallise variables
        renderDiagnostics = False
        running = True
        currentScreen = 'Game'
        movingDirection = 'None'
        ingameTime = 0
        
        #Create grid position system
        playerInitX = 23
        playerInitY = 16
        playerWalkSpeed = 2
        #Please note, these choices are arbitrary
    
        playerRenderX = WIDTH/2 - TILESIZE/2
        playerRenderY = HEIGHT/2 - TILESIZE
        
        self.player = Character(playerInitX, playerInitY, 'Down', 100000)
        self.player.hotbar[0] = 'Watering Can'
        self.player.hotbar[1] = 'Shears'
        self.player.hotbar[2] = 'Bucket'
        self.player.hotbar[3] = 'Hoe'
        self.player.inventory['Carrot'] += 10000
        self.player.inventory['Potato'] += 500
        self.player.inventory['Bamboo'] += 300
        self.player.unlocks['Carrot Seeds'] = True
        
        #Loading player textures
        playerUpTexture = pygame.transform.scale(pygame.image.load(os.path.join(iconFolderLocation, 'player_up.png')), (TILESIZE, TILESIZE))
        playerDownTexture = pygame.transform.scale(pygame.image.load(os.path.join(iconFolderLocation, 'player_down.png')), (TILESIZE, TILESIZE))
        playerLeftTexture = pygame.transform.scale(pygame.image.load(os.path.join(iconFolderLocation, 'player_left.png')), (TILESIZE, TILESIZE))
        playerRightTexture = pygame.transform.scale(pygame.image.load(os.path.join(iconFolderLocation, 'player_right.png')), (TILESIZE, TILESIZE))
        
        #Creating font presets
        self.font1 = pygame.font.SysFont(('bookmanoldstyle', 'bookantiqua', 'arial'), 30)
        self.font3 = pygame.font.SysFont(('bookmanoldstyle', 'bookantiqua', 'arial'), 20)
        self.font4 = pygame.font.SysFont(('arial'), 36)

        
        def renderButton(colour, posSizeArray, textContent):
            pygame.draw.rect(self.screen, colour, posSizeArray, 0)
            self.screen.blit(self.font3.render(textContent, True, 'black'), (posSizeArray[0], posSizeArray[1]))

        def renderTileColour(xGridPos, yGridPos, colour):
            pygame.draw.rect(self.screen, colour, [playerRenderX - TILESIZE*(self.player.x - xGridPos), playerRenderY - TILESIZE*(self.player.y - yGridPos - 1), TILESIZE, TILESIZE], 0)
                
        #Create Game Gui template
        guiGame_surface = createGameGUI(self.player.hotbar[self.player.heldItem])

        
        #Generate World
        tilemapBase, tilemapDetail = newWorld(100,100)

        #Initiallise rendering booleans
        playerMoved = True
        mapEdited = True
        heldItemChanged = True
        currentScreenChanged = True
        placeMode = False

        while running:
            
            mouseXpos, mouseYpos = pygame.mouse.get_pos()

            mouseXGridPos = int(((mouseXpos-playerRenderX)/TILESIZE + self.player.x)//1)
            mouseYGridPos = int(((mouseYpos-playerRenderY)/TILESIZE + self.player.y)//1)

            prevXpos = self.player.x
            prevYpos = self.player.y

            # Check for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    buttonPressed, newScreen = navigationButtonHandling(mouseXpos, mouseYpos, currentScreen)

                    if buttonPressed:
                        currentScreen = newScreen
                        currentScreenChanged = True
                    else:
                        buttonPressed, shopOperation, targetItem = shopActionButtonHandling(mouseXpos, mouseYpos, currentScreen)
                        if buttonPressed:
                            currentScreenChanged = self.player.shopaction(shopOperation, targetItem)
                            if (currentScreen[-6:] == 'Locked') and self.player.unlocks[currentScreen[:-11]]:
                                currentScreen = currentScreen[:-6] + 'Unlocked'
                        else:

                            if currentScreen == 'Game':
                                self.player.heldItem, heldItemChanged = hotbarButtonHandling(mouseXpos, mouseYpos, self.player.heldItem)
                                if self.player.hotbar[self.player.heldItem] == 'Hoe' and not heldItemChanged:
                                    if tilemapDetail[mouseXGridPos, mouseYGridPos] == 0:
                                        if 0 < tilemapBase[mouseXGridPos, mouseYGridPos] < 4 :
                                            tilemapBase[mouseXGridPos, mouseYGridPos] = 4
                                            mapEdited = True
                                elif self.player.hotbar[self.player.heldItem] == 'Watering Can' and not heldItemChanged:
                                    if tilemapBase[mouseXGridPos, mouseYGridPos] ==  4 :
                                        tilemapBase[mouseXGridPos, mouseYGridPos] = 5
                                        mapEdited = True
                                elif self.player.hotbar[self.player.heldItem] == None and not heldItemChanged:
                                    if tilemapDetail[mouseXGridPos, mouseYGridPos] == 0:
                                        if 0 < tilemapBase[mouseXGridPos, mouseYGridPos] < 4 :
                                            tilemapDetail[mouseXGridPos, mouseYGridPos] = 5
                                            mapEdited = True

                            elif currentScreen == 'Menu':
                                if (800 < mouseXpos < 880) and (80 < mouseYpos < 160):
                                    self.save('New_Save')
                                elif (900 < mouseXpos < 1200) and (80 < mouseYpos < 160):
                                    self.save('New_Save')
                                    running = False

                if event.type == pygame.KEYDOWN:
                    currentScreen, currentScreenChanged = screenChangeHandling(event.key, currentScreen)
                    if currentScreen == 'Game':
                        if event.key == pygame.K_w:
                            movingDirection = self.player.facing = 'Up'
                            self.player.move(0,-1, tilemapDetail)
                        elif event.key == pygame.K_a:
                            movingDirection = self.player.facing = 'Left'
                            self.player.move(-1,0, tilemapDetail)
                        elif event.key == pygame.K_s:
                            movingDirection = self.player.facing = 'Down'
                            self.player.move(0,1, tilemapDetail)
                        elif event.key == pygame.K_d:
                            movingDirection = self.player.facing = 'Right'
                            self.player.move(1,0, tilemapDetail)

                    if event.key == pygame.K_l:
                        renderDiagnostics = not renderDiagnostics
                    if event.key == pygame.K_m:
                        currentScreen = 'Guide'
                
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        if movingDirection == 'Up':
                            movingDirection = 'None'
                    elif event.key == pygame.K_a:
                        if movingDirection == 'Left':
                            movingDirection = 'None'
                    elif event.key == pygame.K_s:
                        if movingDirection == 'Down':
                            movingDirection = 'None'
                    elif event.key == pygame.K_d:
                        if movingDirection == 'Right':
                            movingDirection = 'None'
            
            if currentScreen[-1] == '@':
                item = currentScreen[:-6]
                if self.player.unlocks[item]:
                    currentScreen = item + '_ShopUnlocked'
                else:
                    currentScreen = item + '_ShopLocked'
                
            # Game rendering

            if currentScreen == 'Game':
                
                #Render Game grid
                if playerMoved or mapEdited:
                    renderedTilemap = renderTilemaps(tilemapBase, tilemapDetail, self.player.x, self.player.y, playerRenderX, playerRenderY)

                self.screen.fill(colourDict['Green 1'])
                self.screen.blit(renderedTilemap, (0,0))

                if self.player.facing == 'Up':
                    self.screen.blit(playerUpTexture, (playerRenderX, playerRenderY))
                elif self.player.facing == 'Left':
                    self.screen.blit(playerLeftTexture, (playerRenderX, playerRenderY))
                elif self.player.facing == 'Right':
                    self.screen.blit(playerRightTexture, (playerRenderX, playerRenderY))
                else:
                    self.screen.blit(playerDownTexture, (playerRenderX, playerRenderY))
                
                #Render GUI
                if heldItemChanged:
                    guiGame_surface = createGameGUI(self.player.hotbar[self.player.heldItem])

                self.screen.blit(guiGame_surface, (0,0))
                
                #Coin balance display
                self.screen.blit(self.font4.render(f'{self.player.purseBalance}', True, 'white'), (90,35))
                
                #Render diagnostic graphics
                if renderDiagnostics:
                    self.screen.blit(self.font3.render(f'Moving Direction: {movingDirection}', True, 'black'), (50,660))
                    self.screen.blit(self.font3.render(f'Facing Direction: {self.player.facing}', True, 'black'), (50,690))
                    renderButton(colourDict['Light Grey'], [130, 600, 25, 25], 'w')
                    renderButton(colourDict['Light Grey'], [100, 630, 25, 25], 'a')
                    renderButton(colourDict['Light Grey'], [130, 630, 25, 25], 's')
                    renderButton(colourDict['Light Grey'], [160, 630, 25, 25], 'd')
                    self.screen.blit(self.font3.render(f'Player X Position: {self.player.x}', True, 'black'), (50,550))
                    self.screen.blit(self.font3.render(f'Player Y Position: {self.player.y}', True, 'black'), (50,580))
                    self.screen.blit(self.font3.render(f'Held Item: {self.player.hotbar[self.player.heldItem]}', True, 'black'), (50,500))
                    self.screen.blit(self.font1.render(f'Time: {ingameTime}', True, 'black'), (50,450))
                    self.screen.blit(self.font3.render(f'Mouse X Grid: {mouseXGridPos}', True, 'black'), (50,400))
                    self.screen.blit(self.font3.render(f'Mouse Y Grid: {mouseYGridPos}', True, 'black'), (50,425))
                    self.screen.blit(self.font3.render(f'Looking at Block ID: {tilemapBase[mouseXGridPos, mouseYGridPos]}', True, 'black'), (50,375))
                    

                    renderTileColour(self.player.x - 10, self.player.y - 6, 'white')
                    renderTileColour(self.player.x - 10, self.player.y + 5, 'white')
                    renderTileColour(self.player.x + 10, self.player.y - 6, 'white')
                    renderTileColour(self.player.x + 10, self.player.y + 5, 'white')
                    
            
            elif currentScreen in screenDict:
                self.screen.blit(screenDict[currentScreen], (0,0))

            if currentScreen == 'Inventory':
                self.screen.blit(self.font1.render(f'Carrots: {self.player.inventory["Carrot"]}', True, 'black'), (180,200))
                self.screen.blit(self.font1.render(f'Potatoes: {self.player.inventory["Potato"]}', True, 'black'), (180,250))
                self.screen.blit(self.font1.render(f'Wheat: {self.player.inventory["Wheat"]}', True, 'black'), (180,300))
                self.screen.blit(self.font1.render(f'Beetroots: {self.player.inventory["Beetroot"]}', True, 'black'), (180,350))
                self.screen.blit(self.font1.render(f'Melons: {self.player.inventory["Melon"]}', True, 'black'), (180,400))
                self.screen.blit(self.font1.render(f'Bamboo: {self.player.inventory["Bamboo"]}', True, 'black'), (180,450))
                self.screen.blit(self.font1.render(f'Cherries: {self.player.inventory["Cherry"]}', True, 'black'), (180,500))
                self.screen.blit(self.font1.render(f'Apples: {self.player.inventory["Apple"]}', True, 'black'), (180,550))
                
            if (currentScreen in screenDict) and (currentScreen != 'Guide') and (currentScreen != 'Menu') and (currentScreen != 'Inventory'):
                self.screen.blit(self.font4.render(f'{self.player.purseBalance}', True, 'white'), (1030,85))
                
            pygame.display.update()

            mapEdited = False
            heldItemChanged = False
            currentScreenChanged = False
            playerMoved = not ((prevXpos == self.player.x) and (prevYpos == self.player.y))
            
            ingameTime += self.clock.get_time()
            self.clock.tick(60)  # limits FPS to 60
        
        pygame.quit()

gameInstance = Game()
gameInstance.reset()
gameInstance.run()