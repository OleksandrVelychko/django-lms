from django.shortcuts import render


def get_index_page(request):
    page_title = 'Main page'
    return render(request, 'core_lms/index.html', {
        'args': request.GET,
        'page_title': page_title
    })
