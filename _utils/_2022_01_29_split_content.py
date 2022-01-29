from lib import get_all_episodes, read_data, write_data, read_content, write_content
import json, os

episodes = get_all_episodes()
for episode in episodes:
  content = read_content(episode)
  [desc, appendix] = content.split('{% include middle.html %}')
  write_content(episode, desc)
  write_content('../_extensions/' + episode.replace('ep', 'ext'), '---\n---\n' + appendix)