from django.db import models

# Create your models here.
class storeUserInfo(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    age = models.IntegerField(max_length=5)
    gender = models.CharField(max_length=30)
    image = models.ImageField(upload_to='save')
    user_id = models.IntegerField(max_length=5)
