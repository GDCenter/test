from django.db import models
from django.core.validators import MaxValueValidator




class Rank(models.Model):

    clients = models.CharField(max_length=128,verbose_name='客户端号',null=False)

    score = models.IntegerField(validators=[MaxValueValidator(10000000)])


