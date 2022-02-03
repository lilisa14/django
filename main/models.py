from django.db import models


class Task(models.Model):
    title = models.CharField ('name', max_length= 100)
    task = models.TextField ('')

def __str__(self):
    return self.title