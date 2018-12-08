from django.shortcuts import render

import requests
from bs4 import BeautifulSoup


def get_notice(max_pages):
    page = max_pages
    url = 'http://uos.ac.kr/korNotice/view.do?list_id=FA1&seq=' + str(page)
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    title = soup.find('title').text.split('<')[0]
    sort = soup.find('title').text.split('<')[1]
#    title = soup.findAll("ul", {"class": "listType"})
    print(title, sort)

i = 20400

while i <= 20453:
    get_notice(i)
    i += 1


# def get_single_article(item_url):
#     source_code = requests.get(item_url)
#     plain_text = source_code.text
#     soup = BeautifulSoup(plain_text, 'lxml')
#
#     for contents in soup.select('p > span'):
#         print(contents.text)
#
