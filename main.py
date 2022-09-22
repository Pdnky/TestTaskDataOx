import requests
from bs4 import BeautifulSoup
from config import db
from models import *


def check_status_code(url, page):
    """
    :param url: url pages to check code status
    :param page: For a more informative error
    :return: 1 - status code 200, allows you to parse the site
             2 - status code does not allow parsing the page
    """
    if 200 >= url.status_code < 300:
        return 1
    else:
        print(f'Error in page-{page}: status_code:{url.status_code}')
        return 2


def save_data(data):
    """
    :param data: Processed information that will be stored in the database
    :return: nothing
    """
    db.add(Item(
        image=data['image'],
        title=data['title'],
        date=data['date'],
        location=data['location'],
        beds=data['beds'],
        description=data['description'],
        price=data['price']
    ))
    db.commit()


def parse():
    """
    The main function that performs the extraction of the necessary information from the page
    """
    for page_num in range(1, 95, 1):
        url = f'https://www.kijiji.ca/b-apartments-condos/city-of-toronto/page-{page_num}/c37l1700273'

        q = requests.get(url)

        if check_status_code(q, page_num) == 2:
            continue

        result = q.content
        soup = BeautifulSoup(result, 'lxml')

        page_content = soup.find('div', {'class': 'new-real-estate-srp'}).find_all('div', {'class': 'clearfix'})

        for hotel_info in page_content:
            data = {
                'image': hotel_info.find('img').get('src'),
                'title': hotel_info.find('div', {'class': 'title'}).text.strip(),
                'date': hotel_info.find('span', {'class': 'date-posted'}).text.replace('/', '-'),
                'location': hotel_info.find('span', {'class': ''}).text.strip(),
                'beds': hotel_info.find('span', {'class': 'bedrooms'}).text.split('\n')[-2].strip(),
                'description': hotel_info.find('div', {'class': 'description'}).stripped_strings.__next__(),
                'price': hotel_info.find('div', {'class': 'price'}).text.strip()
            }

            save_data(data)


if __name__ == '__main__':
    parse()
