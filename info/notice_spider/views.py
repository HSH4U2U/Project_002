from django.shortcuts import render
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job
from .moniter_and_add_notice import monitor_and_add_notice

common_notice = {
    'list': 'http://uos.ac.kr/korNotice/list.do?list_id=FA1',
    'view': 'http://uos.ac.kr/korNotice/view.do?list_id=FA1&seq='
}
# bachelor_notice = 'http://uos.ac.kr/korNotice/list.do?list_id=FA2'
# employment_notice = 'http://uos.ac.kr/korNotice/list.do?list_id=FA34'
# job_notice = 'http://uos.ac.kr/korColumn/list.do?list_id=FA35'
# event_notice = 'http://uos.ac.kr/korCalendarMonth/list.do?list_id=FA3'
# extracurriculum_notice = 'http://uos.ac.kr/korNotice/list.do?list_id=ED3'

scheduler = BackgroundScheduler()
scheduler.add_jobstore(DjangoJobStore(), "default")


# TODO: 5분마다 전체 함수 실행
@register_job(scheduler, "interval", seconds=300)
def test_job():
    # 예시로 채워논 것(notice_list 모델에 있는 거로 바꿔줘야 함)
    max_notice_seq = notice_list[-1]['seq']
    monitor_and_add_notice(common_notice, max_notice_seq)
    print(notice_list)
    # TODO: for 문으로 모든 공지에서 아래 실행
       # TODO: 각 공지의 최근 글의 seq 얻기
       # TODO: 여기에 monitor_and_add_notice(해당 공지, 최근 글의 seq) 함수 넣기


register_events(scheduler)

scheduler.start()
print("Scheduler started!")