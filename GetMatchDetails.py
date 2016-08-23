import requests
from bs4 import BeautifulSoup

def GetMatchDetails(match_id):
    r = requests.get('http://api.steampowered.com/IDOTA2Match_570/GetMatchDetails/v1?key=3EB124BC8F8A4E77269DCE8D2487C935&match_id={}'.format(match_id))
    print(r.json()['result']['players'])

GetMatchDetails(2589157420)