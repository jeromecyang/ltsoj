from lib import *

episodes = get_all_episodes()
for episode in [e for e in episodes[:41] if not e in ['ep017.md', 'ep026.md', 'ep035.md']]:
  content = read_content(episode)
  timeline = get_section(content, 1)
  lines = re.findall(r'\*.*?\n', timeline, flags=re.S)
  output = '\n'
  for line in lines:
    parts = line.replace('* ', '').split(' ', 1)
    time = parts[0].replace('(','').replace(')','')
    if len(time) == 4:
      line = line.replace(time, '(00:0' + time + ')')
    if len(time) == 5:
      line = line.replace(time, '(00:' + time + ')')
    output = output + line
  write_content(episode, content.replace(timeline, output))