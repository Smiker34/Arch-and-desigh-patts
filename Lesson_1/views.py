from framework.templator import render


class Index:
    def __call__(self, request):
        return '200 OK', render('./templates/index.html', date=request.get('date', None))


class About:
    def __call__(self, request):
        return '200 OK', render('./templates/about.html', date=request.get('date', None))
