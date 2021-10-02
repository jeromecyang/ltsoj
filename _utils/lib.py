import sys, re, os, yaml

path = os.path.dirname(os.path.realpath(__file__)) + '/../_posts/'

def get_all_episodes():
  return sorted(filter(lambda x: '-ep' in x and not 'episode' in x, os.listdir(path)))

def add_to_data(raw_content, data_to_add):
  data_list = raw_content.split('---')
  data_list[1] = data_list[1] + data_to_add
  return "---".join(data_list)

def read_data(episode):
  f = open(path + episode)
  content = f.read()
  data_list = content.split('---')
  return yaml.load(data_list[1], Loader=yaml.FullLoader)

def write_data(episode, data):
  f = open(path + episode)
  content = f.read()
  data_list = content.split('---')
  str_data = '\n' + yaml.dump(data, sort_keys=False, allow_unicode=True)
  new_content = "---".join([data_list[0], str_data, *data_list[2:]])
  g = open(path + episode, 'w')
  g.write(new_content)
  g.close()