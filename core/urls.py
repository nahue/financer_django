from django.urls import include, path
from . import views

app_name = 'core'
urlpatterns = [
    path("", views.index),
    path("accounts", views.ListAccounts.as_view(), name = "accounts"),
    path("accounts/new", views.CreateAccount.as_view(), name = "new_account"),
    path("accounts/<int:pk>/edit", views.UpdateAccount.as_view(), name = "update_account"),
    path("transacciones", views.transacciones),
    path("deudas", views.deudas)
]
