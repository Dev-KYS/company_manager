from django.db import models

# Create your models here.
class Team_model(models.Model):
    team_cd = models.CharField(max_length=10, primary_key=True)
    team_nm = models.CharField(max_length=10)
    upper_team = models.CharField(max_length=10, null=True)
    created_at = models.DateField()
    class Meta:
        db_table = 't_team'