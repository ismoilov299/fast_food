from django.contrib import admin
from .models import *

class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number', 'lang_id', 'chat_id')
    # list_display_links = ('first_name')
admin.site.register(User, UserAdmin)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name_uz','name_ru','name_en','parent')
admin.site.register(Category, CategoryAdmin)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name_uz','name_ru','name_en','category','description_uz','description_ru','description_en','price','image')
admin.site.register(Product,ProductAdmin)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','user','status','payment_type','longitude','latitude','created_at')
admin.site.register(Order,OrderAdmin)
class OrderProductAdmin(admin.ModelAdmin):
    list_display = ('product','order','amount','created_at')
admin.site.register(OrderProduct,OrderProductAdmin)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user_id','comment_text','username')
# admin.site.register(About)
admin.site.register(Comment,CommentAdmin)
class NewAdmin(admin.ModelAdmin):
    list_display = ('posted_at','heading_uz','heading_ru','heading_en','text_uz','text_ru','text_en','image')
admin.site.register(New,NewAdmin)