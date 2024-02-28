from django.urls import include, path
from . import views

app_name = 'core'

urlpatterns = [
    path("", views.index),
    path("accounts", views.ListAccounts.as_view(), name = "account-list"),
    path("accounts/new", views.CreateAccount.as_view(), name = "account-new"),
    path("accounts/<int:pk>/edit", views.UpdateAccount.as_view(), name = "account-update"),
    path("accounts/<int:pk>/delete", views.DeleteAccount.as_view(), name = "account-delete"),

    path("transactions", views.ListTransactions.as_view(), name = "transaction-list"),
    path("transactions/new", views.CreateTransaction.as_view(), name = "transaction-new"),
    path("transactions/<int:pk>/edit", views.UpdateTransaction.as_view(), name = "transaction-edit"),
    path("transactions/<int:pk>/delete", views.DeleteTransaction.as_view(), name = "transaction-delete"),

    path("deudas", views.deudas)
]
