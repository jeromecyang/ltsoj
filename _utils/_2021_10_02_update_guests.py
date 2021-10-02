from lib import *

episodes = get_all_episodes()
for episode in episodes:
  data = read_data(episode)
  data['subtitle'] = data['title']
  data['title'] = data['name']
  del data['name']
  del data['episodes']
  del data['order']
  if 'avatar' in data:
    data['image'] = data['avatar']
    del data['avatar']
  write_data(episode, data)