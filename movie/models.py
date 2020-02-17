from django.db import models

# Create your models here.


class Movie(models.Model):
    status = models.IntegerField(default=0)
    rate = models.FloatField(default=0)
    url = models.CharField(max_length=50)
    changed = models.IntegerField(default=0)

    def __str__(self):
        return 'Movie' + str(self.status) + ' ' + str(self.rate) + ' ' + self.url + ' ' + self.changed
