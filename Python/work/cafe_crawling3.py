# -*- coding: utf-8 -*-

import os
import sys
# import django
import datetime
from datetime import timedelta
from selenium import webdriver

import urllib.request
from urllib.parse import urlencode

import json
import re

# # Django 모델에 접근하기 위함
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# os.environ['DJANGO_SETTINGS_MODULE'] = 'chemreg.settings'
# django.setup()
# from news.models import Notice, Source #Notice와 Source 모델을 사용


# 네이버 계정 및 앱 정보
# 보안을 위해 환경 변수로 등록
naver_id = "784wldnd" #네이버 아이디
naver_pw = "chlwldnd1!" #네이버 비밀번호
naver_cid = "aYTsvZMKlGN5WlK2XRDI" #클라이언트 아이디
naver_csec = "6fn4JXF_rn" #클라이언트 시크릿

naver_redirect = "http://127.0.0.1:8000/" #리다이렉트 URI -> 아무거나 상관없음


driver = webdriver.Chrome("/Users/jw/Desktop/study/Python/work/chromedriver")
driver.implicitly_wait(3)

# 네이버 로그인
driver.get('https://nid.naver.com/nidlogin.login')
driver.execute_script("document.getElementsByName('id')[0].value=\'"+ naver_id + "\'")
driver.execute_script("document.getElementsByName('pw')[0].value=\'"+ naver_pw + "\'")
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
driver.implicitly_wait(3)
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/span[2]/a').click()

state = "SOMETHING" # 보안을 위한 문자열 -> 아무거나 상관없음

# 네아로로 이동
req_url = 'https://nid.naver.com/oauth2.0/authorize?response_type=code&client_id=%s&redirect_uri=%s&state=%s' % (naver_cid, naver_redirect, state)
driver.get(req_url)

# 처음 1회에 한해서 여기서 권한을 추가하는데, 이것은 수동으로 하는 게 편할 것 같아서 그냥 이렇게 놔둠
# 오류가 발생한다면 이까지만 실행하고 권한 추가는 수동으로 한다.
# 카페 관련 권한 체크하는 것 빼먹지 않도록 조심.

redirect_url = driver.current_url
temp = re.split('code=', redirect_url)
code = re.split('&state=', temp[1])[0]
driver.quit()

url = 'https://nid.naver.com/oauth2.0/token?'
data = 'grant_type=authorization_code' + '&client_id=' + naver_cid + '&client_secret=' + naver_csec + '&redirect_uri=' + naver_redirect + '&code=' + code + '&state=' + state


request = urllib.request.Request(url, data=data.encode("utf-8"))
request.add_header('X-Naver-Client-Id', naver_cid)
request.add_header('X-Naver-Client-Secret', naver_redirect)
response = urllib.request.urlopen(request)
rescode = response.getcode()
token = ''

# 정상 작동하면 token 변수에 접근토큰이 저장된다.
if rescode == 200:
    response_body = response.read()
    js = json.loads(response_body.decode('utf 8'))
    token = js['access_token']
else:
    print("Error Code:", rescode)

# 접근 토큰을 정상적으로 받아왔다면 이제 글을 쓸 차례

# 여기서부터는 게시물 내용 작성을 위한 부분. Django DB에 접근한다
# source_list = Source.objects.all()
# one_week_ago = datetime.datetime.today() - timedelta(days=7) # 일주일 전 날짜

# 지난 주 게시물을 가져오는 함수
# def last_week_notices(pk):
#     return Notice.objects.filter(source__pk=pk).filter(written_date__gte=one_week_ago).order_by('-written_date','-scrapped_date')

post_content = "게시글 내용입니다." # 게시물 내용
# for source in source_list:
#     notices = last_week_notices(source.pk)
#     if notices:
#         post_content += "<br> <h2><a href='{}'>{} {}</a></h2>".format(source.address, source.name, source.sub_name)
#         for notice in notices:
#             post_content += "<strong>{}</strong> {} <br>".format(str(notice.written_date)[:11], notice.title)
post_content += "<br><br>-----<br>이 글은 매주 월요일 아침에 자동으로 게시됩니다.<br>감사합니다.<br>"
# 여기까지는 장고에서 글 쓸 내용을 불러오는 내용이었음

# 여기서부터 네이버 카페 글쓰기
header = "Bearer " + token # Bearer 다음에 공백 추가
clubid = "29415004" # 카페의 고유 ID값
menuid = "59" # (상품게시판은 입력 불가)

url = "https://openapi.naver.com/v1/cafe/" + clubid + "/menu/" + menuid + "/articles"
subject = urllib.parse.quote("테스트 글 제목") # 제목
content = urllib.parse.quote(post_content) # 글 내용
data = urlencode({'subject': subject, 'content': content}).encode()
request = urllib.request.Request(url, data=data)
request.add_header("Authorization", header)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)