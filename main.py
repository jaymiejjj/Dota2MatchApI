from GetFivePlayers import GetFivePlayers
from GetPlayerPerformance import GetRecentlyPerformance, GetPlayerPrice
from GetTeammates import GetTeammateName
from GetMatchDetails import GetMatchDetails

def GetPlayerData(teamlist):
    for team_id in teamlist:
        playerlist = GetFivePlayers(team_id)
        for account_id in playerlist:
            performance = GetRecentlyPerformance(account_id)
            data = {
                'account_id' : account_id,
                'nick_name'  : GetTeammateName(account_id,team_id),
                'team_id'    : team_id,
                'performance': performance,
                'price'      : GetPlayerPrice(account_id, team_id)
            }
            print(data)

def GetResult(match_list):
    datalist = []
    for match_id in match_list:
        list = GetMatchDetails(match_id)
        for dict in list:
            data = {
                'account_id': dict['account_id'],
                'nick'      : dict['nick'],
                'score'     : round(dict['kills']*2+dict['deaths']*(-1)+dict['assists']*1.6, 1)
            }
            datalist.append(data)

    newdata = {}
    for data in datalist:
        if data['nick'] in newdata.keys():
            newdata[data['nick']] = newdata[data['nick']]+ [data['score']]
        else:
            newdata[data['nick']] = [data['score']]
    #print(newdata)


    for key in newdata.keys():
        newdata[key] = round(sum(newdata[key])/len(newdata[key]),1)

    d = {}
    for i in sorted(newdata.items(),key=lambda x: x[1], reverse=True):
        data = {
            'nick'  :i[0],
            'result':i[1]
        }
        print(data)


    '''for nick in newdata.keys():
        data_result = {
            'nick' : nick,
            #'score'      : newdata[nick],
            'result'     : round(sum(newdata[nick])/len(newdata[nick]),1)
        }
        print(data_result)'''


'''
Ti6胜者组第二轮
MVP     BO3  Wings  match_id = [2562521800,2562482317]
Ehome   BO3  EG     match_id = [2562582896,2562671370]

MVP(1148284) Wings(1836806)
EG(39)       Ehome(4)

'''

#teamlist = [1148284,1836806,39,4]

match_list = [2562521800, 2562482317, 2562582896, 2562671370]

#GetPlayerData(teamlist)

GetResult(match_list)

