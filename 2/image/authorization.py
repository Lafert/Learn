from requests import Session
from bs4 import BeautifulSoup
from time import sleep


headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0'}
url_base = 'https://quotes.toscrape.com'
url_login = 'https://quotes.toscrape.com/login'

work = Session()
work.get(url_base, headers=headers)
work.get(url_login, headers=headers)
