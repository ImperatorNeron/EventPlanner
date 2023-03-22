from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=25, blank=False, null=False)

    class Meta:
        verbose_name = "Категорію"
        verbose_name_plural = "Категорії"
        ordering = ["name"]
