import os
import contextlib
with contextlib.redirect_stdout(None):
    import pygame

from GlobalVariables import iconFolderLocation

itemIcon_sheet = pygame.image.load(os.path.join(iconFolderLocation, 'item_sheet.png'))
tree_sheet = pygame.image.load(os.path.join(iconFolderLocation, 'tree_sheet.png'))
seed_sheet = pygame.image.load(os.path.join(iconFolderLocation, 'seed_sheet.png'))

def extractTexture(spritesheet, position, dimensions):
    texture = spritesheet.subsurface(pygame.Rect(position[0], position[1], dimensions[0], dimensions[1]))
    return texture

carrotIcon = extractTexture(itemIcon_sheet, , (16, 16))
tomatoIcon = extractTexture(itemIcon_sheet, , (16, 16))
strawberryIcon = extractTexture(itemIcon_sheet, , (16, 16))
pumpkinIcon = extractTexture(itemIcon_sheet, , (16, 16))
cornIcon = extractTexture(itemIcon_sheet, , (16, 16))
potatoIcon = extractTexture(itemIcon_sheet, , (16, 16))
watermelonIcon = extractTexture(itemIcon_sheet, , (16, 16))
radishIcon = extractTexture(itemIcon_sheet, , (16, 16))
lettuceIcon = extractTexture(itemIcon_sheet, , (16, 16))
wheatIcon = extractTexture(itemIcon_sheet, , (16, 16))
aubergineIcon = extractTexture(itemIcon_sheet, , (16, 16))

apple = extractTexture(itemIcon_sheet, , (16, 16))
avocado = extractTexture(itemIcon_sheet, , (16, 16))
cherry = extractTexture(itemIcon_sheet, , (16, 16))
orange = extractTexture(itemIcon_sheet, , (16, 16))
plum = extractTexture(itemIcon_sheet, , (16, 16))
pear = extractTexture(itemIcon_sheet, , (16, 16))
peach = extractTexture(itemIcon_sheet, , (16, 16))
lemon = extractTexture(itemIcon_sheet, , (16, 16))

