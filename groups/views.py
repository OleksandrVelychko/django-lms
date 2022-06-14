from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404  # noqa
from django.urls import reverse

from core_lms.views import EditView
from groups.forms import GroupUpdateForm
from groups.models import Group


def get_group(request, id):
    group = get_object_or_404(Group, id=id)
    return render(request,
                  'groups/group.html',
                  {
                      'group': group
                  }
                  )


class GroupEditView(EditView):
    model = Group
    success_url = 'students:list_students'
    form = GroupUpdateForm
    template_name = 'groups/edit_group.html'

    def get_success_url(self, instance):
        return reverse('groups:edit_group', kwargs={'id': instance.id})


# def update_group(request, id):
#     group = get_object_or_404(Group, id=id)
#     if request.method == 'POST':
#         form = GroupUpdateForm(request.POST, instance=group)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('groups:edit_group', kwargs={'id': group.id}))
#     else:
#         form = GroupUpdateForm(instance=group)
#
#     return render(request, 'groups/edit_group.html', {
#         'form': form,
#         'group': group
#     })
