from django.db import models

class studentclass(models.Model):
      name=models.CharField( max_length=50)
      age=models.IntegerField()
      id = models.AutoField(primary_key=True)

def __str__(self) :
            return self.name