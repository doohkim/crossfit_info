from django.db import models

from boxes.models import Box


class Coach(models.Model):
    box = models.ForeignKey(Box, on_delete=models.CASCADE)
    coachName = models.CharField(max_length=100, help_text='코치 이름')
