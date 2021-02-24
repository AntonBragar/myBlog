from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=150)
    date = models.DateTimeField()
    text = models.TextField()
    image = models.ImageField(upload_to='post_images/')

    def __str__(self):
        return self.title
