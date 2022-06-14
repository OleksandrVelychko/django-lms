from django.urls import path

from groups.views import get_group, GroupEditView

app_name = 'groups'

urlpatterns = [
    path('<int:id>', get_group, name='get_group'),
    path('update/<int:id>', GroupEditView().update_instance, name='edit_group'),
    ]
