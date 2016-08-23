from bs4 import BeautifulSoup
import requests

def GetPlayerTournamentMatches(account_id):
    r = requests.get('http://dotamax.com/player/match/{}/?skill=pro'.format(account_id))
    soup = BeautifulSoup(r.text, 'lxml')
    match_ids = soup.select('tbody.table-player-detail > tr > td > a')
    match_list = []
    for match_id in match_ids:
        print(match_id.get('href'))

GetPlayerTournamentMatches(101525357)
