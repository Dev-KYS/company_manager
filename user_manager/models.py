from django.db import models

class Register_model(models.Model):
    user_id = models.CharField(max_length=20)
    user_pw = models.CharField(max_length=255)
    user_nm = models.CharField(max_length=5)
    email = models.EmailField(max_length=50)
    position = models.CharField(max_length=5)
    v_day = models.IntegerField()
    join_day = models.DateField()
    exit_day = models.DateField()



