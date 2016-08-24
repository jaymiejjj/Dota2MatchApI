import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
def GetMatchDetails(match_id):
    r = requests.get('http://www.dotabuff.com/matches/{}'.format(match_id),headers=headers)
    soup = BeautifulSoup(r.text,'lxml')
    account_ids = soup.select('a.link-type-player')
    nicks = soup.select('a.link-type-player')
    kills = soup.select('div.team-results tbody > tr > td:nth-of-type(5)')
    deaths = soup.select('div.team-results tbody > tr > td:nth-of-type(6)')
    assists = soup.select('div.team-results tbody > tr > td:nth-of-type(7)')

    datalist = []
    for account_id,nick,kill,death,assist in zip(account_ids,nicks,kills,deaths,assists):
        data = {
            'account_id' : account_id.get('href').split('/')[2],
            'nick'       : nick.text,
            'kills'      : 0 if kill.text == '-' else int(kill.text),
            'deaths'     : 0 if death.text == '-' else int(death.text),
            'assists'    : 0 if assist.text == '-' else int(assist.text),
        }
        datalist.append(data)

    return datalist





    '''r = requests.get('http://api.steampowered.com/IDOTA2Match_570/GetMatchDetails/v1?key=3EB124BC8F8A4E77269DCE8D2487C935&match_id={}'.format(match_id))
    return r.json()['result']['players']'''





