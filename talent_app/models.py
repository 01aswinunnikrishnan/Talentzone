from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class UserType(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    
   
 
class user_register(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    mobile =models.CharField(max_length=100,null=True)
    
    address =models.CharField(max_length=100,null=True)
 
    

class artist_register(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    mobile =models.CharField(max_length=100,null=True)
    
    address =models.CharField(max_length=100,null=True)


class organisation_register(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    mobile =models.CharField(max_length=100,null=True)
    address =models.CharField(max_length=100,null=True)


class Add_Products(models.Model):
    artist= models.ForeignKey(artist_register,on_delete=models.CASCADE,null=True)
    work_name =models.CharField(max_length=100,null=True)
    rate =models.CharField(max_length=100,null=True)
    description =models.CharField(max_length=100,null=True)
    product_image= models.ImageField(upload_to='media/', null=True)


class Buy_Product(models.Model):
    product= models.ForeignKey(Add_Products,on_delete=models.CASCADE,null=True)
    user = models.ForeignKey(user_register,on_delete=models.CASCADE,null=True)
    cardname = models.CharField(max_length=100,null=True)
    cardno= models.CharField(max_length=100,null=True)
    expiry= models.CharField(max_length=100,null=True)
    cvv= models.CharField(max_length=100,null=True)
    status= models.CharField(max_length=100,null=True)
    artist= models.ForeignKey(artist_register,on_delete=models.CASCADE,null=True)

class Add_Events(models.Model):
    artist= models.ForeignKey(artist_register,on_delete=models.CASCADE,null=True)
    organisation= models.ForeignKey(organisation_register,on_delete=models.CASCADE,null=True)
    event_name =models.CharField(max_length=100,null=True)
    venue =models.CharField(max_length=100,null=True)
    address =models.CharField(max_length=100,null=True)
    date =models.CharField(max_length=100,null=True)
    time =models.CharField(max_length=100,null=True)
   

class feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    feedback = models.CharField(max_length=50,null=True)
    artist= models.ForeignKey(artist_register,on_delete=models.CASCADE,null=True)


# class payment(models.Model):rue)
#     artist= models.ForeignKey(artist_register,on_delete=models.CASCADE,null=True)
#     event= models.ForeignKey(Add_Events,on_delete=models.CASCADE,null=T
#     user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
#     payment = models.CharField(max_length=50,null=True)


class rating(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    product = models.ForeignKey(Add_Products,on_delete=models.CASCADE,null=True)
    rate = models.CharField(max_length=100,null=True)
    comment= models.CharField(max_length=100,null=True)


class payment_event(models.Model):
    event= models.ForeignKey(Add_Events,on_delete=models.CASCADE,null=True)
    artist =models.ForeignKey(artist_register,on_delete=models.CASCADE,null=True)
    cardname = models.CharField(max_length=100,null=True)
    cardno= models.CharField(max_length=100,null=True)
    expiry= models.CharField(max_length=100,null=True)
    cvv= models.CharField(max_length=100,null=True)
    status= models.CharField(max_length=100,null=True)
    organisation= models.ForeignKey(organisation_register,on_delete=models.CASCADE,null=True)
