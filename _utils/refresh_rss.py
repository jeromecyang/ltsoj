import re, os, json
from collections import OrderedDict

def get_content(filepath):
  f = open(filepath)
  content = f.read()
  return content

path = os.path.dirname(os.path.realpath(__file__)) + '/../_posts/'
posts = sorted(os.listdir(path), reverse=True)
obj = OrderedDict()

for post in [p for p in posts if '-ep' in p and not 'episodes' in p]:
  content = get_content(path + post)
  episode = re.findall(r'episode: .*?\n', content)[0].replace('episode: ', '').replace('\n', '')
  main = re.findall(r'\n---.*?{%', content, flags=re.S)[0].replace('\n---', '').replace('{%', '')
  obj[episode] = {'description': main}

g = open(os.path.dirname(os.path.realpath(__file__)) + '/../_data/episodes.json', 'w')
g.write(json.dumps(obj, indent=2))
g.close()
