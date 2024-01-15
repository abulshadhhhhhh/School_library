from django.db import models
from datetime import date
# Create your models here.
class Register(models.Model):
  name = models.CharField(max_length=50)
  phone = models.CharField(max_length=10)
  email = models.CharField(max_length=50)
  username = models.CharField(max_length=50)
  password = models.CharField(max_length=50)
  type = models.IntegerField(null=True)

  def __str__(self):
    return self.name

# class Login(models.Model):
#   username = models.CharField(max_length=50)
#   password = models.CharField(max_length=50)
#
#
#   def __str__(self):
#     return self.username

class Book(models.Model):
  bookname = models.CharField(max_length=100)
  author = models.CharField(max_length=100)
  genre = models.CharField(max_length=100)
  description = models.TextField(max_length=5000)
  image = models.ImageField()

  def __str__(self):
    return self.bookname

class Issue(models.Model):
    username=models.ForeignKey(Register,on_delete=models.CASCADE)
    bookname=models.ForeignKey(Book,on_delete=models.CASCADE)
    issuedate = models.DateField(default=date.today, blank=False)

    def __str__(self):
     return self.username.username

