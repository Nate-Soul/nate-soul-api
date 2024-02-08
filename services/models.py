from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import FileExtensionValidator



# Create your models here.
class Service(models.Model):
    
    name = models.CharField(verbose_name=_("Service Name"), max_length=255, unique=True)
    slug = models.CharField(verbose_name=_("Service Safe URL"), unique=True, max_length=255)
    desc = models.TextField(verbose_name=_("Service Description"),)
    icon = models.FileField(
        verbose_name=_("Service Image"),
        default="images/services/default.png", 
        upload_to="images/services/",
        validators=[FileExtensionValidator(['svg', 'png', 'jpg', 'jpeg', 'webp'])]
    )
    icon_alt    = models.CharField(verbose_name=_("Service Icon Alternative Text"), max_length=255)
    priority    = models.PositiveSmallIntegerField(verbose_name=_("Service Display Order/Priority"), unique=True)
    is_active   = models.BooleanField(default=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"
