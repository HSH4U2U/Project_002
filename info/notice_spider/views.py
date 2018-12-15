from django.shortcuts import render
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job
from .moniter_and_add_notice import monitor_and_add_send_notice
from .models import Notice


common_notice = {
    'list': 'http://uos.ac.kr/korNotice/list.do?list_id=FA1',
    'view': 'http://uos.ac.kr/korNotice/view.do?list_id=FA1&seq='
}
bachelor_notice = {
    'list': 'http://uos.ac.kr/korNotice/list.do?list_id=FA2',
    'view': 'http://uos.ac.kr/korNotice/view.do?list_id=FA2&seq='
}
employment_notice = {
    'list': 'http://uos.ac.kr/korNotice/list.do?list_id=FA34',
    'view': 'http://uos.ac.kr/korNotice/view.do?list_id=FA34&seq='
}
notices = [common_notice, bachelor_notice, employment_notice]

scheduler = BackgroundScheduler()
scheduler.add_jobstore(DjangoJobStore(), "default")


# def job(notice):
#     max_notice_seq = Notice.objects.filter(sort=notice).values("seq").last()["seq"]
#     monitor_and_add_send_notice(notice, max_notice_seq)
#
#
# # TODO: 5분마다 전체 함수 실행
# @register_job(scheduler, "interval", seconds=10)
# def test_job():
#     for notice in notices:
#         max_notice_seq = Notice.objects.filter(sort=notice).values("seq").last()["seq"]
#         monitor_and_add_send_notice(notice, max_notice_seq)
#
#
# register_events(scheduler)
#
# scheduler.start()
# print("Scheduler started!")
