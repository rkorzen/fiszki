from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Card


# Register your models here.


class CardResource(resources.ModelResource):
    class Meta:
        model = Card
        fields = "__all__"


@admin.register(Card)
class CardAdmin(ImportExportModelAdmin):
    resource_class = CardResource
    list_display = ["question", "answer", "box"]


# admin.site.register(Card, CardAdmin)
