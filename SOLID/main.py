from social_midias.midia_types import SocialMidiaTypes
from links import get_link

social_midia_link = get_link(
  params='watch?v=899Qa6sQcRc&t=200s',
  midia=SocialMidiaTypes.YOUTUBE
)

print(social_midia_link)