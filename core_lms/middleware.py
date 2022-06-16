import time


class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start = time.time()
        response = self.get_response(request)
        response.headers['X-Response-Time'] = str(round(time.time() - start, 3))
        print(f'request took {round(time.time() - start, 3)} seconds')
        return response
