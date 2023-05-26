import requests
from bs4 import BeautifulSoup
from time import sleep
import os


def download(url):
    image_dir = 'image'
    current_dir = os.getcwd()
    image_path = os.path.join(current_dir, image_dir)

    if not os.path.exists(image_path):
        os.makedirs(image_path)
        print(f"Папка '{image_dir}' создана в текущей директории.")

    image_filename = os.path.basename(url) + '.jpg'
    image_file_path = os.path.join(image_path, image_filename)

    response = requests.get(url, stream=True)
    with open(image_file_path, 'wb') as file:
        for chunk in response.iter_content(1024 * 1024):
            file.write(chunk)

    print(f"Изображение сохранено по пути: {image_file_path}")


url_base = 'https://scrapingclub.com'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0'}


def get_url():
    for count in range(1, 3):
        url = f'https://scrapingclub.com/exercise/list_basic/?page={count}'

        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')  # html.parser

        data = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
        for card_url in data:
            url_card = url_base + card_url.find('a').get('href')
            yield url_card


def array():
    for card_url in get_url():
        # name = i.find('h4', class_='card-title').text.replace('\n', '')
        # price = i.find('h5').text
        # url_img = 'https://scrapingclub.com' + i.find('img', class_='card-img-top img-fluid').get('src')

        response = requests.get(card_url)
        sleep(0)
        soup = BeautifulSoup(response.text, 'lxml')  # html.parser
        data = soup.find('div', class_='card mt-4 my-4')

        name = data.find('h3', class_='card-title').text
        price = data.find('h4').text
        overviev = data.find('p', class_='card-text').text
        url_img = url_base + data.find('img').get('src')
        download(url_img)
        yield name, price, overviev, url_img



