from social_midias.base.midia_types import SocialMidiaTypes
import factory

def get_link(params, midia: SocialMidiaTypes):
    
    midias = {
        SocialMidiaTypes.YOUTUBE: factory.twitter_factory(),
        SocialMidiaTypes.TWITTER: factory.youtube_factory()
    }

    midia = midias[midia](params)

    return midia.get_url()
