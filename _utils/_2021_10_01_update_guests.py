from lib import get_all_episodes, read_data, write_data

guests = {"4":["whale"],"5":["whale"],"7":["whale"],"8":["johnny"],"9":["johnny"],"12":["liu"],"13":["liu"],"14":["yoga"],"15":["yoga"],"18":["yian"],"19":["yian"],"20":["infosec"],"21":["angel"],"22":["pengju"],"23":["pengju"],"25":["jessie"],"27":["mamakajima"],"28":["tzuting"],"30":["angel"],"31":["tzuting"],"32":["tzuting"],"33":["hsiang"],"34":["hsiang"],"35":["ralph"],"36":["mamakajima"],"37":["kwan"],"39":["likeitformosa"],"40":["peitsun"],"41":["peitsun"],"42":["piggyteammates"],"43":["piggyteammates"],"45":["stanley"],"46":["tsanyu"],"47":["cindy"],"48":["brandy"],"49":["vivian"],"51":["lena"],"52":["ane"],"53":["ane"],"54":["summer"],"55":["yolanda"],"56":["chunyuan"],"58":["tsanyu"],"59":["tsanyu"],"62":["malina"],"63":["cheryl"],"64":["pointchen"],"67":["haku"],"68":["whale"],"71":["jacques"]}

episodes = get_all_episodes()
for episode in episodes:
  data = read_data(episode)
  if str(data['episode']) in guests:
    data['guests'] = guests[str(data['episode'])]
  write_data(episode, data)