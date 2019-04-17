from django.db import models

# Create your models here.

class blogUser(models.Model):
  def __str__(self):
    return self.userName
  userName = models.CharField(max_length=200)

class blogPost(models.Model):
  def __str__(self):
    return (self.postName, self.postUrl)
  postName = models.TextField(default='postname')
  userName = models.ForeignKey(blogUser, on_delete=models.CASCADE)
  dateCreated = models.DateTimeField()
  dateUpdated = models.DateTimeField()
  postUrl = models.TextField(default='oldmanreffi.com/read/')

