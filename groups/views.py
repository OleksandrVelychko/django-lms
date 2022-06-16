from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404  # noqa
from django.views.generic import UpdateView
from groups.forms import GroupUpdateForm
from groups.models import Group


@login_required
def get_group(request, id):
    group = get_object_or_404(Group, id=id)
    return render(request,
                  'groups/group.html',
                  {
                      'group': group
                  }
                  )


class GroupEditView(LoginRequiredMixin, UpdateView):
    model = Group
    form_class = GroupUpdateForm
    template_name = 'groups/edit_group.html'
    pk_url_kwarg = 'id'
