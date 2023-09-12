from django.db import models

# Create your models here.
class Reflink(models.Model):
    reflink_id = models.AutoField(primary_key=True)
    name_user = models.CharField(max_length=255, null=False)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    uses_reflink = models.DecimalField(max_digits=4, decimal_places=1, default=0)

    def __str__(self):
        #return self.item_id
        return self.name_user

class Coupon(models.Model):
    coupon_id = models.AutoField(primary_key=True)
    coupon_name = models.CharField(max_length=255, null=False)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    uses_coupon = models.DecimalField(max_digits=4, decimal_places=1, default=0)
    def __str__(self):
        
        return self.coupon_name