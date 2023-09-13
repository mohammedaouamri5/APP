from django.db import models
from django.contrib.auth.models import User

#Docter , Pharmacist , pachent 
# Create your models here.

 
class Profile(models.Model): 
    position = models.IntegerField();
    Kind = models.CharField(max_length=10, null=False )
    name = models.CharField(max_length=20, null=False ) ; 
    num = models.IntegerField( max_length=10, null=False ) ;
    e_mail = models.EmailField(unique=True , null=False ) ; 
    password = models.CharField(max_length=10   , null=False) ;    
    score = models.IntegerField( max_length=10, null=False );
 