import sys, re

f = open(sys.argv[1])
text = f.read()

new_text = re.sub(r'\?w\=[0-9]*?\)', ')', text)
#for width in widths:
#  print width

g = open(sys.argv[1].split('.')[0] + '.md', 'w')
g.write(new_text)
g.close()