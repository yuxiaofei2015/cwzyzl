from django.contrib import admin

# Register your models here.
from blog.models import Blog, Group


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    pass


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    pass
