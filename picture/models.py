from django.db import models

# Create your models here.


class Picture(models.Model):
    name = models.CharField(max_length=50)
    time = models.DateField()
    author = models.CharField(max_length=20)
    label = models.CharField(max_length=50)

    def __str__(self):
        return 'Picture'+str(self.id) + ' ' + self.name + ' ' + str(self.time) + ' ' + self.author + ' ' + self.label
