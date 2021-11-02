from social_midias.base.midia_types import SocialMidiaTypes
from links import get_link

youtube_link = get_link(
  params='watch?v=899Qa6sQcRc&t=200s',
  midia=SocialMidiaTypes.YOUTUBE
)

twitter_link = get_link(
  params='Oscar_timaocord',
  midia=SocialMidiaTypes.TWITTER
)

for link in [youtube_link, twitter_link]: print(link)