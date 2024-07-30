import json
from bs4 import BeautifulSoup
import requests
import re


def get_date_page():
    pattern = r'16 лютого'
    i = 1
    ac = True
    while ac:
        url = f'https://lb.ua/politics/newsfeed?page={i}'
        bs_soup = BeautifulSoup(requests.get(url).text, 'html.parser')
        dates = [b.string for b in bs_soup.find_all('li', class_='caption list-item-caption')]
        for k in dates:
            if re.search(pattern, k):
                ac = False
            else:
                i += 1
    return i - 2

