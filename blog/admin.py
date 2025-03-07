from django.contrib import admin
from .models import  post, Catagory, AboutUs
# Register your models here.
# admin.site.register(post,)
# admin.site.register(Catagory)

class PostAdmin(admin.ModelAdmin):
    list_display=('title','content') # display panna vendiya arguments tuple kudukkanum
    serach_field =('title','content') # search panna vendiya arguments tuple kudukkanum
    list_filter =('category','created_at') # filter panni display contant easy pakkalam


# Modified your models here.
admin.site.register(post,PostAdmin)
admin.site.register(Catagory)
admin.site.register(AboutUs)