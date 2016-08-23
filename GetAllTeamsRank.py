import requests
from bs4 import BeautifulSoup
import pymongo

client = pymongo.MongoClient('localhost',27017)
Dota2Data = client['Dota2Data']
TeamRank = Dota2Data['TeamRank']

def GetAllTeamsRank():
    for page in range(1,6):
        r = requests.get('http://dotamax.com/match/tour_famous_team_list/?league_id=&skill=&ladder=&p={}'.format(page))
        soup = BeautifulSoup(r.text, 'lxml')
        for index in range(1,21):
            if soup.select('#matchrow_{} > td:nth-of-type(1)'.format(index)) != []:
                data = {
                    'place' : soup.select('#matchrow_{} > td:nth-of-type(1)'.format(index))[0].text,
                    'team_id' : soup.select('#matchrow_{}'.format(index))[0].get('onclick').split('=')[1].split("'")[0],
                    'name'  : soup.select('#matchrow_{} > td.table-title-font'.format(index))[0].get_text().strip()
                }
                print(data)
                TeamRank.insert_one(data)

            else:
                continue

GetAllTeamsRank()
