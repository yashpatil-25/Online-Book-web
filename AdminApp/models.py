from django.db import models

# Create your models here.
class Category (models.Model):
    cat_name = models.CharField(max_length=20)

    class Meta:
        db_table = "Category"

    def __str__(self):
        return self.cat_name
    
class Book(models.Model):
    book_name = models.CharField(max_length=20)
    author = models.CharField(max_length=20)
    price = models.FloatField(default=500)
    description =models.CharField(max_length=500)
    image_url = models.ImageField(default="abc.jpg",upload_to="media/Images/")
    category =models.ForeignKey(Category,on_delete=models.CASCADE)

    class Meta:
        db_table = "Book"

    def __str__(self):
        return self.book_name
