from django.db import models

# Create your models here.


class users (models.Model):
	user_id=models.AutoField(primary_key=True)
	full_name=models.CharField(max_length=255,default=None)
	username=models.CharField(max_length=255,default=None, unique=True)
	email=models.CharField(max_length=255,default=None)
	department=models.CharField(max_length=255,default=None)
	password=models.CharField(max_length=255,default=None)

class images (models.Model):
	image_name=models.CharField(max_length=255,default=None)
	start_date=models.DateTimeField(max_length=255,default=None)
	stop_date=models.DateTimeField(max_length=255,default=None)
	urgent=models.CharField(max_length=255,default=None)
	
class text (models.Model):
	text_id=models.AutoField(primary_key=True)
	text=models.CharField(max_length=255,default=None)
	start_date=models.DateTimeField(max_length=255,default=None)
	stop_date=models.DateTimeField(max_length=255,default=None)
	
	
	