from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class product(models.Model):
    PNAME=((1,'Ring'),(2,'Bracelets'),(3,'Earring'),(4,'Chain'),(5,'Ancklates'),(6,'Necklace'))
    Product_Name=models.IntegerField(verbose_name="PName",choices=PNAME)
    name=models.CharField(max_length=50,verbose_name="Product Name")
    price=models.FloatField()
    Metal_Type=models.CharField(max_length=100,verbose_name="Metal Type")
    Weight_gm=models.FloatField(verbose_name="Metal_Weight gm")
    CAT=((1,'Gold'),(2,'Silver'),(3,'Dimond'))
    Cat=models.IntegerField(verbose_name="Category",choices=CAT)
    is_active=models.BooleanField(default=True,verbose_name="Available")
    pimage=models.ImageField(upload_to='image')


    #def __str__(self):
        #return self.name


class Cart(models.Model):
        uid=models.ForeignKey(User,on_delete=models.CASCADE,db_column='uid')
        pid=models.ForeignKey(product,on_delete=models.CASCADE,db_column='pid')
        qty=models.IntegerField(default=1)


class Order(models.Model):
        order_id=models.CharField(max_length=30)
        uid=models.ForeignKey(User,on_delete=models.CASCADE,db_column='uid')
        pid=models.ForeignKey(product,on_delete=models.CASCADE,db_column='pid')
        qty=models.IntegerField(default=1)
        
    
