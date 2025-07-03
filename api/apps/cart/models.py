from django.db import models

from apps.products.models import Product
from apps.users.models import User

class Cart(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return f"Cart for {self.user.name}"

class CartItem(models.Model):
	cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	quantity = models.PositiveIntegerField(default=1)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f"{self.product.name} in {self.cart}"
