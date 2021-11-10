import csv
from time import sleep, time
from random import randint
from fake_useragent import UserAgent


import requests
from bs4 import BeautifulSoup


def random_sleep():
    sleep(randint(1, 3))

ua = UserAgent()


BASE_URL = 'https://www.work.ua/ru/jobs/'

with open(f'jobs{time()}.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(('job_id', 'title'))

    page = 0
    while True:
        page += 1
        print(f'Page: {page}')
        params = {
            'page': page,
        }

        random_sleep()

        headers = {
            'User-Agent': ua.random,
        }
        response = requests.get(BASE_URL, params=params, headers=headers)
        response.raise_for_status()

        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        job_list = soup.find("div", {"id": "pjax-job-list"})

        if job_list is None:
            break

        cards = job_list.findAll('h2', {'class': ''})

        for card in cards:
            # TODO сделать запрос на детали вакансии и достать инфо
            """
            response = requests.get(???)
            response.raise_for_status()

            html = response.text
            soup = BeautifulSoup(html, 'html.parser')
            """

            link = card.find('a')
            href = link['href']
            job_id = href.split('/')[-2]
            title = link.text

            writer.writerow((job_id, title))
