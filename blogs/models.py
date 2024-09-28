from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

