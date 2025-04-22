from django.db import models

class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Pending')

    def __str__(self):
        return f"Order for {self.customer_name} - {self.product_name}"
