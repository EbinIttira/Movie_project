from django.db import models
class movies(models.Model):
    name=models.CharField(max_length=50)
    desc=models.TextField(max_length=250)
    year=models.IntegerField()
    img=models.ImageField(upload_to='gallery')

    def __str__(self):
        return self.name