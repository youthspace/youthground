import jwt
from django.conf import settings
from django.http import JsonResponse


class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if 'HTTP_AUTHORIZATION' in request.META:
            token = str(request.META['HTTP_AUTHORIZATION'])[7:]
            try:
                decoded = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
                request.user_id = decoded['id']
            except jwt.exceptions.DecodeError:
                return JsonResponse({'result': False, 'error': '토큰이 잘못되었습니다.'})
            except jwt.exceptions.ExpiredSignatureError:
                return JsonResponse({'result': False, 'error': '토큰이 만료되었습니다.'})
        else:
            request.user_id = None

        response = self.get_response(request)
        return response
