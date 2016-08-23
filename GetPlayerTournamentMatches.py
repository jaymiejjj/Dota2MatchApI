from bs4 import BeautifulSoup
import requests

def GetPlayerTournamentMatches(account_id):
    r = requests.get('http://dotamax.com/player/match/{}/?skill=pro'.format(account_id))
    soup = BeautifulSoup(r.text, 'lxml')
    match_ids = soup.select('tbody.table-player-detail > tr > td:nth-of-type(2) > a')
    match_list = []
    for match_id in match_ids:
        match_list.append(match_id.get('href').split('/')[3])
    return match_list[0:10]
