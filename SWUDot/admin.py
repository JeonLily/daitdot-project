from django.contrib import admin
from .models import *


# Register your models here.

class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'username','password', 'number', 'user_image', 'email', 'temp_number','last_name', 'isStudent']
    search_fields = ['username', 'nickname']
    ordering = ['username']

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user_name','store','review_score', 'text', 'hearts','review_image','created','updated']
    list_filter = ['user_name', 'created', 'updated']
    raw_id_fields = ['user_name']
    ordering = ['-updated', '-created']

class StoreInfoAdmin(admin.ModelAdmin):
    list_display = ['st_name', 'st_number', 'st_address','st_score','review_count', 'latitude','longitude','st_time','tag','category']
    search_fields = ['st_name', 'category']
    ordering = ['-st_score']

class SchoolAdressBookAdmin(admin.ModelAdmin):
    list_display = ['name','team_name', 'number']
    search_fields = ['name']
    ordering = ['team_name']


admin.site.register(User, UserInfoAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(StoreInfo, StoreInfoAdmin)
admin.site.register(SchoolAdressBook, SchoolAdressBookAdmin)