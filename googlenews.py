import ssl
import tweepy
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
from time import sleep
from mtranslate import translate
from googletrans import Translator



consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
# translator = Translator(service_urls=['translate.google.com'])

def twitter(news11):
  "  "
  try:
      to_translate = translate(news11,'ml')
      # translated = translator.translate(news11,src="en",dest='ml')
      api.update_status(to_translate)
      print(f'news title: {news11}')
      sleep(60)

  except tweepy.TweepError as e:
        print(e.reason)

def news(xml_news_url):
    '''Print select details from a html response containing xml
      @param xml_news_url: url to parse
      '''

    context = ssl._create_unverified_context()
    Client = urlopen(xml_news_url, context=context)
    xml_page = Client.read()
    Client.close()

    soup_page = soup(xml_page, "xml")

    news_list = soup_page.findAll("item")

    for news in news_list:
        twitter(news.title.text)
        
        # print(f'news link:    {news.link.text}')
        # print(f'news pubDate: {news.pubDate.text}')
        print("+-" * 20, "\n\n")


# you can add google news 'xml' URL here for any country/category
news_url = "https://news.google.com/news/rss/?ned=us&gl=US&hl=en"
sports_url = "https://news.google.com/news/rss/headlines/section/topic/SPORTS.en_in/Sports?ned=in&hl=en-IN&gl=IN"

# now call news function with any of these url or BOTH
news(news_url)
# news(sports_url)