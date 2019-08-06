from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    phone = models.CharField(_('phone number'), max_length=30, blank=True)
    address = models.CharField(_('reseller address'), max_length=220, blank=True)


class OneL(models.Model):
    lno = models.CharField(_('1000ks lottery'), max_length=8, unique=True)
    name = models.CharField(_('customer name'), max_length=100, )
    reseller = models.ForeignKey('lotto_app.User', on_delete=models.CASCADE)
    phone = models.CharField(_('customer phone'), max_length=33, )
    address = models.CharField(_('customer address'), max_length=200, )
    is_winner = models.CharField(_('is lottery winner'), default=0, max_length=1)
    prize_details = models.CharField(_('winning prize detail'), max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    nth = models.CharField(_('nth of lottery'), max_length=5, default=375, )

    def __str__(self):
        return self.lno

    class Meta:
        ordering = ('-created_at',)


class FiveL(models.Model):
    lno = models.CharField(_('500ks lottery'), max_length=8, unique=True)
    name = models.CharField(_('customer name'), max_length=100, )
    reseller = models.ForeignKey('lotto_app.User', on_delete=models.CASCADE)
    phone = models.CharField(_('customer phone'), max_length=33, )
    address = models.CharField(_('customer address'), max_length=200, )
    is_winner = models.CharField(_('is lottery winner'), default=0, max_length=1)
    prize_details = models.CharField(_('winning prize detail'), max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    nth = models.CharField(_('nth of lottery'), max_length=5, default=375, )

    def __str__(self):
        return self.lno

    class Meta:
        ordering = ('-created_at',)


class TwoL(models.Model):
    lno = models.CharField(_('200ks lottery'), max_length=8, unique=True)
    name = models.CharField(_('customer name'), max_length=100, )
    reseller = models.ForeignKey('lotto_app.User', on_delete=models.CASCADE)
    phone = models.CharField(_('customer phone'), max_length=33, )
    address = models.CharField(_('customer address'), max_length=200, )
    is_winner = models.CharField(_('is lottery winner'), default=0, max_length=1)
    prize_details = models.CharField(_('winning prize detail'), max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    nth = models.CharField(_('nth of lottery'), max_length=5, default=375, )

    def __str__(self):
        return self.lno

    class Meta:
        ordering = ('-created_at',)
