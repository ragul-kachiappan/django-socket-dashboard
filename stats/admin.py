from django.contrib import admin

from stats import models

# Register your models here.

admin.site.register(models.Statistic)
admin.site.register(models.DataItem)
