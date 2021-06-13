from django.db import models

# Create your models here.

class Menu(models.Model):
    nameid = models.IntegerField(default=0)
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    calorie = models.IntegerField(default=0)
    picture = models.URLField(max_length=200)
    link = models.URLField(max_length=200)
    judge = models.IntegerField(default=0)

    def __str__(self):
        return '<menus:ID'+str(self.id)+','+self.name+'nameid:'+str(self.nameid)+'>'