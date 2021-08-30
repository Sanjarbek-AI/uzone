from django.db import models
from django.utils.translation import ugettext_lazy as _


class ChargerCategoryModel(models.Model):
    title = models.CharField(max_length=50, verbose_name=_('Title'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Charger Category')
        verbose_name_plural = _('Charger Categories')


class ChargerModel(models.Model):
    category = models.ForeignKey(
        ChargerCategoryModel,
        on_delete=models.PROTECT,
        related_name='chargers',
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
        verbose_name = _('Charger')
        verbose_name_plural = _('Chargers')


class EarphoneCategoryModel(models.Model):
    title = models.CharField(max_length=50, verbose_name=_('Title'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Charger Category')
        verbose_name_plural = _('Charger Categories')


class EarphoneModel(models.Model):
    category = models.ForeignKey(
        ChargerCategoryModel,
        on_delete=models.PROTECT,
        related_name='earphones',
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
        verbose_name = _('Charger')
        verbose_name_plural = _('Chargers')


class MusicPlayerModel(models.Model):
    image = models.ImageField(upload_to='Chargers', verbose_name=_('Image'))
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    price = models.FloatField(verbose_name=_('Price'))
    little_about = models.TextField(verbose_name=_('Little About'))
    more_about = models.TextField(verbose_name=_('More About'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Music Player')
        verbose_name_plural = _('Music Players')


class PowerBankModel(models.Model):
    image = models.ImageField(upload_to='PowerBanks', verbose_name=_('Image'))
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    price = models.FloatField(verbose_name=_('Price'))
    little_about = models.TextField(verbose_name=_('Little About'))
    more_about = models.TextField(verbose_name=_('More About'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('PowerBank')
        verbose_name_plural = _('PowerBanks')
