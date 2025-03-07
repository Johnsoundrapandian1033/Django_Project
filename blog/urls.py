from django.urls import path
from . import views

app_name = 'blog'
handler404 = "myapp.views.custom_page_not_Found"; 
# myapp folderla views module-la custom_page_not_Found mathod handle pannura variable
urlpatterns = [
    path("post",views.index , name="index" ),
    path("post/<str:num>",views.detail , name ="detail"),
    path("old_url", views.old_url_redir , name="old_page_url"),
    path("new_url", views.new_url_redir , name="new_page_url"),
    path("",views.renderMathod , name="indexes"),
    path("/<str:id>", views.renderMethod2, name="details"),
    path("contact",views.contactMathod, name="contactName"),
    path("about",views.about_view, name="aboutName")
]