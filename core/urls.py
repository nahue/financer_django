from django.urls import include, path
from . import views

app_name = 'core'

urlpatterns = [
    path("", views.index),
    path("accounts", views.ListAccounts.as_view(), name = "account-list"),
    path("accounts/new", views.CreateAccount.as_view(), name = "account-new"),
    path("accounts/<int:pk>/edit", views.UpdateAccount.as_view(), name = "account-update"),
    path("accounts/<int:pk>/delete", views.DeleteAccount.as_view(), name = "account-delete"),
    path("transacciones", views.transacciones),
    path("deudas", views.deudas)
]
