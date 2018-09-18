from django.contrib import admin

from .models import blogPost, blogUser

admin.site.register(blogPost)
admin.site.register(blogUser)

# Register your models here.
