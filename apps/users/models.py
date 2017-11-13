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
    position = models.ForeignKey(
        'UserCode',
        verbose_name='직급',
        null=True,
        blank=True
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
    v_day = models.IntegerField(
        null=False,
        blank=False,
        verbose_name='잔여 연차일',
        default=0
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
        verbose_name = '사용자'

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


class UserCode(models.Model):

    code = models.CharField(
        primary_key=True,
        max_length=10,
        verbose_name='직급 코드',
        null=False,
        blank=False
    )

    codename = models.CharField(
        max_length=5,
        verbose_name='직급명',
        null=False,
        blank=False
    )

    sort = models.IntegerField(
        verbose_name='순서',
        null=False,
        blank=False,
        unique=True
    )

    class Meta:
        db_table = 'user_code'
        verbose_name = '직급코드'

    def __str__(self):
        return self.codename


class Grant(models.Model):
    user = models.ForeignKey(
        'MyUser',
        null=True,
        blank=True,
        verbose_name='사용자'
    )

    agent = models.ForeignKey(
        'Agent',
        null=True,
        blank=True,
        verbose_name='대리인'
    )

    class Meta:
        db_table = 'grants'
        verbose_name = '권한'

    def __str__(self):
        return self.user.name


class Agent(models.Model):
    user = models.ForeignKey(
        'MyUser',
        null=False,
        blank=False,
        verbose_name='대리인'
    )

    start = models.DateField(
        null=False,
        blank=False,
        verbose_name='시작일'
    )

    end = models.DateField(
        null=False,
        blank=False,
        verbose_name='종료일'
    )

    class Meta:
        db_table = 'agents'
        verbose_name = '대리인'

    def __str__(self):
        return self.user.name