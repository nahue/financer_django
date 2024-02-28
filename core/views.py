from django.shortcuts import render
from django.views.generic import CreateView, ListView, DeleteView, DetailView, UpdateView, View
from django.contrib.messages.views import SuccessMessageMixin
from django import forms
from .models import Account
from django.urls import reverse_lazy

class HtmxView(View):
    def get_context_data(self, **kwargs):
        ctx = super(HtmxView, self).get_context_data(**kwargs)
        if self.request.htmx:
            base_template = "_partial.html"
            message = "Hello from Server + HTMX"
        else:
            base_template = "_base.html"
            message = "Hello from Server"
        ctx["base_template"] = base_template
        ctx["message"] = message
        return ctx

class AccountBaseView(HtmxView):
    model = Account
    fields = '__all__'
    success_url = reverse_lazy('core:account-list')


class ListAccounts(AccountBaseView, ListView):
    pass

class CreateAccount(AccountBaseView, SuccessMessageMixin, CreateView):
    success_message = "%(name)s was created successfully"

class UpdateAccount(AccountBaseView, SuccessMessageMixin, UpdateView):
    success_message = "%(name)s was updated successfully"

class DeleteAccount(AccountBaseView, SuccessMessageMixin, DeleteView):
    def get_success_message(self, cleaned_data):
        return f'{self.object.name} was deleted'


def index(request):
    if request.htmx:
        base_template = "_partial.html"
        message = "Hello from Server + HTMX"
    else:
        base_template = "_base.html"
        message = "Hello from Server"

    return render(request, "core/index.html", {
        "base_template": base_template,
        "message": message
    })


def transacciones(request):
    if request.htmx:
        base_template = "_partial.html"
        message = "Hello from Server + HTMX"
    else:
        base_template = "_base.html"
        message = "Hello from Server"

    print(base_template)
    return render(request, "core/transacciones.html", {
        "base_template": base_template,
        "message": message
    })


def deudas(request):
    if request.htmx:
        base_template = "_partial.html"
        message = "Hello from Server + HTMX"
    else:
        base_template = "_base.html"
        message = "Hello from Server"

    print(base_template)
    return render(request, "core/deudas.html", {
        "base_template": base_template,
        "message": message
    })
