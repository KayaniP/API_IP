from django.db import models

class Snippet(models.Model):
    ip = models.CharField(max_length=100)

    def __str__(self):
        return self.ip