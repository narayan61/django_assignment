from django.contrib import admin
from app.models import Book
# Register your models here.
 
@admin.register(Book)
class BookModelAdmin(admin.ModelAdmin):
    list_display=['id','user','bookname','author','catagory','discription']

 