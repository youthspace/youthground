from django.conf.urls import url

from . import users

urlpatterns = [
    url(r'^users$', users.index),  # 회원가입
    url(r'^users/login$', users.login),  # 로그인
    url(r'^users/me$', users.me),  # 회원정보 조회, 회원정보 수정
]
