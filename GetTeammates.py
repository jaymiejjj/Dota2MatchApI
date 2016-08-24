from bs4 import BeautifulSoup
import requests

def GetTeammates(team_id):
    r = requests.get('http://dotamax.com/match/tour_team_detail/?team_id={}'.format(team_id))
    soup = BeautifulSoup(r.text,'lxml')
    account_ids = soup.select('div.new-box > div > a')
    imgs = soup.select('img.match-avatars-img')
    names = soup.select('div.overflow-text')
    list = []

    for account_id, img, name in zip(account_ids, imgs, names):
        data = {
            'account_id' : account_id.get('href').split('/')[3],
            'img' : img.get('src'),
            'name': name.get_text().rstrip()
            }
        list.append(data)
    return(list)

def GetTeammateName(account_id,team_id):
    list = GetTeammates(team_id)
    for i in list:
        if i['account_id'] != str(account_id):
            continue
        else:
            return i['name']








