import sys, re

f = open(sys.argv[1])
text = f.read()

tables = re.findall(r'\<table.*?\<\/table\>', text, re.DOTALL)

for table in tables:
  images = re.findall(r'\!\[\]\(.*?\)', table)
  captions = re.findall(r'tr-caption\"\s\>.*?\<', table, re.DOTALL)
  if len(images) > 0:
    image = images[0] + '\n'
    if len(captions) > 0:
      caption = '*' + captions[0].replace('tr-caption" >', '').replace('<', '').replace('\n', '') + '*\n'
      image += caption
    text = text.replace(table, image)

g = open(sys.argv[1].split('.')[0] + '.md', 'w')
g.write(text)
g.close()

