from django.contrib import admin
from .models import Brand, Watch, Review
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

class ReviewAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'watch',
        'title',
    ]


admin.site.register(Brand, BrandAdmin)
admin.site.register(Watch, WatchAdmin)
admin.site.register(Review, ReviewAdmin)
