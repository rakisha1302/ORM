from django.db import models
from django.contrib import admin
class website (models.Model):
    colour=models.CharField(max_length=10)
    size=models.CharField(max_length=20)
    ratings=models.FloatField()
    price=models.IntegerField()
    Product_code=models.IntegerField(primary_key=True)
    Brand=models.CharField(max_length=50)
    Quality=models.CharField(max_length=20)
class websiteAdmin(admin.ModelAdmin):
    list_display=["colour","size","ratings","price","Product_code","Brand","Quality"]


