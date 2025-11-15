from operator import index
from django.contrib import admin

# Register your models here.
from app.models import *

class CustomWebpage(admin.ModelAdmin):
    list_display=['topic_name','name','url','email','pk']
    list_display_links=['name','pk']
    list_editable=['email']
    list_per_page=4
    search_fields=['name']
    list_filter=['topic_name']
    
class CustomTopic(admin.ModelAdmin):
    list_display=['topic_name','pk']
    list_display_links=['topic_name']
    list_per_page=4
    search_fields=['topic_name']
    
    
class CustomAccessRecord(admin.ModelAdmin):
    list_display=['name','date','author','pk']
    list_display_links=['name','pk']
    list_per_page=4
    search_fields=['name']
    list_filter=['date']
    
    
admin.site.site_header = "Django Topic Database"
admin.site.site_title = "Admin Portal"
admin.site.index_title = "Sports"

admin.site.register(Topic,CustomTopic)
admin.site.register(WebPage,CustomWebpage)
admin.site.register(AccessRecord,CustomAccessRecord)