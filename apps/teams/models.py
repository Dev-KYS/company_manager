from django.db import models

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
    
    team_master = models.ForeignKey(
        'users.MyUser',
        null=True,
        blank=True,
        verbose_name='그룹장',
        related_name='team_master'
    )

    upper_team = models.ForeignKey(
        'Team',
        null=True,
        blank=True,
        default=None,
        verbose_name='상위그룹'
    )

    created = models.DateField(
        null=True,
        blank=True,
        verbose_name='팀 생성일'
    )

    class Meta:
        db_table = 'teams'
        verbose_name = '팀'


    def __str__(self):
        return self.name