from django.db import models
from django.utils.translation import ugettext_lazy as _


class MobileCategoryModel(models.Model):
    title = models.CharField(max_length=50, verbose_name=_('Title'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


class PhoneModel(models.Model):
    category = models.ForeignKey(
        MobileCategoryModel,
        on_delete=models.PROTECT,
        related_name='phones',
        verbose_name=_('Category')
    )
    image = models.ImageField(upload_to='phone', verbose_name=_('Image'))
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    price = models.FloatField(verbose_name=_('Price'))
    little_about = models.TextField(verbose_name=_('Little About'))
    more_about = models.TextField(verbose_name=_('More About'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Phone')
        verbose_name_plural = _('Phones')


class WindowModel(models.Model):
    category = models.ForeignKey(
        MobileCategoryModel,
        on_delete=models.PROTECT,
        related_name='windows',
        verbose_name=_('Category')
    )
    image = models.ImageField(upload_to='phone', verbose_name=_('Image'))
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    price = models.FloatField(verbose_name=_('Price'))
    little_about = models.TextField(verbose_name=_('Little About'))
    more_about = models.TextField(verbose_name=_('More About'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Window')
        verbose_name_plural = _('Windows')


class ProtectionModel(models.Model):
    category = models.ForeignKey(
        MobileCategoryModel,
        on_delete=models.PROTECT,
        related_name='protections',
        verbose_name=_('Category')
    )
    image = models.ImageField(upload_to='phone', verbose_name=_('Image'))
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    price = models.FloatField(verbose_name=_('Price'))
    little_about = models.TextField(verbose_name=_('Little About'))
    more_about = models.TextField(verbose_name=_('More About'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Protection')
        verbose_name_plural = _('Protections')
