import pymongo

client = pymongo.MongoClient('localhost',27017)
Dota2Data = client['Dota2Data']
TeamRank = Dota2Data['TeamRank']

def GetTeamRank(team_id):
    for i in TeamRank.find({'team_id':str(team_id)}):
        return i['place']






