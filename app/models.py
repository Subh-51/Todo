from django.db import models

# Create your models here.
class Todo(models.Model):
    slno = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    desc = models.TextField()
    
    
    def __str__(self):
        return self.title[:10]+'..........'