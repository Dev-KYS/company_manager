from django.db import models
from django.conf import settings


class Vacation(models.Model):
    VACATION_TYPES = (
        ('a', '연차'),
        ('b', '오전 반차'),
        ('c', '오후 반차'),
        ('d', '공가'),
        ('e', '병가'),
        ('e', '건강검진'),
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        verbose_name='유저'
    )
    vacation_type = models.CharField(
        max_length=2,
        choices=VACATION_TYPES,
        default='a',
        verbose_name='연차 종류'
    )
    start = models.DateField(
        verbose_name='연차 시작'
    )
    end = models.DateField(
        verbose_name='연차 끝'
    )
    first_approval = models.BooleanField(
        default=False,
        verbose_name='첫 승인 여부'
    )
    last_approval = models.BooleanField(
        default=False,
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


    class Meta:
        db_table = 'vacations'
        verbose_name = '연차'
        verbose_name_plural = '연차들'

    def __str__(self):
        return str(self.user)
