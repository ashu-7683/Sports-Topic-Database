from operator import index
from django.contrib import admin

# Register your models here.
from app.models import *

class CustomWebpage(admin.ModelAdmin):
    list_display=['topic_name','name','url','email','pk']
    list_display_links=['name','pk']
    list_editable=['email']
    list_per_page=3
    search_fields=['name']
    list_filter=['topic_name']
    
admin.site.site_header = "Django Topic Database"
admin.site.site_title = "Admin Portal"
admin.site.index_title = "Ashu"

admin.site.register(Topic)
admin.site.register(WebPage,CustomWebpage)
admin.site.register(AccessRecord)