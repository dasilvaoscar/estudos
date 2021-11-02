from social_midias.midia_types import SocialMidiaTypes
from social_midias.youtube import Youtube

def get_link(params, midia: SocialMidiaTypes):
    
    midias = {
        SocialMidiaTypes.YOUTUBE: Youtube
    }

    midia = midias[midia](params)

    return midia.get_url()
