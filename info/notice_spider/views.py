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



from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job

scheduler = BackgroundScheduler()
scheduler.add_jobstore(DjangoJobStore(), "default")


@register_job(scheduler, "interval", seconds=10)
def test_job():
    i = 20450
    while i <= 20453:
        get_notice(i)
        i += 1


register_events(scheduler)

scheduler.start()
print("Scheduler started!")