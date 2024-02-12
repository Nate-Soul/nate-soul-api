from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.core.validators import FileExtensionValidator

# Create your models here.
class Profile(models.Model):
    user        = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    headline    = models.CharField(verbose_name=_("Hero headline"), max_length=150)
    subheading  = models.TextField(verbose_name=_("Hero subheading"), max_length=300)
    headshot    = models.ImageField(verbose_name=_("Hero Avatar"), upload_to="images/personal/")
    profile_img = models.ImageField(verbose_name=_("About Image Display"), upload_to="images/personal/")
    bio         = models.TextField(verbose_name=_("Professional Summary"))
    phone       = models.CharField(max_length=20, verbose_name=_("Phone Number"))
    address     = models.CharField(verbose_name=_("Location"), max_length=100)
    
    def __str__(self) -> str:
        return f"{self.user.username}'s profile"
    
    
class Social(models.Model):
    profile     = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="social")
    platform    = models.CharField(verbose_name=_("Social Media Platform"), max_length=100, unique=True)
    icon        = models.FileField(
        verbose_name=_("Social Media Icon"), 
        default="images/icons/default.svg", 
        upload_to="images/icons/", 
        validators=[FileExtensionValidator(['svg', 'png', ''])]
    )
    icon_dark   = models.FileField(
        verbose_name=_("Social Media Dark Icon"),
        upload_to="images/icons/",
        null=True,
        blank=True,
        validators=[FileExtensionValidator(['svg', 'png', ''])]
    )
    link        = models.URLField(verbose_name=_("Social Media Link"), max_length=255, unique=True)
    
    def __str__(self) -> str:
        return f"{self.profile.user.username}'s {self.platform}'s profile"
    
    