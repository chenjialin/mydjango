from django.db import models


# Create your models here.
class Music_info(models.Model):
    artist = models.CharField(max_length=50)
    artistLink = models.CharField(max_length=200)
    album = models.CharField(max_length=200)
    albumLink = models.CharField(max_length=200)
    albumPrice = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    coverArt = models.CharField(max_length=200)
    releasedate = models.CharField(max_length=200)

    def __str__(self):
        return "%s (%s)" % (self.artist, self.artistLink)