from django.db import models

class Trip(models.Model):
    title = models.CharField(max_length=200)
    start_location = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class Location(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='locations')
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=500)
    latitude = models.FloatField()
    longitude = models.FloatField()
    order = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order']
