import os, yaml

settings = yaml.safe_load(open('../_data/settings.yml'))



def create_tag(item):
  f = open('../tag/' + item['tag'] + '.md', 'w')
  f.write('---\n')
  f.write('layout: tagpage\n')
  f.write('tag: ' + item['tag'] + '\n')
  f.write('title: ' + item['name'].encode('utf-8') + '\n')
  f.write('reversed: ' + ('true' if 'reversed' in item and item['reversed'] else 'false') + '\n')
  f.write('---')
  if 'subitems' in item:
    for subitem in item['subitems']:
      create_tag(subitem)

for item in settings['menu']:
  create_tag(item)