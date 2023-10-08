from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class staff(models.Model):
   # staff_status=models.BooleanField(deafult = False)
   
   name = models.CharField(max_length = 25)
   referal_code = models.CharField(max_length=10)
   people_joined = models.ManyToManyField(User)
   
   def __str__(self):
      return self.name
   
   def get_people_joined(self):
      users =  self.people_joined.all()
      b=[]
      for user in users:
        b.append(user.username)
      return b

class Product(models.Model):
   name = models.CharField(max_length=25)
   price = models.IntegerField(null = True)

   def __str__(self):
       return self.name
   

class Customer(models.Model):
   name = models.ForeignKey(User , on_delete=models.CASCADE)
   Product_purchased = models.ManyToManyField(Product , null = True)
   email =  models.EmailField( max_length=254)
   email_token = models.CharField(max_length=20)
   email_is_verified = models.BooleanField(default=False)

   def __str__(self) -> str:
      return self.name

class Orders(models.Model):
   Course_name = models.ForeignKey(Product, on_delete=models.CASCADE)
   Owner = models.ForeignKey(User , on_delete=models.CASCADE)
   

   
class lectures(models.Model):
   caption = models.CharField(max_length=25)





