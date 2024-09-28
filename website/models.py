from django.db import models

class Question(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=250)
    text = models.TextField()

    def __str__(self):
        return self.name



