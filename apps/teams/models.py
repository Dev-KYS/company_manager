from django.db import models
from django.conf import settings
import uuid


class Team(models.Model):
    tid = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
        verbose_name='팀 고유 아이디'
    )
    name = models.CharField(
        max_length=20,
        verbose_name='팀 이름'
    )
    members = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        blank=True,
        verbose_name='팀 멤버'
    )
    created = models.DateField(
        null=True,
        blank=True,
        verbose_name='팀 생성일'
    )


    class Meta:
        db_table = 'teams'
        verbose_name = '팀'
        verbose_name_plural = '팀들'

    def __str__(self):
        return self.name