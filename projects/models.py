import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import FileExtensionValidator

from services.models import Service

# Create your models here.
    
class Tag(models.Model):
    name = models.CharField(unique=True, max_length=100, verbose_name=_("Tag Name"))
    slug = models.CharField(unique=True, max_length=100, verbose_name=_("Tag Safe URL"))
    
    def __str__(self) -> str:
        return self.name
    
class Category(models.Model):
    name = models.CharField(unique=True, max_length=255, verbose_name=_("Category name"))
    slug = models.CharField(unique=True, max_length=255, verbose_name=_("Category Safe URL"))
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class Feature(models.Model):
    web_id  = models.UUIDField(default=uuid.uuid4, unique=True, verbose_name=_("Feature Web ID"), editable=False)
    feature = models.CharField(unique=True, max_length=255, verbose_name=_("Feature"))
    
    def __str__(self):
        return self.feature
    
class Technology(models.Model):
    name = models.CharField(unique=True, max_length=100, verbose_name=_("Technology Name"))
    slug = models.CharField(unique=True, max_length=100, verbose_name=_("Technology Safe URL"))
    icon = models.FileField(
        verbose_name=_("Technology Logo"), 
        upload_to="images/technologies/", 
        default="images/technologies/default.svg",
        validators=[FileExtensionValidator(['svg', 'png', 'jpeg','jpg', 'webp', ''])]
    )
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Technology"
        verbose_name_plural = "Technologies"    

class Project(models.Model):
    
    PROJECT_TYPE_CHOICES = (
        ('client', 'Client'),
        ('hubby', 'Hubby'),
        ('side', 'Side'),
    )
    
    PROJECT_STATUS_CHOICES = (
        ('completed', 'Completed'),
        ('incomplete', 'Incomplete'),
    )
    
    name        = models.CharField(verbose_name=_("Project Name"), max_length=255, unique=True)
    slug        = models.CharField(verbose_name=_("Project Safe URL"), unique=True, max_length=255)
    excerpt     = models.CharField(verbose_name=_("Project Excerpt"), unique=True, max_length=255)
    case_study  = models.TextField(verbose_name=_("Project Description"),)
    link        = models.CharField(verbose_name=_("Project Live Link"), null=True, blank=True, max_length=255)
    github      = models.CharField(verbose_name=_("Project Repo"), null=True, blank=True, max_length=255)
    tags        = models.ManyToManyField(Tag, related_name="tags")
    categories  = models.ManyToManyField(Category, related_name="categories")
    services    = models.ManyToManyField(Service, related_name="services")
    technologies= models.ManyToManyField(Technology, related_name="technologies")
    features    = models.ManyToManyField(Feature, related_name="features")
    type        = models.CharField(verbose_name=_("Project Type"), max_length=100, choices=PROJECT_TYPE_CHOICES)
    status      = models.CharField(verbose_name=_("Project Completion Status"), max_length=100, choices=PROJECT_STATUS_CHOICES)
    is_active   = models.BooleanField(default=True)
    priority    = models.PositiveIntegerField(unique=True, verbose_name=_("Project Display Priority"))
    created_at  = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"

class ProjectImage(models.Model):
    web_id  = models.UUIDField(default=uuid.uuid4, verbose_name=_("Image Web ID"), unique=True, editable=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="images")
    alt     = models.CharField(max_length=255, verbose_name=_("Project Image Alternative Text"))
    image   = models.ImageField(
        verbose_name=_("Project Image"), 
        default="images/portfolio/default.jpg", 
        upload_to="images/portfolio/"
    )
    is_feature = models.BooleanField(default=False)