from django.db import models
from django.utils.translation import gettext


class GeneralSettings(models.Model):
    """
    Easy way to ensure that only one tuple is used for actual data storage.
    """
    key = models.CharField(max_length=16, default="general_settings", primary_key=True)

    """
    When template_debugging = True, show a special sign near whatever text is rendered
    from the database (phones, emails etc.)
    """
    template_debugging = models.BooleanField(default=False,
                                             verbose_name=gettext("Template debugging"))

    def __str__(self):
        return gettext("General sertings")

    class Meta:
        verbose_name = gettext("General sertings")
        verbose_name_plural = verbose_name
