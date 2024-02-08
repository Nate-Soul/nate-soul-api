from django.db import models
from django.utils.translation import gettext_lazy as _



# Create your models here.
class Process(models.Model):
    
    name        = models.CharField(verbose_name=_("Process Name"), max_length=255, unique=True)
    slug        = models.CharField(verbose_name=_("Process Safe URL"), max_length=255, unique=True)
    desc        = models.TextField(verbose_name=_("Process Description"),)
    icon        = models.ImageField(
        verbose_name=_("Process Image"), 
        default="images/processes/default.png", 
        upload_to="images/processes/"
    )
    icon_alt    = models.CharField(verbose_name=_("Process Icon Alternative Text"), max_length=255)
    priority    = models.PositiveSmallIntegerField(verbose_name=_("Process Display Order/priority"), unique=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Process"
        verbose_name_plural = "Processes"