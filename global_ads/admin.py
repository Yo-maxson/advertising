from django.contrib import admin
from .models import Advert


@admin.register(Advert)
class AdvertModelAdmin(admin.ModelAdmin):
    list_display = ["name", "pub_date", "price"]
    search_fields = [
        "name",
    ]
