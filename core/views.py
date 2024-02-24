from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django import forms
from .models import Account


class ListAccounts(ListView):
    model = Account

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        if self.request.htmx:
            base_template = "_partial.html"
            message = "Hello from Server + HTMX"
        else:
            base_template = "_base.html"
            message = "Hello from Server"
        context["base_template"] = base_template
        context["message"] = message
        return context

class CreateAccount(SuccessMessageMixin, CreateView):
    model = Account
    form = Account

    fields = "__all__"
    success_url = "/accounts"
    success_message = 'Cuenta creada correctamente'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        if self.request.htmx:
            base_template = "_partial.html"
            message = "Hello from Server + HTMX"
        else:
            base_template = "_base.html"
            message = "Hello from Server"
        context["base_template"] = base_template
        context["message"] = message

        return context


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
