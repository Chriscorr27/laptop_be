from django.contrib import admin
from .models import*

# Register your models here.
admin.site.register(OrderModel)

class PostImageAdmin(admin.StackedInline):
    model = PostImage
 
@admin.register(LaptopModel)
class LaptopAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]
 
    class Meta:
       model = LaptopModel
 
@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass