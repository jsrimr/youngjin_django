# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.timezone import now
from django.db import models

from groups.models import Group

from django.contrib.auth import get_user_model
User = get_user_model() # This allows you to get the current user logged into a session.


# Create your models here.

class Log(models.Model):

    group = models.ForeignKey(Group, related_name='view_page', on_delete=models.CASCADE, default = '')
    user = models.ForeignKey(User, related_name='view_page', on_delete=models.CASCADE, default = '')

    log_date = models.DateTimeField(default=now)
    log_time = models.DateTimeField(default=now)
    log_userid = models.CharField(max_length=60)
    log_question = models.TextField(default='질문')
    log_answer = models.TextField(default='답변')

    def __str__(self):
        return self.log_question
