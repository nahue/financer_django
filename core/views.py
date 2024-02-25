from django.shortcuts import render, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, View
from django.contrib.messages.views import SuccessMessageMixin
from django import forms
from .models import Account


class HtmxMixin(View):
    def get_context_data(self, **kwargs):
        ctx = super(HtmxMixin, self).get_context_data(**kwargs)
        if self.request.htmx:
            base_template = "_partial.html"
            message = "Hello from Server + HTMX"
        else:
            base_template = "_base.html"
            message = "Hello from Server"
        ctx["base_template"] = base_template
        ctx["message"] = message
        return ctx


class ListAccounts(HtmxMixin, ListView):
    model = Account


class CreateAccount(HtmxMixin, SuccessMessageMixin, CreateView):
    model = Account
    form = Account

    fields = "__all__"
    success_url = "/accounts"
    success_message = 'Cuenta creada correctamente'


class UpdateAccount(HtmxMixin, UpdateView):
    model = Account
    form = Account

    fields = "__all__"
    success_url = "/accounts"


def index(request):
    if request.htmx:
        base_template = "_partial.html"
        message = "Hello from Server + HTMX"
    else:
        base_template = "_base.html"
        message = "Hello from Server"

    print(base_template)
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
