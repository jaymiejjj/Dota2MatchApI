from GetMatchDetails import GetMatchDetails

#def GetPlayerPerformance(account_id):
#    break

def GetOneMatchPerformance(match_id):
    dict = GetMatchDetails(match_id)
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

    '''for i in dict:

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
        #print(data)'''


GetOneMatchPerformance(2569610900)

