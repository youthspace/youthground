from django.http import Http404, JsonResponse
from ..services import users


def index(request):
    # 회원가입
    if request.method == 'POST':
        return JsonResponse(users.create(request))
    raise Http404


def login(request):
    # 로그인
    if request.method == 'POST':
        return JsonResponse(users.login(request))
    raise Http404


def me(request):
    # 회원정보 조회
    if request.method == 'GET':
        return JsonResponse(users.find_me(request))
    # 회원정보 수정
    elif request.method == 'PATCH':
        return JsonResponse(users.update_me(request))
    raise Http404
