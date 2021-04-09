from django.db import models


class Note(models.Model):
    author = models.CharField(max_length=32, default='admin')
    body = models.TextField(max_length=300)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body
