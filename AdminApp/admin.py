from django.contrib import admin #username = admin
from AdminApp.models import Category,Book#password = yash@1234

class CategoryAdmin(admin.ModelAdmin):
    list_display=['id','cat_name']
class BookAdmin(admin.ModelAdmin):
    list_display = ['id','book_name','author','price','description','image_url','category']

admin.site.register(Book,BookAdmin)
admin.site.register(Category,CategoryAdmin)
