from lib import get_all_episodes, read_data, write_data
import json, os

parsed_data = json.load(open(os.path.dirname(os.path.realpath(__file__)) + '/../_data/podcast_data.json'))

episodes = get_all_episodes()
for episode in episodes:
  data = read_data(episode)
  timeline = parsed_data[str(data['episode'])]['timeline']
  data['timeline'] = list(map(lambda x: {'time': x['time'] + ' ', 'text': x['text']}, timeline))
  write_data(episode, data)