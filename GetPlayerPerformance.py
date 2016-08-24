from GetMatchDetails import GetMatchDetails
from GetPlayerTournamentMatches import GetPlayerTournamentMatches
from GetTeamRank import GetTeamRank

def GetOneMatchPerformance(match_id,account_id):
    dict = GetMatchDetails(match_id)
    for i in dict:
        if i['account_id'] != str(account_id):
            continue
        else:
            score = i['kills']*2+i['deaths']*(-1)+i['assists']*1.6
            return score

def GetRecentlyPerformance(account_id):
    matchlist = GetPlayerTournamentMatches(account_id)
    total_score = 0
    for match_id in matchlist:
        score = GetOneMatchPerformance(match_id, account_id)
        total_score = total_score + score
    recent_score = round(total_score/5, 1)
    return recent_score

def GetPlayerPrice(account_id, team_id):
    recent_score = GetRecentlyPerformance(account_id)
    rank = int(GetTeamRank(team_id))
    if rank > 0 and rank <= 3:
        price = recent_score*100*(1.2)
    elif rank >3 and rank <= 10:
        price = recent_score*100*(1.1)
    elif rank > 10 and rank <= 20:
        price = recent_score*100*(1)
    else:
        price = recent_score*100*(0.8)
    return price

'''
    total_Radiant_hero_damage = 0
    total_Dire_hero_damage = 0
    total_Radiant_Death = 0
    total_Dire_Death = 0
    total_Radiant_last_hit = 0
    total_Dire_last_hit =0
    total_Radiant_XPM = 0
    total_Dire_XPM = 0
    total_Radiant_GPM = 0
    total_Dire_GPM = 0



    for i in dict:
        if int(i['player_slot']) < 128:
            total_Radiant_hero_damage = total_Radiant_hero_damage + i['hero_damage']
            total_Radiant_Death = total_Radiant_Death +i['deaths']
            total_Radiant_last_hit = total_Radiant_last_hit + i['last_hits']
            total_Radiant_XPM = total_Radiant_XPM + i['xp_per_min']
            total_Radiant_GPM = total_Radiant_GPM + i['gold_per_min']

        else:
            total_Dire_hero_damage = total_Dire_hero_damage + i['hero_damage']
            total_Dire_Death = total_Dire_Death +i['deaths']
            total_Dire_last_hit = total_Dire_last_hit + i['last_hits']
            total_Dire_XPM = total_Dire_XPM + i['xp_per_min']
            total_Dire_GPM = total_Dire_GPM + i['gold_per_min']

    average_Radiant_Death =  total_Radiant_Death/5
    average_Dire_Death =  total_Dire_Death/5
    average_Radiant_last_hit = total_Radiant_last_hit / 5
    average_Dire_last_hit = total_Dire_last_hit / 5
    average_Radiant_XPM = total_Radiant_XPM / 5
    average_Dire_XPM = total_Dire_XPM / 5
    average_Radiant_GPM = total_Radiant_GPM / 5
    average_Dire_GPM = total_Dire_GPM / 5

    for i in dict:
        data = {
            'camp': 'Radiant' if int(i['player_slot']) < 128 else 'Dire',
            'account_id': i['account_id'],
            'f': i['kills']*2+i['deaths']*(-1)+i['assists']*1.6
        }
        print(data)


    for i in dict:
        if int(i['player_slot']) < 128:
            f = (i['hero_damage']/total_Radiant_hero_damage)/i['gold_per_min']
        else:
            f = (i['hero_damage']/total_Dire_hero_damage)/i['gold_per_min']


        data = {
            'camp': 'Radiant' if int(i['player_slot']) < 128 else 'Dire',
            'account_id': i['account_id'],
            'f': f*1000
        }
        print(data)


    for i in dict:
        if int(i['player_slot']) < 128:
            f = 4*(i['last_hits']/average_Radiant_last_hit)+10*i['hero_damage']/total_Radiant_hero_damage-1.5*i['deaths']/average_Radiant_Death+10*i['gold_per_min']/average_Radiant_GPM+2*i['xp_per_min']/average_Radiant_XPM

        else:
            f = 4*(i['last_hits']/average_Dire_last_hit)+10*i['hero_damage']/total_Dire_hero_damage-1.5*i['deaths']/average_Dire_Death+10*i['gold_per_min']/average_Dire_GPM+2*i['xp_per_min']/average_Dire_XPM

        data = {
            'camp': 'Radiant' if int(i['player_slot']) < 128 else 'Dire',
            'account_id': i['account_id'],
            'f': f
        }
        print(data)

    for i in dict:

        data = {
            'camp': 'Radiant' if int(i['player_slot']) < 128 else 'Dire',
            'account_id':i['account_id'],
            'death':i['deaths'],
            'GPM':i['gold_per_min'],
            'XPM':i['xp_per_min'],
            'last_hit':i['last_hits'],
            'hero_damage':i['hero_damage'],
            'hero_damage_rate': format(i['hero_damage']/total_Radiant_hero_damage,'.1%') if int(i['player_slot']) < 128 else format(i['hero_damage']/total_Dire_hero_damage,'.1%')
        }
        print(data)'''

