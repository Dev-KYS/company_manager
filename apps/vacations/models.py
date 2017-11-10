from django.db import models
from django.conf import settings
from apps.users.models import MyUser


class Vacation(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        verbose_name='유저'
    )
    vacation_type = models.ForeignKey(
        'VacationCode',
        verbose_name='연차 종류',
        null=False,
        blank=False
    )
    start = models.DateField(
        verbose_name='연차 시작'
    )
    end = models.DateField(
        verbose_name='연차 끝'
    )
    first_approval = models.CharField(
        max_length=2,
        default='',
        verbose_name='첫 승인 여부'
    )
    last_approval = models.CharField(
        max_length=2,
        default='',
        verbose_name='마지막 승인 여부'
    )
    reason = models.TextField(
        verbose_name='사유'
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='생성일'
    )
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name='수정일'
    )
    first_approval_user = models.ForeignKey(
        MyUser,
        verbose_name='1차 승인자',
        null=True,
        blank=True,
        related_name='first_approval_user'
    )
    last_approval_user = models.ForeignKey(
        MyUser,
        verbose_name='최종 승인자',
        null=True,
        blank=True,
        related_name='last_approval_user'
    )


    class Meta:
        db_table = 'vacations'
        verbose_name = '연차'
        verbose_name_plural = '연차들'

    def __str__(self):
        return str(self.user)


class VacationCode(models.Model):
    codename = models.CharField(
        max_length=10,
        verbose_name='연차 명'
    )

    minus_day = models.FloatField(
        verbose_name='차감일수'
    )

    class Meta:
        db_table='vacation_code'

    def __str__(self):
        return self.codename