from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    
    user            = models.ForeignKey(User, unique=True)

    def __unicode__(self):
        return str(self.user.username)
# Create your models here.
