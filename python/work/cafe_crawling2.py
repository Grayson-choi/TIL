# -*- coding: utf-8 -*-

import os
import sys
import datetime
import time
from datetime import timedelta
from selenium import webdriver
import urllib.request
from urllib.parse import urlencode

import json
import re


# 네이버 계정 및 앱 정보
naver_id = os.environ.get("NAVER_ID") #네이버 아이디
naver_pw = os.environ.get("NAVER_PW") #네이버 비밀번호
naver_cid = os.environ.get("NAVER_CID") #클라이언트 아이디
naver_csec = os.environ.get("NAVER_CSEC") #클라이언트 시크릿

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
# driver.find_element_by_xpath('//*[@id="profile_optional_list"]/span/label').click()
# time.sleep(1)
# driver.find_element_by_xpath('//*[@id="content"]/div[4]/div[2]/button/span').click()
redirect_url = driver.current_url

temp = re.split('code=', redirect_url)
print(temp)
code = re.split('&state=', temp[1])[0]
print(code)
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

post_title = "성공했따!!!!"
post_content = "이 내용으로 글이 써진당ㅋㅋㅋㅋ"


# 여기서부터 네이버 카페 글쓰기
header = "Bearer " + token # Bearer 다음에 공백 추가
clubid = "28457504" # 카페의 고유 ID값
menuid = "53" # (상품게시판은 입력 불가)

url = "https://openapi.naver.com/v1/cafe/" + clubid + "/menu/" + menuid + "/articles"
subject = urllib.parse.quote(post_title) # 제목
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

print("이거다")

print(response_body.decode('utf-8')[1])
