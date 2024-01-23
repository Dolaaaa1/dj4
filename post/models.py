from django.db import models
from django.utils import timezone
# Create your models here.

CATEGORY_CHOICES =(
    ("WB","Web Development"),
    ("DS", "Data Science"),
)



class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    published_at = models.BooleanField(default=True)
    email = models.EmailField( max_length=254, null=True , blank=True)
    views_count= models.IntegerField(default=0)
    category = models.CharField(choices= CATEGORY_CHOICES, max_length=20)
    
    
    
    def __str__(self):
        return self.title
