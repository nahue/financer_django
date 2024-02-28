from django.db import models
from djmoney.models.fields import MoneyField

class TimestampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Account(TimestampedModel):
    name = models.CharField(max_length=200)



class Debt(TimestampedModel):
    label = models.CharField(max_length=200)
    currency = models.CharField(max_length=5)
    amount = MoneyField(max_digits=14, decimal_places=2, default_currency='ARS')
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

class Transaction(TimestampedModel):
    label = models.CharField(max_length=200)
    amount = MoneyField(max_digits=14, decimal_places=2, default_currency='ARS')
    date = models.DateTimeField(auto_now_add=True, null=True)
    debt = models.ForeignKey("Debt", on_delete=models.CASCADE, null=True, blank=True)
