from django.db import models
import random

random_string = str(random.randint(10000, 99999))

class Order(models.Model):
	BRANCH_CHOICES = (('k','Katipunan branch'), ('m', 'Makati branch'))
	order_number = models.CharField(max_length=50, default=random_string)
	product_name = models.CharField(max_length=50)
	product_quantity = models.CharField(max_length=50)
	branch_choice = models.CharField(max_length=1, choices=BRANCH_CHOICES)
	user_name = models.CharField(max_length=100)
	shipping_address = models.CharField(max_length=100)
	phone_number = models.CharField(max_length=50)
	pub_date = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f"{self.product_name}"
	
