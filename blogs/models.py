from django.db import models

from users.models import MyUser

class blog_category(models.Model):
    category_name =  models.CharField(max_length=266,blank=True)
    createdAt = models.DateTimeField( auto_now=True)
    
class blogs(models.Model):
    author = models.ForeignKey(MyUser,  on_delete=models.CASCADE)
    created_by = models.CharField(max_length=266,blank=True)
    content= models.TextField(blank=True)
    summary = models.TextField( blank=True)
    category = models.CharField(max_length=200, blank=True)
    file = models.FileField( upload_to='posts', max_length=100 , blank=True)
    title = models.CharField( max_length=255, blank=True)
    referel_link = models.CharField( max_length=50, blank=True)
    createdAt = models.DateTimeField( auto_now=True)