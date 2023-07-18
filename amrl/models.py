#from django.utils import timezone
from django.contrib.gis.db import models 



class Writer(models.Model):
    name = models.TextField()
    birth_date = models.DateField()
    nationality = models.TextField()

    def __str__(self): 
        return self.name


class Route(models.Model):
    name = models.TextField(unique=True)
    city = models.TextField()
    writer = models.ManyToManyField(Writer)

    def __str__(self): 
        return self.name

class Point(models.Model):
    title = models.TextField()
    text = models.TextField(null=True, blank=True)
    sequence_number = models.IntegerField()
    location = models.PointField()
    speech_file = models.FileField(upload_to="speech/", null=True, blank=True)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['route', 'sequence_number']

    def __str__(self):
        return self.title


class PointImage(models.Model):
    name = models.TextField()
    caption = models.TextField()
    image = models.ImageField(upload_to="point/", null=True)
    point = models.ForeignKey(Point, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
