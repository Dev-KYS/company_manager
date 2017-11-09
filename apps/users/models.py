from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from apps.teams.models import Team
import uuid

class MyUserManager(BaseUserManager):
    def _create_user(self, username, password, **extra_kwargs):
        user = self.model(username=username, **extra_kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, **extra_kwargs):
        extra_kwargs.setdefault('is_active', True)
        extra_kwargs.setdefault('is_superuser', True)
        extra_kwargs.setdefault('is_staff', True)

        if extra_kwargs.get('is_superuser', None) is not True:
            raise ValueError('관리자 권한이 필요합니다.')

        return self._create_user(username, password, **extra_kwargs)


class MyUser(AbstractBaseUser):
    """
    유저 모델
    """
    POSITION_TYPES = (
        ('a', '대표'),
        ('b', '팀장'),
        ('c', '과장'),
        ('d', '대리'),
        ('e', '주임'),
        ('f', '사원'),
        ('g', '인턴'),
    )
    uid = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
        verbose_name='팀 고유 아이디'
    )
    username = models.CharField(
        max_length=20,
        unique=True,
        verbose_name='아이디'
    )
    name = models.CharField(
        max_length=10,
        verbose_name='이름'
    )
    email = models.EmailField(
        verbose_name='이메일'
    )
    team = models.ForeignKey(
        Team,
        verbose_name='소속',
        null=True,
        blank=True
    )
    position = models.CharField(
        max_length=2,
        choices=POSITION_TYPES,
        default='g',
        verbose_name='직급'
    )
    birth = models.DateField(
        null=True,
        blank=True,
        verbose_name='생일'
    )
    date_joined = models.DateField(
        null=True,
        blank=True,
        verbose_name='입사일'
    )
    date_exited = models.DateField(
        null=True,
        blank=True,
        verbose_name='퇴사일'
    )
    is_superuser = models.BooleanField(
        default=False,
        verbose_name='관리자 여부'
    )
    is_staff = models.BooleanField(
        default=False,
        verbose_name='스태브 여부'
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='활성화 여부'
    )

    objects = MyUserManager()

    USERNAME_FIELD = 'username'


    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.name

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, module):
        return True