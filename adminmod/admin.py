from django.contrib import admin
from .models import SalesSummary


@admin.register(SalesSummary)
class SalesSummaryAdmin(ModelsAdmin):
    change_list_template = 'admin/sale_summary_change_list.html'
    date_hierarchy = 'created'
