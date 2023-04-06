from django.contrib import admin

from .models import Categories, ContactUs


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


class ContactUsAdmin(admin.ModelAdmin):
    list_display = ("email", "topic", "text", "sending_datetime",)
    search_fields = ("email", "topic", "sending_datetime",)


admin.site.register(Categories, CategoriesAdmin)
admin.site.register(ContactUs, ContactUsAdmin)
