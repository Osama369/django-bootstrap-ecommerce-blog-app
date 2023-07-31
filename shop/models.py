from django.db import models
# Create your models here.

class product(models.Model):
    product_id= models.AutoField
    product_name = models.CharField(max_length=20)
    category = models.CharField(max_length=50, choices=[
        ('Men', 'Men Shoes'),
        ('Women', 'Women Shoes'),
        ('Kids', 'Kids Shoes'),
        # Add more categories as needed
    ])
    # subcategory= models.CharField(max_length=50, default="")

    price  = models.FloatField(default=0)
    desc= models.CharField(max_length=300)
    pub_date= models.DateField()
    image= models.ImageField(upload_to="shop/images", default="")
    def __str__(self) :     
        return self.product_name

class CartItem(models.Model):
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.product.product_name} - {self.quantity}"

    