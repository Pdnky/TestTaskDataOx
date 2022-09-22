import requests
from bs4 import BeautifulSoup
from config import db
from models import *


class PageScrap:


    def parse():
        for page_num in range(1, 2, 1):
            url = f'https://www.kijiji.ca/b-apartments-condos/city-of-toronto/page-{page_num}/c37l1700273'

            q = requests.get(url)
            result = q.content
            soup = BeautifulSoup(result, 'lxml')

            page_content = soup.find('div', {'class': 'new-real-estate-srp'}).find_all('div', {'class': 'clearfix'})

            for hotel_info in page_content:

                photo = hotel_info.find('img').get('src')
                title = hotel_info.find('div', {'class': 'title'}).text.strip()
                date = hotel_info.find('span', {'class': 'date-posted'}).text.replace('/', '-')
                city = hotel_info.find('span', {'class': ''}).text.strip()
                beds = hotel_info.find('span', {'class': 'bedrooms'}).text.split('\n')[-2].strip()
                description = hotel_info.find('div', {'class': 'description'}).stripped_strings.__next__()
                price = hotel_info.find('div', {'class': 'price'}).text.strip()

                db.add(Item(
                        image=photo,
                        title=title,
                        date=date,
                        location=city,
                        beds=beds,
                        description=description,
                        price=price
                    ))
                db.commit()


PageScrap.parse()
