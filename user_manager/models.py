from django.db import models
from code_manager.models import Code_model
from team_manager.models import Team_model

class Register_model(models.Model):
    user_id = models.CharField(max_length=20, primary_key=True, unique=True)
    user_pw = models.CharField(max_length=255)
    user_nm = models.CharField(max_length=5)
    email = models.EmailField(max_length=50, null=True)
    position = models.ForeignKey(Code_model, to_field='cd', related_name='position_code') # join구문을 사용할시 타겟이 되는 모델(pk가 있는)을 참조, 중복시에 related_name으로 중복해결
    v_day = models.IntegerField(null=True)
    join_day = models.DateField()
    exit_day = models.DateField(null=True)
    birth = models.DateField(null=True)
    last_login = models.DateTimeField(null=True)
    user_grade = models.CharField(max_length=10, null=True)
    agent = models.CharField(max_length=20, null=True)
    team = models.ForeignKey(Team_model)
    master = models.CharField(max_length=2, null=True)
    class Meta:
        db_table = 't_user'





