
from django.contrib.auth.mixins import PermissionRequiredMixin

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from crmapp.models import Fine

from crmapp.forms import FineForm


class FineListView(PermissionRequiredMixin, ListView):
    model = Fine
    context_object_name = 'fines'
    template_name = 'fine/list.html'
    permission_required = "crmapp.view_fine"


class FineCreateView(PermissionRequiredMixin, CreateView):
    model = Fine
    form_class = FineForm
    template_name = 'fine/create.html'
    permission_required = "crmapp.add_fine"


class FineUpdateView(PermissionRequiredMixin, UpdateView):
    model = Fine
    form_class = FineForm
    template_name = 'fine/update.html'
    permission_required = "crmapp.change_fine"


class FineDeleteView(PermissionRequiredMixin, DeleteView):
    model = Fine
    context_object_name = 'fine'
    template_name = "fine/delete.html"
    permission_required = "crmapp.delete_fine"

    def get_success_url(self):
        return reverse_lazy("crmapp:fine_list")