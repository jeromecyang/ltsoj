import sys, re, os, yaml

def add_to_data(raw_content, data_to_add):
  data_list = raw_content.split('---')
  data_list[1] = data_list[1] + data_to_add
  return "---".join(data_list)

path = os.path.dirname(os.path.realpath(__file__)) + '/../_posts/'
posts = os.listdir(path)
#for post in ['2021-03-04-ep041.md']:
# for post in ['2020-07-03-ep003.md']:
for post in [p for p in posts if 'ep0' in p and not 'ep042' in p and not 'ep043' in p and not 'ep044' in p]:
  f = open(path + post)
  content = f.read()

  print post
  number = re.findall(r'title: EP\d+', content)[0].replace('title: EP', '')
  spotify = re.findall(r'episode/.+\)', content)[0].replace('episode/', '').replace(')', '')
  apple = re.findall(r'\?i=.+\)', content)[0].replace('?i=', '').replace(')', '')

  template = """episode: {number}
player:
  spotify: {spotify}
  apple: {apple}
""".format(number=number, spotify=spotify, apple=apple)
  output = add_to_data(content, template).replace('listen.html', 'middle.html')
  output = re.sub(r'\!\[\]\(.*?\)', '', output.replace('---\n\n', '---'), 1)
  output = re.sub(r'## \xe4.+apple', '', output, flags=re.S)
  output = re.sub(r'<iframe src.+apple', '', output, flags=re.S)
  output = re.sub(r'\.com\/tw\/podcast\/id1518914711\?i\=\d+\)', '', output)

  g = open(path + post, 'w')
  g.write(output)
  g.close()
