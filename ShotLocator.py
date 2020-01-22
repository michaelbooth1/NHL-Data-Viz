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
            if play["result"]["eventTypeId"] in ["SHOT","GOAL","BLOCKED_SHOT","MISSED_SHOT"]:
                if play["players"][0]['player']['fullName'].lower() == playerName.lower():
                    shotData.append(play)
                elif len(play["players"]) > 1:
                    if play["players"][1]['player']['fullName'].lower() == playerName.lower():
                        shotData.append(play)

        return shotData

def getCoords(shotData):
    shotList = []
    for shot in shotData:
        if(shot['coordinates']['x'] < 0):
            shotList.append((abs(shot['coordinates']['x']), shot['coordinates']['y'] * (-1),shot["result"]["eventTypeId"]))
        else:
            shotList.append((shot['coordinates']['x'],shot['coordinates']['y'],shot["result"]["eventTypeId"]))

    return shotList



