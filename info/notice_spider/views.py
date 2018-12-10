from django.shortcuts import render

import requests
from bs4 import BeautifulSoup
# import time
#
# now = time.gmtime(time.time())  # 현재 시각 측정 후 해석
# today = "%d-%d-%d" % (now.tm_year, now.tm_mon, now.tm_mday)

common_notice = 'http://uos.ac.kr/korNotice/list.do?list_id=FA1'    #나중에는 for문으로 다 같이 처리!
# bachelor_notice = 'http://uos.ac.kr/korNotice/list.do?list_id=FA2'
# employment_notice = 'http://uos.ac.kr/korNotice/list.do?list_id=FA34'
# job_notice = 'http://uos.ac.kr/korColumn/list.do?list_id=FA35'
# event_notice = 'http://uos.ac.kr/korCalendarMonth/list.do?list_id=FA3'
# extracurriculum_notice = 'http://uos.ac.kr/korNotice/list.do?list_id=ED3'


def get_notice(page):
    url = 'http://uos.ac.kr/korNotice/view.do?list_id=FA1&seq=' + str(page)
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    title = soup.find('title').text.split('<')[0]
    sort = soup.find('title').text.split('<')[1]
#    title = soup.findAll("ul", {"class": "listType"})
    print(title, sort)


def monitor_and_get_notice(sort_of_notice, max_notice_number):
    url = sort_of_notice
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    new_notice_number = max_notice_number + 1
    does_max_page_change = len(soup.findAll(text=new_notice_number))
    if does_max_page_change > 0:
        max_notice_number = new_notice_number
        print(max_notice_number)
        get_notice(max_notice_number)
        monitor_and_get_notice(sort_of_notice, max_notice_number)
    # is_new_notice = soup.findAll(text=str(max_page + 1))
    # if len(is_new_notice) >= 1:
    #     max_page += 1                   # 나중 전체 실행 함수에서는 global로 변수 설정하기 나중에 +1 된 거 집어 넣는거
    #     get_notice(max_page)
    #     monitor_and_get_notice(sort_of_notice, max_page)

monitor_and_get_notice(common_notice, 11935)

# from apscheduler.schedulers.background import BackgroundScheduler
# from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job
#
# scheduler = BackgroundScheduler()
# scheduler.add_jobstore(DjangoJobStore(), "default")
#
#
# @register_job(scheduler, "interval", seconds=10)
# def test_job():
#     i = 20450
#     while i <= 20453:
#         get_notice(i)
#         i += 1
#
#
# register_events(scheduler)
#
# scheduler.start()
# print("Scheduler started!")