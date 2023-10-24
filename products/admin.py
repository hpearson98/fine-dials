from django.contrib import admin
from .models import Brand, Watch
# Register your models here.


class WatchAdmin(admin.ModelAdmin):
    list_display = [
        'brand',
        'model',
        'style',
        'price',
        'image',
    ]


class BrandAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'country_of_origin',
        'year_established',
    ]


admin.site.register(Brand, BrandAdmin)
admin.site.register(Watch, WatchAdmin)
