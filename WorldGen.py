import numpy as np
import contextlib
with contextlib.redirect_stdout(None):
    import pygame

def newWorld(xSize, ySize):
    baseTilemap = np.zeros((ySize, xSize))
    for i in range(ySize):
        for j in range(xSize):
            tempVal = np.random.rand()
            if tempVal < 0.02:
                baseTilemap[i,j] = 3
            elif tempVal > 0.75:
                baseTilemap[i,j] = 2
            else:
                baseTilemap[i,j] = 1

    
    for i in range(14,66):
        baseTilemap[i, 14] = 0
    for i in range(14,40):
        baseTilemap[30, i] = 0
    

    detailTilemap = np.zeros((xSize, ySize))
    detailTilemap[16,16] = 3
    detailTilemap[33,17] = 3
    
    for i in range(0,10):
        for j in range(xSize):
            detailTilemap[i,j] = 1
            detailTilemap[ySize-i-1,j] = 1
    for i in range(0,10):
        for j in range(ySize):
            detailTilemap[j,i] = 1
            detailTilemap[j,xSize-i-1] = 1


    return baseTilemap, detailTilemap