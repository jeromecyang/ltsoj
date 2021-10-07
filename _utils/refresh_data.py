import re, os, json
from collections import OrderedDict

def read_file(filepath):
  f = open(filepath)
  content = f.read()
  return content

def split_and_get_nth(text, pattern, index):
  parts = text.split(pattern)
  if (len(parts) > index):
    return parts[index]
  return ''

def parse_time_point(text):
  parts = text.replace('* ', '').split(' ', 1)
  return OrderedDict({'text':parts[1].replace('\n',''),'time':parts[0].replace('(','').replace(')','')})

def cleanup_multi(patterns, text):
  return reduce(lambda last, pattern: re.sub(pattern, '', last), patterns, text)

path = os.path.dirname(os.path.realpath(__file__)) + '/../_episodes/'
posts = sorted(os.listdir(path), reverse=True)
obj = OrderedDict()

for post in posts:
  content = read_file(path + post)
  episode = re.findall(r'episode: .*?\n', content)[0].replace('episode: ', '').replace('\n', '')
  sections = re.split(r'[^#]##\s.*?\n', split_and_get_nth(content, '---\n', 2), flags=re.S)
  main = cleanup_multi([r'\{.*?\}', r'\!\[\]\(.*?\)', r'###\s', r'\|'], sections[0])
  timeline = sections[1]
  points = map(parse_time_point, re.findall(r'\*.*?\n', timeline, flags=re.S))
  obj[episode] = OrderedDict()
  obj[episode]['description'] = main
  obj[episode]['timeline'] = points

g = open(os.path.dirname(os.path.realpath(__file__)) + '/../_data/podcast_data.json', 'w')
g.write(json.dumps(obj, indent=2, ensure_ascii=False))
g.close()
