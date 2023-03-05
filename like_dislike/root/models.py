from django.db import models

# Create your models here.
class Like(models.Model):
    like = models.IntegerField(default=0)
     
    # def __str__(self):
    #     return self.like
    