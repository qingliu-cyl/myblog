from django.db import models

# Create your models here.
class SgFlag(models.Model):
    qqnumber = models.CharField(max_length = 11)
    email = models.CharField(max_length = 30,null = True,blank = False)
    flag = models.TextField(null = True,blank = False)
