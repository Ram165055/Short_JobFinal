from django.db import models
from phone_field import PhoneField

# Create your models here.
class Destination(models.Model):
    # id:int
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()
    skill=models.CharField(blank=True,max_length=100,default="Gardening")
    price=models.IntegerField()
    location=models.CharField(blank=True,max_length=100,default="bhilai")
    offer=models.BooleanField(default=False)
    phone = PhoneField(blank=True, help_text='Contact phone number')



class Article(models.Model):
    author = models.ForeignKey('auth.User', on_delete = models.CASCADE,)
    title = models.CharField(max_length = 100)
    body = models.TextField()
    def __str__(self):
        return self.title



class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    intro = models.TextField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
    	ordering = ['-date_added']




class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
