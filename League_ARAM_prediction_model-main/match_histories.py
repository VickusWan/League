# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 23:50:27 2023

@author: Victor
"""

import league_data
import datetime
import time


def main():
    # vickus1 puuid -> starting point
    my_puuid = 'y5cvkCjUQdFfwAUfBdmMFcoCAYsk96GwenHJGiTUUYrygYejQSLLaP3HkrEJVDK_sP8EOnWtJe8lDg'
    
    # get vickus1 latest match history
    latest_match = league_data.get_matchIDs(my_puuid, 1)[0]
        
    list_participants = league_data.get_participants(latest_match)
    
    print(list_participants)
    
    
def my_games():
    
    my_puuid = 'y5cvkCjUQdFfwAUfBdmMFcoCAYsk96GwenHJGiTUUYrygYejQSLLaP3HkrEJVDK_sP8EOnWtJe8lDg'
    url = '/lol/match/v5/matches/by-puuid/{puuid}/ids'.format(puuid = my_puuid)
    data = league_data.fetch(url, '')
    
    #https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/y5cvkCjUQdFfwAUfBdmMFcoCAYsk96GwenHJGiTUUYrygYejQS
    #LLaP3HkrEJVDK_sP8EOnWtJe8lDg/ids?start=500&count=100

if __name__ == "__main__":
    #main()
    
    # vickus1 puuid -> starting point
    #my_puuid = 'y5cvkCjUQdFfwAUfBdmMFcoCAYsk96GwenHJGiTUUYrygYejQSLLaP3HkrEJVDK_sP8EOnWtJe8lDg'
    
    # # get vickus1 latest match history
    #latest_match = league_data.get_matchIDs(my_puuid, 1)[0]
        
    # list_participants = league_data.get_participants(latest_match)
    
    # print(list_participants)
    
    # a = league_data.get_match_data(latest_match)
    
    # t = a['info']['gameCreation']
    
    # date = datetime.datetime.fromtimestamp()
    # print(date)
    
    qweqwe = league_data.get_full_matchHistory('Vickus1')
    
    

    
    
    # start = 0
    # num = 10
    
    # match_ids = []
    
    # while True:
        
        
    #     url = '/lol/match/v5/matches/by-puuid/{puuid}/ids?start={start}&count={count}'.format(puuid = my_puuid, start = start, count = num)
    #     data = league_data.fetch(url, '')
    #     time.sleep(3)
        
    #     if len(data) == num:
            
    #         for i in data:
            
    #             if league_data.is_ARAM(i) == True:
                    
                    
    #                 match_ids.append(i)
                
    #             time.sleep(3)
    #     else:
    #         break
        
    #     start += num
    
    
    
    