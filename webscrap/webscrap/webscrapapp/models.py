from importlib.resources._common import _

from django.db import models

# Create your models here.
class Links(models.Model):
    def __str__(self):
        return self.stringname
    address=models.CharField(max_length=300,null=True,blank=True)
    stringname=models.CharField(max_length=300,null=True,blank=True)