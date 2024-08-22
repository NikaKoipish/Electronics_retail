from django.contrib import admin

from retail.models import NetworkUnit, Product


@admin.action(description='Очистить задолженность перед поставщиком')
def clear_debt(modeladmin, request, queryset):
    queryset.update(debt=0.00)


@admin.register(NetworkUnit)
class NetworkUnitAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "country",
        "city",
        "level",
        "supplier",
        "debt",
        "date_of_create",
    )
    list_filter = ("city",)
    search_fields = ("name",)
    actions = [clear_debt]
    list_display_links = ['supplier']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "product_model",
        "release_date",
        "network_unit",
    )
    list_filter = ("network_unit",)
    search_fields = ("name",)
    list_display_links = ['network_unit']

