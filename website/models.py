from django.db import models

# Create your models here.


class ProductCategory(models.Model):
    product_cat_id = models.AutoField(primary_key=True)
    product_category_name = models.CharField(max_length=100)
    product_category_image = models.ImageField(blank=True, upload_to='product_category')
    product_description = models.TextField(blank=True)
    is_active = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return f"{self.product_category_name}"
    
   



class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=200)
    product_short_description = models.CharField(max_length=200, blank=True)
    product_image = models.ImageField(upload_to='product')
    product_discount_price = models.PositiveIntegerField(blank=True) 
    product_price = models.PositiveIntegerField()
    product_description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)



QUERY_TYPE = (
    ('FARMER', 'Farmer'),
    ('DEALER','Dealer'),
    ('RETAILER','Retailer'),
)

class ContactUs(models.Model):
    contact_id = models.AutoField(primary_key=True)
    contact_name = models.CharField(max_length=100)
    mobile = models.IntegerField()
    email = models.EmailField(blank=True)
    query_type = models.CharField(max_length=50, choices=QUERY_TYPE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

