from urllib import request
import json
from FindPlayer import findPlayer

BASE_URL = 'https://statsapi.web.nhl.com/api/v1/'
ENDPOINT = 'people/'
GAMELOG_MOD = '/stats?stats=gameLog&season='

def playerHistory(name, year):
    data = request.urlopen(BASE_URL + ENDPOINT + str(findPlayer(name)) + GAMELOG_MOD + str(year) + str(year + 1))
    response = json.loads(data.read().decode('utf-8'))
    return response['stats'][0]['splits']

def playerShotLog(gameLog):
    shotLog = []
    for game in gameLog:
        shotLog.append(game['stat']['shots'])
    return shotLog

def gameLogIDs(gameLog):
    gameIds = []
    for game in gameLog:
        gameIds.append(game['game']['gamePk'])
    return gameIds