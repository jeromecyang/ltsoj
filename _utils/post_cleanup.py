import sys, re

f = open(sys.argv[1])
lines = f.readlines()
lines = [l for l in lines if not 'slug: ' in l and not 'link: ' in l and not 'comments: ' in l and not 'author: ' in l and not 'wordpress_id: ' in l]

date = sys.argv[1][0:4] + '/' + sys.argv[1][5:7] + '/' + sys.argv[1][8:10]

for i in range(len(lines)):
  if 'tmp: ' in lines[i]:
    break
l = lines[i]
del lines[i]

print l.replace('tmp: ', '').replace('\n', '')

images = re.findall('!\[.*?\]\(http.*?\)', ''.join(lines))
if len(images) > 0:
  image = images[0].replace('![](', '').replace(')', '').replace('?w=300', '')

lines.insert(i, 'permalink: ' + date + '/' + l.replace('tmp: ', ''))
if len(images) > 0:
  lines.insert(i + 1, 'image: ' + image + '\n')

g = open('temp/' + sys.argv[1][0:11] + l.replace('tmp: ', '').replace('\n', '') + '.md', 'w')
g.write(''.join(lines))
g.close()