from django.db import models

# Create your models here.

class Post(models.Model):
    content = models.TextField()
    title = models.CharField(max_length=200)
    date_pub = models.DateTimeField()
    description = models.TextField()

    '''
    def __str__(self):
        return self.title
    '''
        
