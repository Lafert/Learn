import requests
from bs4 import BeautifulSoup
from time import sleep

url_base = 'https://scrapingclub.com'

def get_url():

    for count in range(1, 3):
        url = f'https://scrapingclub.com/exercise/list_basic/?page={count}'

        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')  # html.parser

        data = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
        for card_url in data:
            url_card = url_base + card_url.find('a').get('href')
            yield url_card

for card_url in get_url():
    # name = i.find('h4', class_='card-title').text.replace('\n', '')
    # price = i.find('h5').text
    # url_img = 'https://scrapingclub.com' + i.find('img', class_='card-img-top img-fluid').get('src')

    response = requests.get(card_url)
    soup = BeautifulSoup(response.text, 'lxml')  # html.parser
    data = soup.find('div', class_='card mt-4 my-4')

    name = data.find('h3', class_= 'card-title').text
    price = data.find('h4').text
    overviev = data.find('p', class_='card-text').text
    url_img = url_base + data.find('img').get('src')
    print(name + '\n', price + '\n', overviev + '\n', url_img + '\n')

