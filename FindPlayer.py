from urllib import request
import json

BASE_URL = 'https://statsapi.web.nhl.com/api/v1/'
ENDPOINT = 'teams/'
ROSTER_MODIFIER = '?expand=team.roster'


def findPlayer(name):
    for ID in range(1,102):
        rosterData = request.urlopen(BASE_URL + ENDPOINT + str(ID) + ROSTER_MODIFIER)
        response = json.loads(rosterData.read().decode('utf-8'))
        if('roster' in response['teams'][0].keys()):
            for player in response['teams'][0]['roster']['roster']:
                playerName = (player['person']['fullName'])
                playerID = (player['person']['id'])
                if name.lower() in playerName.lower():
                    return playerID

    return -1

print(findPlayer("Jack Hughes"))
