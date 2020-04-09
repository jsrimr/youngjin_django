from django.db import models

# Create your models here.


from django.contrib.auth import get_user_model
User = get_user_model() # This allows you to get the current user logged into a session.


class Group(models.Model):
    dpt_code = models.CharField(max_length=255, unique= True, default = '')
    dpt_name = models.CharField(max_length=255, unique=True, default = '')

    def __str__(self):
        return self.dpt_name

    class Meta:
        ordering = ['dpt_code']