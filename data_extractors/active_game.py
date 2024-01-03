from league_data import fetch, get_encryptedId, get_player_level

encryptedId = get_encryptedId('vickus1')

typename = '/lol/spectator/v4/active-games/by-summoner/{encryptedSummonerId}'.format(encryptedSummonerId = encryptedId)
body = 'NA1'
data = fetch(typename, body)

dic = {}
for participant in data['participants']:
    dic[participant['puuid']] = get_player_level(participant['puuid'])

# {
#     "gameId": 4870934210,
#     "mapId": 12,
#     "gameMode": "ARAM",
#     "gameType": "MATCHED_GAME",
#     "gameQueueConfigId": 450,
#     "participants": [
#         {
#             "puuid": "YVv1oIsOFAkKNOPoigfKyVKBPtQqeV4ORW0MRQ7nPg-mf66kb5wtCCxBcRdK4TJuLb3IvOpb1VUMUw",
#             "teamId": 100,
#             "spell1Id": 4,
#             "spell2Id": 32,
#             "championId": 34,
#             "profileIconId": 6330,
#             "summonerName": "MoistSandwich",
#             "bot": false,
#             "summonerId": "LC8OOyqFAJhyk1YfCysNqHXu4XbYmf7bBsXlTi5GXPVN9UqY",
#             "gameCustomizationObjects": [],
#             "perks": {
#                 "perkIds": [
#                     8112,
#                     8126,
#                     8138,
#                     8105,
#                     8014,
#                     8009,
#                     5005,
#                     5008,
#                     5003
#                 ],
#                 "perkStyle": 8100,
#                 "perkSubStyle": 8000
#             }
#         },
#         {
#             "puuid": "tbU4FxORL2yz96_vduvPdmxGRhm13RxH-2jQYuoKi5DllU5QNw5kM2H6BRyicUlT24bWyU55J2GgKQ",
#             "teamId": 100,
#             "spell1Id": 4,
#             "spell2Id": 21,
#             "championId": 134,
#             "profileIconId": 6426,
#             "summonerName": "tiac",
#             "bot": false,
#             "summonerId": "dvuk-eLLgtIvl8dhbxMkfZ8E_97e-s0I6FAbx7CXiBjNDWI",
#             "gameCustomizationObjects": [],
#             "perks": {
#                 "perkIds": [
#                     8128,
#                     8126,
#                     8138,
#                     8106,
#                     8014,
#                     8009,
#                     5008,
#                     5008,
#                     5002
#                 ],
#                 "perkStyle": 8100,
#                 "perkSubStyle": 8000
#             }
#         },
#         {
#             "puuid": "lQz74-DpZneG10B9i2csifgLaVyXJNrd0hNOFw6Np80mFBe8y12Mfagrrx23t5qM4dJSGrOOhsKe6Q",
#             "teamId": 100,
#             "spell1Id": 32,
#             "spell2Id": 4,
#             "championId": 200,
#             "profileIconId": 1296,
#             "summonerName": "Scrotiess",
#             "bot": false,
#             "summonerId": "vfDJ9tgAGAJXNMhvBax278_2pMdUg5DUPpfMELPNX7JpsO0",
#             "gameCustomizationObjects": [],
#             "perks": {
#                 "perkIds": [
#                     8008,
#                     9111,
#                     9104,
#                     8014,
#                     8139,
#                     8135,
#                     5005,
#                     5008,
#                     5002
#                 ],
#                 "perkStyle": 8000,
#                 "perkSubStyle": 8100
#             }
#         },
#         {
#             "puuid": "9_TFgL-K4m9BjbXgWdYOpqRc43LEumA8M5dtO0iE-CKJwDO1VcpoDur-J9oo9tD8NmibqaYzu0HFNQ",
#             "teamId": 100,
#             "spell1Id": 32,
#             "spell2Id": 4,
#             "championId": 234,
#             "profileIconId": 744,
#             "summonerName": "v0rvex",
#             "bot": false,
#             "summonerId": "Hi0QMZ9qLf5ACnoN4D3mXKR2hpS03imhuaDqCRGwd1QZUc4",
#             "gameCustomizationObjects": [],
#             "perks": {
#                 "perkIds": [
#                     8010,
#                     9111,
#                     9104,
#                     8014,
#                     8347,
#                     8304,
#                     5005,
#                     5008,
#                     5002
#                 ],
#                 "perkStyle": 8000,
#                 "perkSubStyle": 8300
#             }
#         },
#         {
#             "puuid": "g4uOUZd38rsJT3t6OK-c4BCoYN4-zSQdpcKpXqcRZaLsP0DlYbu_goxppqd_CqIJLDMIGleijolAuQ",
#             "teamId": 100,
#             "spell1Id": 32,
#             "spell2Id": 4,
#             "championId": 131,
#             "profileIconId": 4533,
#             "summonerName": "Álvaro",
#             "bot": false,
#             "summonerId": "QxIx79llminO9MXCWNtG55J-N-QPoqCOrsx6kK6F3o4Mfzo",
#             "gameCustomizationObjects": [],
#             "perks": {
#                 "perkIds": [
#                     8128,
#                     8143,
#                     8138,
#                     8106,
#                     8014,
#                     8009,
#                     5008,
#                     5008,
#                     5003
#                 ],
#                 "perkStyle": 8100,
#                 "perkSubStyle": 8000
#             }
#         },
#         {
#             "puuid": "Lzd8tAUzUXxALVgqD1WDnp7f8ZO3i1WLM-yg8UPrBtGYi16b6pKx3ZVlGVIDPQUbR8dGce9bn-hmsg",
#             "teamId": 200,
#             "spell1Id": 7,
#             "spell2Id": 4,
#             "championId": 21,
#             "profileIconId": 505,
#             "summonerName": "DrRockso",
#             "bot": false,
#             "summonerId": "ZN2gdwe8P9b12TomQ6mqKPvhDZC8FDyokskJ5l_vEcNm6sk",
#             "gameCustomizationObjects": [],
#             "perks": {
#                 "perkIds": [
#                     8128,
#                     8126,
#                     8138,
#                     8106,
#                     8009,
#                     8014,
#                     5008,
#                     5008,
#                     5002
#                 ],
#                 "perkStyle": 8100,
#                 "perkSubStyle": 8000
#             }
#         },
#         {
#             "puuid": "L-_YqDtlK6_P8lmPN5fwPKX8iMzXcs1LEuP-Y-UMfHTeBO03RhWRb0KRs7pOq86FSSzwILJAQqgnvQ",
#             "teamId": 200,
#             "spell1Id": 32,
#             "spell2Id": 4,
#             "championId": 111,
#             "profileIconId": 5642,
#             "summonerName": "Yumomo",
#             "bot": false,
#             "summonerId": "B2dFN-ln-FBVApcBklIytOBFs5UsdZK5ggQG-zgaVAhBv3g",
#             "gameCustomizationObjects": [],
#             "perks": {
#                 "perkIds": [
#                     8439,
#                     8401,
#                     8429,
#                     8451,
#                     8226,
#                     8210,
#                     5008,
#                     5003,
#                     5002
#                 ],
#                 "perkStyle": 8400,
#                 "perkSubStyle": 8200
#             }
#         },
#         {
#             "puuid": "3l2_xGQhVhrODJlXgIiv9cEsirrpRPxR3WNg1umVAPP25Da1F51x8EycXVb5exmTIoPwVCIh33j6Fw",
#             "teamId": 200,
#             "spell1Id": 6,
#             "spell2Id": 4,
#             "championId": 222,
#             "profileIconId": 4562,
#             "summonerName": "Royalnemo",
#             "bot": false,
#             "summonerId": "7YX8TzZ93b6d6HsAuYlIOfkAtEmfdKVKQnqF0st1bXGaG8Y",
#             "gameCustomizationObjects": [],
#             "perks": {
#                 "perkIds": [
#                     8008,
#                     8009,
#                     9103,
#                     8014,
#                     8233,
#                     8236,
#                     5005,
#                     5008,
#                     5002
#                 ],
#                 "perkStyle": 8000,
#                 "perkSubStyle": 8200
#             }
#         },
#         {
#             "puuid": "qBKmlLC5szK6dq8tGINX6I_qAJeafN6S1yz8k9_mA1_Ft9r54oEbQlRFIpiNlo5YE3wJ4HKKqwo65A",
#             "teamId": 200,
#             "spell1Id": 4,
#             "spell2Id": 32,
#             "championId": 17,
#             "profileIconId": 4793,
#             "summonerName": "DeBunteKoe",
#             "bot": false,
#             "summonerId": "VRLLvnVRl1Gltlou3gJpZ2En0ANVMzMebaAXngIkvTJ6OvU",
#             "gameCustomizationObjects": [],
#             "perks": {
#                 "perkIds": [
#                     8214,
#                     8226,
#                     8210,
#                     8237,
#                     8345,
#                     8347,
#                     5008,
#                     5008,
#                     5002
#                 ],
#                 "perkStyle": 8200,
#                 "perkSubStyle": 8300
#             }
#         },
#         {
#             "puuid": "y5cvkCjUQdFfwAUfBdmMFcoCAYsk96GwenHJGiTUUYrygYejQSLLaP3HkrEJVDK_sP8EOnWtJe8lDg",
#             "teamId": 200,
#             "spell1Id": 32,
#             "spell2Id": 4,
#             "championId": 31,
#             "profileIconId": 3379,
#             "summonerName": "Vickus1",
#             "bot": false,
#             "summonerId": "OwZb8qPwcSDADY85ensPo71XZvQ0eAgfafTsniI2k82eE8c",
#             "gameCustomizationObjects": [],
#             "perks": {
#                 "perkIds": [
#                     8437,
#                     8463,
#                     8444,
#                     8242,
#                     8106,
#                     8126,
#                     5007,
#                     5003,
#                     5003
#                 ],
#                 "perkStyle": 8400,
#                 "perkSubStyle": 8100
#             }
#         }
#     ],
#     "observers": {
#         "encryptionKey": "qnfRUQ9xaQ/ykB8lbjQOCce5x9LQUIpT"
#     },
#     "platformId": "NA1",
#     "bannedChampions": [],
#     "gameStartTime": 0,
#     "gameLength": 0
# }