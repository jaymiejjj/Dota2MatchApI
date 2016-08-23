from bs4 import BeautifulSoup
import requests
from GetTeammates import GetTeammates

def GetFivePlayers(team_id):
    r = requests.get('http://dotamax.com/match/tour_team_players/?team_id={}'.format(team_id))
    soup = BeautifulSoup(r.text,'lxml')

    list = []
    for index in range(0,10):
        if soup.select('#matchrow_{} a'.format(index)) != []:
            tuple = (soup.select('#matchrow_{} > td:nth-of-type(2)'.format(index))[0].text,soup.select('#matchrow_{} a'.format(index))[0].get('href').split('/')[3])
            list.append(tuple)
        else:
            continue


    accounts_list = []
    for i in GetTeammates(team_id):
        accounts_list.append(i['account_id'])

    print(accounts_list)

    fivePlayerslist = []
    for accounts in sorted(list, reverse=True):
        while len(fivePlayerslist) < 5:
            if accounts[1] in accounts_list:
                fivePlayerslist.append(accounts[1])
            else:
                continue
    return(fivePlayerslist)

