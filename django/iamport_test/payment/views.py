from django.shortcuts import render
from django.conf import settings
from iamport import Iamport
# Create your views here.
def index(req):

    return render(req, 'payment/index.html')

def detail(req, iamport):

    return render(req, 'payment/detail.html')

def payment(req):
    # 테스트 용
    DEFAULT_TEST_IMP_KEY = 'imp_apikey'
    DEFAULT_TEST_IMP_SECRET = ('ekKoeW8RyKuT0zgaZsUtXXTLQ4AhPFW3ZGseDA6bkA5lamv9O'
                            'qDMnxyeB9wqOsuO9W3Mx9YSJ4dTqJ3f')

    _iamport = Iamport(imp_key=DEFAULT_TEST_IMP_KEY, imp_secret=DEFAULT_TEST_IMP_SECRET)

    return render(req, 'payment/pay.html')
    # 실제 상점 정보
    # iamport = Iamport(imp_key='{발급받은 키}', imp_secret='{발급받은 시크릿}')