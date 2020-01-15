import numpy as np
import matplotlib.pyplot as plt
from ShotLocator import getCoords, shotLocator
from PlayerHistory import playerHistory,gameLogIDs

x,y = getCoords(shotLocator(gameLogIDs(playerHistory("Marner", 2019)), "Mitchell Marner"))

im = plt.imread('nhlRink.png')
plt.imshow(im, extent=[0,100,-42.5,42.5])

plt.scatter(x,y)
plt.savefig('shotmap.png', dpi=600)

