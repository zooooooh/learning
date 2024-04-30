import requests
from bs4 import BeautifulSoup
import lxml
from time import sleep
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5414.74 Safari/537.36'}

def download(url):
    resp = requests.get(url, stream=True)
    r = open('C:\\Users\\User\\PycharmProjects\\simplest_parser\\image\\' + url.split('/')[-1], 'wb')

    for value in resp.iter_content(1024*1024):
        r.write(value)
    r.close()

def get_url():
    for count in range(1, 8):
        url = f'https://scrapingclub.com/exercise/list_basic/?page={count}'

        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')  # html.parser
        data = soup.find_all('div', class_='w-full rounded border')
        for i in data:
            card_url = 'https://scrapingclub.com' + i.find('a').get('href')
            yield card_url



def array():
    for card_url in get_url():
        response = requests.get(card_url, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')
        data = soup.find('div', class_='my-8 w-full rounded border')
        name = data.find('h3', class_='card-title').text
        price = data.find('h4', class_='my-4 card-price').text
        text = data.find('p', class_='card-description').text
        url_img = 'https://scrapingclub.com' + data.find('img', class_='card-img-top').get('src')
        download(url_img)
        yield name, price, text, url_img
