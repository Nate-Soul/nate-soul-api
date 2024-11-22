from django.db import models
from django.utils.translation import gettext_lazy as _
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.
class ArticleTag(models.Model):
    name        = models.CharField(max_length=100, verbose_name=_("Tag name"), unique=True)
    slug        = models.SlugField(max_length=100, verbose_name=_("Tag safe URL"), unique=True)
    created     = models.DateTimeField(auto_now_add=True)
    modified    = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Article Tag")
        verbose_name_plural = _("Article Tags")
    
    def __str__(self) -> str:
        return self.name

class Article(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('archived', 'Archived'),
    ]

    title = models.CharField(max_length=255, unique=True, verbose_name=_("Article title"))
    slug  = models.SlugField(max_length=255, unique=True, verbose_name=_("Article Safe URL"))
    excerpt = models.TextField(verbose_name=_("Article Overview"), null=True, blank=True)
    excerpt = models.TextField(blank=True, null=True)
    featured_img_url = models.ImageField(upload_to="images/blog/thumbnails", default="images/blog/default.png", blank=True, null=True)
    tags = models.ManyToManyField(ArticleTag, related_name="tags")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    content = CKEditor5Field(null=True, blank=True, config_name="extends")
    parent_post = models.ForeignKey(
        'self', on_delete=models.SET_NULL, null=True, blank=True
    )
    featured = models.BooleanField(default=False)
    published_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-published_date']
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        return self.title
