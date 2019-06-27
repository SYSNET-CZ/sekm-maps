from djgeojson.fields import PolygonField
from django.db import models
from django.conf import settings

class ObjectSpot(models.Model):

    title = models.CharField(max_length=256)
    description = models.TextField()
    type = models.CharField(max_length=16)
    picture = models.ImageField(upload_to=settings.IMAGE_DIR)
    geom = PolygonField()

    def __unicode__(self):
        return self.title

    @property
    def picture_url(self):
        return self.picture.url
