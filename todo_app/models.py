from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    content = models.CharField(max_length = 100)
    owner = models.ForeignKey(User,on_delete = models.CASCADE)

    def __str__(self):
        # return (f"{owner}-{self.content}")
        return (self.owner, self.content)