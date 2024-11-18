# Ex02 Django ORM Web Application
## Date: 09.11.2024

## AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).
## 
![Screenshot_2024-11-15_205242 1](https://github.com/user-attachments/assets/f973099b-e149-4f42-aaaf-a8b5e44a5783)


## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
admin.py
from django.contrib import admin
from .models import bankloan,bankloanAdmin
admin.site.register(bankloan,bankloanAdmin)

models.py
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
```


## OUTPUT

![alt text](<Screenshot (6).png>)


## RESULT
Thus the program for creating a database using ORM hass been executed successfully
