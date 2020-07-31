from django.contrib import admin
from .models import Post

# Register your models here.
admin.site.site_header = 'F l i c K _ Administration'
admin.site.register(Post)