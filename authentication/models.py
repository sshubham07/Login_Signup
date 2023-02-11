from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    email_token=models.CharField(max_length=100)
    is_varified=models.BooleanField(default=False)
