from django.db import models
from user_manager.models import Register_model
from code_manager.models import Code_model

class Vacation_model(models.Model):
    user = models.ForeignKey(Register_model)
    type = models.ForeignKey(Code_model, to_field='cd')
    sta_dt = models.DateField()
    end_dt = models.DateField()
    first_approval = models.CharField(max_length=2)
    last_approval = models.CharField(max_length=2)
    created_at = models.DateTimeField(auto_now_add=True)
    reason = models.TextField()
    class Meta:
        db_table = 't_vacation'