from django.db import models


class Comment(models.Model):
    title = models.CharField(max_length=200)
    username = models.CharField(max_length=100)
    reply = models.ForeignKey('Comment', null=True, blank=True, related_name='replies', on_delete=models.DO_NOTHING)
    created_on = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    to_show = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class AddNews(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    email = models.EmailField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    source = models.CharField(max_length=200,blank=True)
    category = models.CharField(max_length=200,blank=True)
    to_publish = models.BooleanField(default=False)

    def __str__(self):
        return self.title