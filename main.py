from GetFivePlayers import GetFivePlayers
from GetPlayerPerformance import GetRecentlyPerformance, GetPlayerPrice
from GetTeammates import GetTeammateName


teamlist = [15,2512249]

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
