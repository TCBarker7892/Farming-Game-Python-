import contextlib
with contextlib.redirect_stdout(None):
    import pygame

screenChangeDictionary = {
    'Game' : {
        pygame.K_e : 'Inventory',
        pygame.K_ESCAPE : 'Menu',
        pygame.K_q : 'Shop',
    },
    'Inventory' : {
        pygame.K_e : 'Game',
        pygame.K_ESCAPE : 'Game',
    },
    'Shop' : {
        pygame.K_ESCAPE : 'Game',
        pygame.K_q : 'Game',
    },
    'Carrot_ShopUnlocked' : {
        pygame.K_ESCAPE : 'Shop',
    },
    'Potato_ShopUnlocked' : {
        pygame.K_ESCAPE : 'Shop',
    },
    'Wheat_ShopUnlocked' : {
        pygame.K_ESCAPE : 'Shop',
    },
    'Beetroot_ShopUnlocked' : {
        pygame.K_ESCAPE : 'Shop',
    },
    'Melon_ShopUnlocked' : {
        pygame.K_ESCAPE : 'Shop',
    },
    'Bamboo_ShopUnlocked' : {
        pygame.K_ESCAPE : 'Shop',
    },
    'Cherry_ShopUnlocked' : {
        pygame.K_ESCAPE : 'Shop',
    },
    'Apple_ShopUnlocked' : {
        pygame.K_ESCAPE : 'Shop',
    },
    'Chicken_ShopUnlocked' : {
        pygame.K_ESCAPE : 'Shop',
    },
    'Goat_ShopUnlocked' : {
        pygame.K_ESCAPE : 'Shop',
    },
    'Sheep_ShopUnlocked' : {
        pygame.K_ESCAPE : 'Shop',
    },
    'Cow_ShopUnlocked' : {
        pygame.K_ESCAPE : 'Shop',
    },
    'Fence_ShopUnlocked' : {
        pygame.K_ESCAPE : 'Shop',
    },
    'Sign_ShopUnlocked' : {
        pygame.K_ESCAPE : 'Shop',
    },
    'StonePath_ShopUnlocked' : {
        pygame.K_ESCAPE : 'Shop',
    },
    'Carrot_ShopLocked' : {
        pygame.K_ESCAPE : 'Shop',
    },
    'Potato_ShopLocked' : {
        pygame.K_ESCAPE : 'Shop',
    },
    'Wheat_ShopLocked' : {
        pygame.K_ESCAPE : 'Shop',
    },
    'Beetroot_ShopLocked' : {
        pygame.K_ESCAPE : 'Shop',
    },
    'Melon_ShopLocked' : {
        pygame.K_ESCAPE : 'Shop',
    },
    'Bamboo_ShopLocked' : {
        pygame.K_ESCAPE : 'Shop',
    },
    'Cherry_ShopLocked' : {
        pygame.K_ESCAPE : 'Shop',
    },
    'Apple_ShopLocked' : {
        pygame.K_ESCAPE : 'Shop',
    },
    'Chicken_ShopLocked' : {
        pygame.K_ESCAPE : 'Shop',
    },
    'Goat_ShopLocked' : {
        pygame.K_ESCAPE : 'Shop',
    },
    'Sheep_ShopLocked' : {
        pygame.K_ESCAPE : 'Shop',
    },
    'Cow_ShopLocked' : {
        pygame.K_ESCAPE : 'Shop',
    },
    'Fence_ShopLocked' : {
        pygame.K_ESCAPE : 'Shop',
    },
    'Sign_ShopLocked' : {
        pygame.K_ESCAPE : 'Shop',
    },
    'Stone Path_ShopLocked' : {
        pygame.K_ESCAPE : 'Shop',
    },
    'Menu' : {
        pygame.K_ESCAPE : 'Game',
    },
    'Settings' : {
        pygame.K_ESCAPE : 'Menu',
    },
    'Controls' : {
        pygame.K_ESCAPE : 'Menu',
    },
    'Stats' : {
        pygame.K_ESCAPE : 'Menu',
    },
    'Guide' : {
        pygame.K_ESCAPE : 'Menu',
    },
    'Title' : {},
}

def screenChangeHandling(keyPressed, current_screen):
    screenChangedBool = False

    if current_screen in screenChangeDictionary:
        currentScreenDictionary = screenChangeDictionary[current_screen]
        if keyPressed in currentScreenDictionary:
            current_screen = currentScreenDictionary[keyPressed]
            screenChangedBool = True

    return current_screen, screenChangedBool

navigationButtons = {
    'Game' : {
        (1155, 1255, 145, 245) : 'Shop',
        (1155, 1255, 25, 125) : 'Menu',
    },
    'Inventory' : {
        (80, 160, 80, 160) : 'Game',                            
    },
    'Shop' : {
        (80, 160, 80, 160) : 'Game',
        (100, 200, 280, 380) : 'Carrot_Shop@',
        (220, 320, 280, 380) : 'Potato_Shop@',
        (100, 200, 400, 500) : 'Wheat_Shop@',
        (220, 320, 400, 500) : 'Beetroot_Shop@',
        (100, 200, 520, 620) : 'Melon_Shop@',
        (220, 320, 520, 620) : 'Bamboo_Shop@',
        (385, 485, 280, 380) : 'Cherry_Shop@',
        (505, 605, 280, 380) : 'Apple_Shop@',
        (670, 770, 280, 380) : 'Chicken_Shop@',
        (790, 890, 280, 380) : 'Goat_Shop@',
        (670, 770, 400, 500) : 'Sheep_Shop@',
        (790, 890, 400, 500) : 'Cow_Shop@',
        (955, 1055, 280, 380) : 'Fence_Shop@',
        (1075, 1175, 280, 380) : 'Sign_Shop@',
        (955, 1055, 400, 500) : 'Stone Path_Shop@',
    },
    'Carrot_ShopUnlocked' : {
        (80, 160, 80, 160) : 'Shop',
    },
    'Potato_ShopUnlocked' : {
        (80, 160, 80, 160) : 'Shop',
    },
    'Wheat_ShopUnlocked' : {
        (80, 160, 80, 160) : 'Shop',
    },
    'Beetroot_ShopUnlocked' : {
        (80, 160, 80, 160) : 'Shop',
    },
    'Melon_ShopUnlocked' : {
        (80, 160, 80, 160) : 'Shop',
    },
    'Bamboo_ShopUnlocked' : {
        (80, 160, 80, 160) : 'Shop',
    },
    'Cherry_ShopUnlocked' : {
        (80, 160, 80, 160) : 'Shop',
    },
    'Apple_ShopUnlocked' : {
        (80, 160, 80, 160) : 'Shop',
    },
    'Chicken_ShopUnlocked' : {
        (80, 160, 80, 160) : 'Shop',
    },
    'Goat_ShopUnlocked' : {
        (80, 160, 80, 160) : 'Shop',
    },
    'Sheep_ShopUnlocked' : {
        (80, 160, 80, 160) : 'Shop',
    },
    'Cow_ShopUnlocked' : {
        (80, 160, 80, 160) : 'Shop',
    },
    'Fence_ShopUnlocked' : {
        (80, 160, 80, 160) : 'Shop',
    },
    'Sign_ShopUnlocked' : {
        (80, 160, 80, 160) : 'Shop',
    },
    'Stone Path_ShopUnlocked' : {
        (80, 160, 80, 160) : 'Shop',
    },
    'Carrot_ShopLocked' : {
        (80, 160, 80, 160) : 'Shop',
    },
    'Potato_ShopLocked' : {
        (80, 160, 80, 160) : 'Shop',
    },
    'Wheat_ShopLocked' : {
        (80, 160, 80, 160) : 'Shop',
    },
    'Beetroot_ShopLocked' : {
        (80, 160, 80, 160) : 'Shop',
    },
    'Melon_ShopLocked' : {
        (80, 160, 80, 160) : 'Shop',
    },
    'Bamboo_ShopLocked' : {
        (80, 160, 80, 160) : 'Shop',
    },
    'Cherry_ShopLocked' : {
        (80, 160, 80, 160) : 'Shop',
    },
    'Apple_ShopLocked' : {
        (80, 160, 80, 160) : 'Shop',
    },
    'Chicken_ShopLocked' : {
        (80, 160, 80, 160) : 'Shop',
    },
    'Goat_ShopLocked' : {
        (80, 160, 80, 160) : 'Shop',
    },
    'Sheep_ShopLocked' : {
        (80, 160, 80, 160) : 'Shop',
    },
    'Cow_ShopLocked' : {
        (80, 160, 80, 160) : 'Shop',
    },
    'Fence_ShopLocked' : {
        (80, 160, 80, 160) : 'Shop',
    },
    'Sign_ShopLocked' : {
        (80, 160, 80, 160) : 'Shop',
    },
    'Stone Path_ShopLocked' : {
        (80, 160, 80, 160) : 'Shop',
    },
    'Menu' : {
        (80, 160, 80, 160) : 'Game',
        (80, 880, 180, 280) : 'Settings',
        (80, 880, 300, 400) : 'Controls',
        (80, 880, 420, 520) : 'Stats',
        (80, 880, 540, 640) : 'Guide',
    },
    'Settings' : {
        (80, 160, 80, 160) : 'Menu',
    },
    'Controls' : {
        (80, 160, 80, 160) : 'Menu',
    },
    'Stats' : {
        (80, 160, 80, 160) : 'Menu',
    },
    'Guide' : {
        (80, 160, 80, 160) : 'Menu',
    },
    'Title' : {},    
}

def navigationButtonHandling(clickXpos, clickYpos, current_screen):
    buttonPressSuccess = False
    newScreen = None

    if current_screen in navigationButtons:
        currentScreenButtons = navigationButtons[current_screen]
        for buttonLocation, destScreen in currentScreenButtons.items():
            if (buttonLocation[0] < clickXpos < buttonLocation[1]) and (buttonLocation[2] < clickYpos < buttonLocation[3]):
                newScreen = destScreen
                buttonPressSuccess = True
                break

    return buttonPressSuccess, newScreen

hotbarButtons = {
    (350, 450, 590, 690) : 0,
    (470, 570, 590, 690) : 1,
    (590, 690, 590, 690) : 2,
    (710, 810, 590, 690) : 3,
    (830, 930, 590, 690) : 4,
}

def hotbarButtonHandling(clickXpos, clickYpos, currentSlot):
    itemChangedBool = False
    newSlot = currentSlot

    for buttonLocation, hotbarSlot in hotbarButtons.items():
            if (buttonLocation[0] < clickXpos < buttonLocation[1]) and (buttonLocation[2] < clickYpos < buttonLocation[3]):
                newSlot = hotbarSlot
                itemChangedBool = True
                break

    return newSlot, itemChangedBool

shopActionButtons = {
    'Carrot_ShopUnlocked' : {
        (750, 965, 520, 640) : ['buy', 'Carrot Seed'],
        (985, 1200, 520, 640) : ['sell', 'Carrot'],
    },
    'Potato_ShopUnlocked' : {
        (750, 965, 520, 640) : ['buy', 'Seed Potato'],
        (985, 1200, 520, 640) : ['sell', 'Potato'],
    },
    'Wheat_ShopUnlocked' : {
        (750, 965, 520, 640) : ['buy', 'Wheat Seed'],
        (985, 1200, 520, 640) : ['sell', 'Wheat'],
    },
    'Beetroot_ShopUnlocked' : {
        (750, 965, 520, 640) : ['buy', 'Beetroot Seed'],
        (985, 1200, 520, 640) : ['sell', 'Beetroot'],
    },
    'Melon_ShopUnlocked' : {
        (750, 965, 520, 640) : ['buy', 'Melon Seed'],
        (985, 1200, 520, 640) : ['sell', 'Melon'],
    },
    'Bamboo_ShopUnlocked' : {
        (750, 965, 520, 640) : ['buy', 'Bamboo Sprout'],
        (985, 1200, 520, 640) : ['sell', 'Bamboo'],
    },
    'Cherry_ShopUnlocked' : {},
    'Apple_ShopUnlocked' : {},
    'Chicken_ShopUnlocked' : {},
    'Goat_ShopUnlocked' : {},
    'Sheep_ShopUnlocked' : {},
    'Cow_ShopUnlocked' : {},
    'Fence_ShopUnlocked' : {},
    'Sign_ShopUnlocked' : {},
    'Stone Path_ShopUnlocked' : {},
    'Carrot_ShopLocked' : {
        (750, 1200, 520, 640) : ['unlock', 'Carrot'],
    },
    'Potato_ShopLocked' : {
        (750, 1200, 520, 640) : ['unlock', 'Potato'],
    },
    'Wheat_ShopLocked' : {
        (750, 1200, 520, 640) : ['unlock', 'Wheat'],
    },
    'Beetroot_ShopLocked' : {
        (750, 1200, 520, 640) : ['unlock', 'Beetroot'],
    },
    'Melon_ShopLocked' : {
        (750, 1200, 520, 640) : ['unlock', 'Melon'],
    },
    'Bamboo_ShopLocked' : {
        (750, 1200, 520, 640) : ['unlock', 'Bamboo'],
    },
    'Cherry_ShopLocked' : {},
    'Apple_ShopLocked' : {},
    'Chicken_ShopLocked' : {},
    'Goat_ShopLocked' : {},
    'Sheep_ShopLocked' : {},
    'Cow_ShopLocked' : {},
    'Fence_ShopLocked' : {},
    'Sign_ShopLocked' : {},
    'Stone Path_ShopLocked' : {},
}

def shopActionButtonHandling(clickXpos, clickYpos, current_screen):
    buttonPressed = False
    item = operation = None

    if current_screen in shopActionButtons:
        actionDict = shopActionButtons[current_screen]
        for buttonLocation, actionPair in actionDict.items():
            if (buttonLocation[0] < clickXpos < buttonLocation[1]) and (buttonLocation[2] < clickYpos < buttonLocation[3]):

                operation, item = actionPair

                buttonPressed = True
                break

    return buttonPressed, operation, item