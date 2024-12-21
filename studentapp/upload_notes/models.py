from django.db import models

class NoteImage(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='notes/')
    subject = models.CharField(max_length=50, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

