from django.contrib import admin

from .models import GeneralSettings


@admin.register(GeneralSettings)
class GeneralSettingsAdmin(admin.ModelAdmin):
    exclude = ["key", ]
