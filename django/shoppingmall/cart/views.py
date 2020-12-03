from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from .forms import AddProductForm
from .cart import Cart
from iamport import Iamport
from datetime import datetime

@require_POST
def add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)

    form = AddProductForm(request.POST)

    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], is_update=cd['is_update'])

    return redirect('cart:detail')


def remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:detail')

def detail(request):
    cart = Cart(request)


    for product in cart:
        product['quantity_form'] = AddProductForm(initial={
            'quantity': product['quantity'],
            'is_update': True

    })

    context = {
        'cart': cart
    }

    return render(request, 'cart/detail.html', context)


def payment(request):
    cart = Cart(request)
    product_price = 10000
    imp_key = '3573147061630950'
    imp_secret = 'FeUZatDu2pPcSBhuMXPRVmXFwjmamVW1aR1kkFOm4EyXfQr1NhTJDQpa9LlvHhxR8zcse1PjFogVeIX2'


    # 객체 만들기
    iamport = Iamport(imp_key=imp_key, imp_secret=imp_secret)
    # 테스트용 키와 시크릿은 tests/conftest.py 파일에 DEFAULT_TEST_IMP_KEY, DEFAULT_TEST_IMP_SECRET를 참고하세요.
    # 객체 만들기
    iamport = Iamport(imp_key=imp_key, imp_secret=imp_secret)

    # 테스트용 값
    payload = {
        'merchant_uid': str(datetime.now) + '00000000',
        'amount': 10000,
        'card_number': '4092-0230-1234-1234',
        'expiry': '2019-03',
        'birth': '500203',
        'pwd_2digit': '19'
    }

    try:
        response = iamport.pay_onetime(**payload)
    except KeyError:
        # 필수 값이 없을때 에러 처리
        pass
    except Iamport.ResponseError as e:
        # 응답 에러 처리
        pass
    except Iamport.HttpError as http_error:
        # HTTP not 200 응답 에러 처리
        pass
    return response


    # # 상품 아이디로 조회
    # response = iamport.find(merchant_uid='{상품 아이디}')
    #
    # # I'mport; 아이디로 조회
    # response = iamport.find(imp_uid='{IMP UID}')
    #
    # # 상품 아이디로 확인
    # iamport.is_paid(product_price, merchant_uid='{상품 아이디}')
    #
    # # I'mport; 아이디로 확인
    # iamport.is_paid(product_price, imp_uid='{IMP UID}')
    #
    # # 이미 찾은 response 재활용하여 확인
    # iamport.is_paid(product_price, response=response)
    #
    # # 테스트용 값
    # payload = {
    #     'merchant_uid': '00000000',
    #     'amount': 5000,
    #     'card_number': '4092-0230-1234-1234',
    #     'expiry': '2019-03',
    #     'birth': '500203',
    #     'pwd_2digit': '19'
    # }
    # try:
    #     response = iamport.pay_onetime(**payload)
    # except KeyError:
    #     # 필수 값이 없을때 에러 처리
    #     pass
    # except Iamport.ResponseError as e:
    #     # 응답 에러 처리
    #     pass
    # except Iamport.HttpError as http_error:
    #     # HTTP not 200 응답 에러 처리
    #     pass
    #
    # # 테스트용 값
    # amount = 12000
    # mid = 'merchant_test'
    # try:
    #     response = iamport.prepare(amount=amount, merchant_uid=mid)
    # except Iamport.ResponseError as e:
    #     # 응답 에러 처리
    #     pass
    # except Iamport.HttpError as http_error:
    #     # HTTP not 200 응답 에러 처리
    #     pass
    #
    # # 테스트용 값
    # amount = 12000
    # mid = 'merchant_test'
    # try:
    #     result = iamport.prepare_validate(merchant_uid=mid, amount=amount)
    # except Iamport.ResponseError as e:
    #     # 응답 에러 처리
    #     pass
    # except Iamport.HttpError as http_error:
    #     # HTTP not 200 응답 에러 처리
    #     pass
