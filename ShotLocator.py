from urllib import request
import json

BASE_URL = 'https://statsapi.web.nhl.com/api/v1/game/'
ENDPOINT = '/feed/live'

def shotLocator(gameIdList, playerName):
    for gameId in gameIdList:
        data = request.urlopen(BASE_URL + str(gameId) + ENDPOINT)
        fullGameFeed = json.loads(data.read().decode('utf-8'))
        liveData = fullGameFeed["liveData"]

        shotData = []
        for play in liveData["plays"]["allPlays"]:
            if play["result"]["eventTypeId"] in ["SHOT","GOAL"] and play["players"][0]['player']['fullName'].lower() == playerName.lower():
               shotData.append(play)

        return shotData

def getCoords(shotData):
    coordsListX = []
    coordsListY = []
    for shot in shotData:
        coordsListX.append(shot['coordinates']['x'])
        coordsListY.append(shot['coordinates']['y'])

    return coordsListX,coordsListY



