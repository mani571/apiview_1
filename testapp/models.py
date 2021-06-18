from django.db import models

# Create your models here.

class details(models.Model):
	name=models.CharField(max_length=20)
	position=models.CharField(max_length=10)
	mobile=models.IntegerField()
	address=models.TextField(max_length=50)

	class Meta:
		db_table="DETAILS"


 