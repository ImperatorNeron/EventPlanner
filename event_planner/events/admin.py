from django.contrib import admin

from .models import Categories


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


admin.site.register(Categories, CategoriesAdmin)
