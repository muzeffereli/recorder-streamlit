from django.db import models


class Post(models.Model):

    text = models.TextField()
    # audio_bytes = models.TextField(blank=True, null=True)
    audio = models.FileField(upload_to='audio', blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
