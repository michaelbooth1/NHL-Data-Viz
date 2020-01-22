import numpy as np
import matplotlib.pyplot as plt
from ShotLocator import getCoords, shotLocator
from PlayerHistory import playerHistory,gameLogIDs

def getShotByType(shotLog, type):
    xCoords = []
    yCoords = []
    for shot in shotLog:
        if(shot[2] == type):
            xCoords.append(shot[0])
            yCoords.append(shot[1])
    return [xCoords,yCoords]

shotList = getCoords(shotLocator(gameLogIDs(playerHistory("Williams", 2019)), "Justin Williams"))

im = plt.imread('nhlRink.png')
plt.imshow(im, extent=[0,100,-42.5,42.5])

shots = getShotByType(shotList, "SHOT")
goals = getShotByType(shotList, "GOAL")
blocked = getShotByType(shotList, "BLOCKED_SHOT")
missed = getShotByType(shotList, "MISSED_SHOT")

plt.scatter(shots[0], shots[1], color="blue")
plt.scatter(goals[0], goals[1], color="red")
plt.scatter(blocked[0], blocked[1], color="purple")
plt.scatter(missed[0], missed[1], color="black")
plt.savefig('shotmap.png', dpi=600)

