import time

from core_lms.models import Logger


class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start = time.time()
        response = self.get_response(request)
        response.headers['X-Response-Time'] = str(round(time.time() - start, 3))
        print(f'request took {round(time.time() - start, 3)} seconds')
        return response


class PerfTrackerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start = time.time()
        response = self.get_response(request)
        if request.user.is_anonymous:
            current_user = None
        else:
            current_user = request.user
        log = Logger(
            user=current_user,
            path=request.path,
            execution_time=round(time.time() - start, 3),
            query_params=str(request.body)
        )
        log.save()
        # print(f'LOGGED: {current_user} {request.path} {round(time.time() - start, 3)} sec {request.GET}')
        return response
