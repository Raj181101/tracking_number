from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class TrackingNumber(models.Model):
    tracking_number = models.CharField(max_length=16, unique=True, db_index=True)
    origin_country_id = models.CharField(max_length=50, blank=True, null=True)
    destination_country_id = models.CharField(max_length=50, blank=True, null=True)
    weight = models.DecimalField(max_digits=5, decimal_places=3, blank=True, null=True)
    customer_id = models.UUIDField(max_length=36, blank=True, null=True)
    customer_name = models.CharField(max_length=100, null=True, blank=True)
    customer_slug = models.SlugField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.tracking_number

    def save(self, *args, **kwargs):
        self.customer_slug = slugify(self.customer_name)
        super(TrackingNumber, self).save(*args, **kwargs)