import os

from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
class CustomUser(AbstractUser):
    image = models.ImageField(upload_to='userimages/')

    def get_filename(self):
        return os.path.basename(self.file.name)

