from adapters.browser.chrome import Chrome
from adapters.social_midia.youtube import Youtube
from adapters.social_midia.twitter import Twitter

youtube = Youtube.create('@NandoMouraOficial')
youtube_link = youtube.profile_info()

twitter = Twitter.create('moura_101')
twitter_link = twitter.profile_info()

youtube_page = Chrome(youtube_link)
twitter_page = Chrome(twitter_link)

youtube_page.open()
twitter_page.open()