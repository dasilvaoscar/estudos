from social_midias.base.midia_types import SocialMidiaTypes
from social_midias.youtube import Youtube
from social_midias.twitter import Twitter

def get_link(params, midia: SocialMidiaTypes):
    
    midias = {
        SocialMidiaTypes.YOUTUBE: Youtube,
        SocialMidiaTypes.TWITTER: Twitter
    }

    midia = midias[midia](params)

    return midia.get_url()
