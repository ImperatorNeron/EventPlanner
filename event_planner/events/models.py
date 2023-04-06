from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=25, blank=False, null=False)

    class Meta:
        verbose_name = "Категорію"
        verbose_name_plural = "Категорії"
        ordering = ["name"]


class ContactUs(models.Model):
    email = models.EmailField(blank=False, null=False)
    topic = models.CharField(max_length=50, blank=False, null=False)
    text = models.TextField(blank=False, null=False)
    sending_datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Повідомлення"
        ordering = ["sending_datetime"]

