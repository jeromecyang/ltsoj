import sys, re, os, yaml, json

def add_to_data(raw_content, data_to_add):
  data_list = raw_content.split('---')
  data_list[1] = data_list[1] + data_to_add
  return "---".join(data_list)

def update(filepath, data_to_add):
  f = open(filepath)
  content = f.read()
  g = open(filepath, 'w')
  g.write(add_to_data(content, data_to_add))
  g.close()

path = os.path.dirname(os.path.realpath(__file__)) + '/../_posts/'
posts = os.listdir(path)

data = json.load(open('/Users/jeromecyang/Desktop/feed.json'))['rss']['channel']['item']
obj = {}
for d in data:
  if ('EP' in d['title']):
    episode = re.findall(r'EP[\d\.]+\s', d['title'])[0].replace('EP', '').replace(' ', '')
    obj[episode] = d

for post in [p for p in posts if '-ep' in p and not 'episodes' in p]:
  f = open(path + post)
  content = f.read()
  episode = re.findall(r'episode: \d+', content)[0].replace('episode: ', '')
  addition = 'duration: \'' + str(obj[episode]['duration']['__text']) + '\'\n' + 'guid: ' + str(obj[episode]['guid']['__text']) + '\n' + 'filepath: ' + str(obj[episode]['enclosure']['_url'].replace('https://chtbl.com/track/782GB8/jeromecyang.github.io/', '')) + '\n'
  update(path + post, addition)