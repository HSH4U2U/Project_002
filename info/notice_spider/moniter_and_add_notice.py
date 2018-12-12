import requests
from bs4 import BeautifulSoup


# 올라온 공지 데이터 얻고 tag 분류하는 함수
def get_notice(sort_of_notice, page):
    url = sort_of_notice['view'] + str(page)
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    title = soup.find('title').text.split('<')[0]
    sort = soup.find('title').text.split('<')[1]
    content = soup.findAll("li", {"id": "view_content"})[0].text
    # TODO: (tag 값 받아오는 거 해야함)tag 해당하는 것 있으면 tags 필드에 넣기
    all_tags = ['아버지 합창단', '스카우터 11기 최종 합격자 발표']
    include_tags = []
    for tag in all_tags:
        if content:
            if title.count(tag) + sort.count(tag) + content.count(tag) > 0:
                include_tags.append(tag)
        elif title.count(tag) + sort.count(tag) > 0:
            include_tags.append(tag)

    # new_notice 에 해당 데이터 저장
    new_notice = {
        "seq": page,
        "sort_of_notice": sort_of_notice,
        "title": title,
        "url": url,
        "tags": include_tags
    }
    return new_notice


# TODO: 얻은 new_notice 데이터를 모델에 저장
notice_list = []  # 이게 모델임


def add_notice(new_notice):
    # 해당 공지가 모델에 없는지 확인
    if not new_notice in notice_list:
        # TODO: 원래는 모델 써서 새로운 object 로 저장
        notice_list.append(new_notice)


# 공지 올라왔는 지 확인하고 올라왔으면 모델에 데이터 저장하는 함수
def monitor_and_add_notice(sort_of_notice, max_notice_seq):
    url = sort_of_notice['list']
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    a_tags = soup.findAll('a')
    seqs = []
    for a_tag in a_tags:
        a_tag_onclick = a_tag.get('onclick')
        if a_tag_onclick:
            if a_tag_onclick.find("fnView(") != -1:
                seq = a_tag_onclick.split("'")[3]
                seq = int(seq)
                seqs.append(seq)
    # 다음 공지 있나 확인하고, 공지 데이터 얻기 함수 실행
    new_notice_seq = max_notice_seq + 1
    if new_notice_seq in seqs:
        max_notice_seq = new_notice_seq
        new_notice = get_notice(sort_of_notice, max_notice_seq)
        add_notice(new_notice)

        # TODO: 여기에 해당 tag 가지고 있는 user 의 receiver_uid 를 모델에서 가져오는 작업 수행
        message = str(new_notice["tags"]) + str(new_notice["title"]) + "/n" + str(new_notice["url"])
        # TODO: 여기에 페메 보내기 함수 넣기(param 은 message 와 receiver_uid)

        monitor_and_add_notice(sort_of_notice, max_notice_seq)
    # 다음 공지가 지워졌을 수도 있으니 +4개까지 공지 확인
    else:
        i = 2
        while i < 5:
            certificate_seq = max_notice_seq + i
            if certificate_seq in seqs:
                max_notice_seq = certificate_seq
                new_notice = get_notice(sort_of_notice, max_notice_seq)
                add_notice(new_notice)

                # TODO: 여기에 해당 tag 가지고 있는 user 의 receiver_uid 를 모델에서 가져오는 작업 수행
                message = str(new_notice["tags"]) + str(new_notice["title"]) + "/n" + str(new_notice["url"])
                # TODO: 여기에 페메 보내기 함수 넣기(param 은 message 와 receiver_uid)

                monitor_and_add_notice(sort_of_notice, max_notice_seq)
                break
            i += 1


monitor_and_add_notice(common_notice, 20464)
print(notice_list)