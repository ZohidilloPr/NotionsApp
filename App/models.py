from django.db import models

# Create your models here.

class NotionModel(models.Model):
    aim = models.CharField(max_length=100)
    about = models.TextField()
    impt = models.BooleanField(default=False)
    comp = models.BooleanField(default=False)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.aim

    def __unicode__(self):
        return self.aim
