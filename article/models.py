from django.db import models


class Article(models.Model):
    name = models.CharField(max_length=20)
    time = models.DateField()
    author = models.CharField(max_length=20)
    label = models.CharField(max_length=20)

    def __str__(self):
        return 'Article'+str(self.id) + ' ' + self.name + ' ' + str(self.time) + ' ' + self.author + ' ' + self.label


class Picture(models.Model):
    name = models.CharField(max_length=20)
    time = models.DateField()
    author = models.CharField(max_length=20)
    label = models.CharField(max_length=20)

    def __str__(self):
        return 'Picture'+str(self.id) + ' ' + self.name + ' ' + str(self.time) + ' ' + self.author + ' ' + self.label