from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()

class Product(models.Model):
    name = models.CharField(max_length=100)
    hsn_code = models.CharField(max_length=20)
    gst_rate = models.FloatField()
    price = models.FloatField()
    stock = models.IntegerField()

class Invoice(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    total = models.FloatField()
    cgst = models.FloatField()
    sgst = models.FloatField()

class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.FloatField()
    gst_rate = models.FloatField()
