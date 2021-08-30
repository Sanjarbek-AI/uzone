from django.db import models
from django.utils.translation import ugettext_lazy as _


class SmartwatchCategoryModel(models.Model):
    title = models.CharField(max_length=50, verbose_name=_('Title'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Smartwatch Category')
        verbose_name_plural = _('Smartwatch Categories')


class SmartwatchModel(models.Model):
    category = models.ForeignKey(
        SmartwatchCategoryModel,
        on_delete=models.PROTECT,
        related_name='smartwatches',
        verbose_name=_('Category')
    )
    image = models.ImageField(upload_to='Chargers', verbose_name=_('Chargers'))
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    price = models.FloatField(verbose_name=_('Price'))
    little_about = models.TextField(verbose_name=_('Little About'))
    more_about = models.TextField(verbose_name=_('More About'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Smartwatch')
        verbose_name_plural = _('Smartwatches')
