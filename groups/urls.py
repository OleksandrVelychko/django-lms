from django.urls import path

from groups.views import get_group, update_group

app_name = 'groups'

urlpatterns = [
    path('<int:id>', get_group, name='get_group'),
    path('update/<int:id>', update_group, name='edit_group'),
    ]
