from django.conf import settings
from django.db import models
from rest_framework.authtoken.admin import User


class AdvertisementStatusChoices(models.TextChoices):
    """Статусы объявления."""

    OPEN = "OPEN", "Открыто"
    CLOSED = "CLOSED", "Закрыто"


class Advertisement(models.Model):
    """Объявление."""

    title = models.TextField()
    description = models.TextField(default='')
    status = models.TextField(
        choices=AdvertisementStatusChoices.choices,
        default=AdvertisementStatusChoices.OPEN
    )
    creator = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )
    draft = models.BooleanField(default=False)
    '''
    favourite = models.ManyToManyField(
        User,
        related_name='favourites',
        through='FavouriteAdvertisement'
    )


class FavouriteAdvertisement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
'''