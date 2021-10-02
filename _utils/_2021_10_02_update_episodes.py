from lib import *

episodes = get_all_episodes()
for episode in episodes:
  data = read_data(episode)
  del data['layout']
  del data['permalink']
  del data['podcast']
  write_data(episode, data)