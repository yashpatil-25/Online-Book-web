from django.db import models
from AdminApp.models import Book
# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(max_length=20,primary_key=True)
    password= models.CharField(max_length=20)

    class Meta:
        db_table = "UserInfo"

class MyCart(models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    user = models.ForeignKey(UserInfo,on_delete=models.CASCADE)
    qty = models.IntegerField(default=2)

    class Meta:
        db_table = "MyCart"