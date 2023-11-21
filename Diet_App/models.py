from django.db import models

# Create your models here.


class AdminDetails(models.Model):
	username = models.CharField(max_length=100,default=None)
	password = models.CharField(max_length=100,default=None)
	class Meta:
		db_table = 'AdminDetails'

class userDetails(models.Model):
	Username 	= models.CharField(max_length=100,default=None,null=True)
	Password 	= models.CharField(max_length=100,default=None,null=True)
	Name 		= models.CharField(max_length=100,default=None,null=True)
	Age 		= models.CharField(max_length=200,default=None,null=True)
	Phone 		= models.CharField(max_length=100,default=None,null=True)
	Email 		= models.CharField(max_length=100,default=None,null=True)
	Address 		= models.CharField(max_length=100,default=None,null=True)
	class Meta:
		db_table = 'userDetails'

class Queries(models.Model):
	User_id = models.CharField(max_length=100,default=None,null=True)
	Query = models.CharField(max_length=300,default=None,null=True)
	Answer = models.CharField(max_length=300,default=None,null=True)
	class Meta:
		db_table = "UserFeedback"

class Information(models.Model):
	Specialization=models.CharField(max_length=100,default=None,null=True)
	Qualifications =models.CharField(max_length=100,default=None,null=True)
	Image =models.ImageField(upload_to="images/",null=True)
	Name=models.CharField(max_length=100,default=None,null=True)
	Age=models.CharField(max_length=100,default=None,null=True)
	Email=models.CharField(max_length=100,default=None,null=True)
	Number=models.CharField(max_length=100,default=None,null=True)
	Gender=models.CharField(max_length=100,default=None,null=True)
	Years=models.CharField(max_length=100,default=None,null=True)
	Languages_Spoken=models.CharField(max_length=100,default=None,null=True)
	Consultation_Hours=models.CharField(max_length=100,default=None,null=True)
	Consultation_Fees=models.CharField(max_length=100,default=None,null=True)
	Venue =models.CharField(max_length=100,default=None,null=True)
	class Meta:
		db_table = "Information"

class Breakfast_List(models.Model):
	userid = models.CharField(max_length = 100,default=None,null=True)
	Food1 =models.CharField(max_length=100,default=None,null=True)
	Food2 =models.CharField(max_length=100,default=None,null=True)
	Food3 =models.CharField(max_length=100,default=None,null=True)
	Food4 =models.CharField(max_length=100,default=None,null=True)
	Food5 =models.CharField(max_length=100,default=None,null=True)
	Food6 =models.CharField(max_length=100,default=None,null=True)
	Food7 =models.CharField(max_length=100,default=None,null=True)
	class Meta:
		db_table = "Breakfast_List"


class Lunch_List(models.Model):
	userid = models.CharField(max_length = 100,default=None,null=True)
	Food1 =models.CharField(max_length=100,default=None,null=True)
	Food2 =models.CharField(max_length=100,default=None,null=True)
	Food3 =models.CharField(max_length=100,default=None,null=True)
	Food4 =models.CharField(max_length=100,default=None,null=True)
	Food5 =models.CharField(max_length=100,default=None,null=True)
	Food6 =models.CharField(max_length=100,default=None,null=True)
	Food7 =models.CharField(max_length=100,default=None,null=True)
	class Meta:
		db_table = "Lunch_List"


class Snack_List(models.Model):
	userid = models.CharField(max_length = 100,default=None,null=True)
	Food1 =models.CharField(max_length=100,default=None,null=True)
	Food2 =models.CharField(max_length=100,default=None,null=True)
	Food3 =models.CharField(max_length=100,default=None,null=True)
	Food4 =models.CharField(max_length=100,default=None,null=True)
	Food5 =models.CharField(max_length=100,default=None,null=True)
	Food6 =models.CharField(max_length=100,default=None,null=True)
	Food7 =models.CharField(max_length=100,default=None,null=True)
	class Meta:
		db_table = "Snack_List"

class Dinner_List(models.Model):
	userid = models.CharField(max_length = 200,default=None,null=True)
	Food1 =models.CharField(max_length=200,default=None,null=True)
	Food2 =models.CharField(max_length=200,default=None,null=True)
	Food3 =models.CharField(max_length=200,default=None,null=True)
	Food4 =models.CharField(max_length=200,default=None,null=True)
	Food5 =models.CharField(max_length=200,default=None,null=True)
	Food6 =models.CharField(max_length=200,default=None,null=True)
	Food7 =models.CharField(max_length=200,default=None,null=True)
	class Meta:
		db_table = "Dinner_List"

class Example_table(models.Model):
	Name = models.CharField(max_length=200,default=None,null=True)
	Age = models.CharField(max_length=200,default=None,null=True)
	class Meta:
		db_table = "Example_table"