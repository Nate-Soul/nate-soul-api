import uuid
from django.db import models

# Create your models here.

from django.utils.translation import gettext_lazy as _



# Create your models here.
class Testimonial(models.Model):
    
    web_id      = models.UUIDField(verbose_name=_("Testimonial Web URL"), unique=True, default=uuid.uuid4)
    name        = models.CharField(verbose_name=_("Testimonee Name"), max_length=255, unique=True)
    role        = models.CharField(verbose_name=_("Testimonee's Role"), max_length=255)
    company     = models.CharField(verbose_name=_("Testimonee's Company"), max_length=255)
    review      = models.TextField(verbose_name=_("Testimonee's Review"))
    avatar      = models.ImageField(
        verbose_name=_("Testimonee's Avatar"), 
        upload_to="images/testimonees/", 
        null=True, 
        blank=True
    )
    is_active   = models.BooleanField(default=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"
    
    def __str__(self):
        return f"Testimonial from {self.name}"