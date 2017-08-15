from django.db import models


class SalesSummary(Sales):
    class Meta:
        proxy = True
        verbose_name = 'Sale Summary'
        verbose_name_plural = 'Sales Summary'
