from django.db import models
from django.contrib import admin
class bankloan (models.Model):
    name=models.CharField(max_length=200)
    address=models.CharField(max_length=100)
    salary=models.IntegerField()
    age=models.IntegerField()
    email=models.EmailField()
 
class bankloanAdmin(admin.ModelAdmin):
    list_display=['name','address','salary','age','email']
