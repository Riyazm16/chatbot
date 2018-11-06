from django.db import models
from django.core.exceptions import ValidationError

from django.core.validators import MinLengthValidator,MaxLengthValidator
# Create your models here.

class User_data(models.Model):
	person_name = models.CharField(max_length=30,default=None,validators=[MinLengthValidator(2,message='Please enter at least 1 character')])
	person_mobile = models.CharField(max_length=11,default=None,unique=True,validators=[MinLengthValidator(10,message='Mobile Number sholud be minimum 10 chacrters'),
		MaxLengthValidator(11,message='Mobile Number sholud be maxiimum 11 chacrters'),
		])
	date	= models.DateTimeField(default=None)
