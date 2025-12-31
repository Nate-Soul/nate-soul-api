from django.contrib import admin
from django.utils.text import slugify
from .models import Project, ProjectImage, Technology, Category, Feature, Tag

# Register your models here.
class ProjectImageInline(admin.TabularInline):
    model = ProjectImage

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "name", 
        "is_active", 
        "priority", 
        "modified_at"
    )
    prepopulated_fields = {
        "slug": [slugify("name"),],
    }
    list_filter = ("status", "is_active", "categories", "tags")
    inlines = [
        ProjectImageInline,
    ]


class TechnologyAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': (slugify('name'),),
    }
admin.site.register(Technology, TechnologyAdmin)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': (slugify('name'),),
    }
admin.site.register(Category, CategoryAdmin)


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': (slugify('name'),),
    }
admin.site.register(Tag, TagAdmin)

admin.site.register(Feature)