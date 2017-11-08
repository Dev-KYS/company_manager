from django.db import models

# Create your models here.
class Code_model(models.Model):
    grp_cd = models.CharField(max_length=10, primary_key=True)
    cd = models.CharField(max_length=10, primary_key=True)
    cd_nm = models.CharField(max_length=10)
    option = models.CharField(max_length=10)
    class Meta:
        db_table = 't_code'

