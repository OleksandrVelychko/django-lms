from django.urls import path
from core_lms.views import get_index_page

urlpatterns = [
    path('', get_index_page, name='index'),
]
