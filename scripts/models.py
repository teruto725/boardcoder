from django.db import models

# Create your models here.
from accounts.models import CustomUser


class Script(models.Model):
    name = models.CharField(max_length=30)
    gamename = models.CharField(max_length=30)
    file = models.FileField(upload_to='scripts/')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    language = models.CharField(max_length=20)


