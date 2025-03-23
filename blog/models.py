from django.db import models
from django.utils.text import slugify

class Catagory(models.Model):
    name = models.CharField(max_length=100)

    def _str_(self):
        return self.name

                # Migration create
        # 

                # Migration deleteAll
        # terminal -> del blog\migrations\* 
# Create your models here.
class post(models.Model):
    title = models.CharField(max_length=100) 
    content = models.TextField() # can't counted words use 
    img_url = models.URLField(null=True)  # max-length = 200, blank (nullable)
    created_at = models.DateTimeField(auto_now_add=True) # current time
    slug = models.SlugField(unique=True, db_column="custom_slug_name")
    # Terminal -> python manage.py makemigrations blog
    # Terminal -> python manage.py migrate blog
    # MySQL -> alter table blog_post add column slug varchar(225) uniq;

    category = models.ForeignKey("Catagory", on_delete=models.CASCADE ) # foreignKey - many to one relationship
 
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title) # title vachi url set panna mudiyum 
    #     # post model create aagumbothu slug create aagirum
    #     super().save(*args, **kwargs)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)  # Title-ஐ slug-ஆக மாற்றுகிறது
        super().save(*args, **kwargs)

    def _str_(self):
        return self.title     #ithu mukkiyam illa.but, ethachum important theriyanumna use pannalam 
       # title theriyum

                 #MySQL Connection Set-up
    # PS C:\Users\User\PycharmProjects\myapp> .\env\Scripts\activate.bat
    # PS C:\Users\User\PycharmProjects\myapp> pip install mysqlclient
    # settings.py ->
    #DATABASES = {
        # 'default': {
        #     'ENGINE': 'django.db.backends.mysql',
        #     'NAME': 'blog',
        #     'USER': 'root',
        #     'PASSWORD': 'John1045@',
        #     'HOST': 'localhost',
        #     'PORT':'3306'
        # }
    #}
    #  PS C:\Users\User\PycharmProjects\myapp> python .\manage.py makemigrations blog->
        # intha comment - oru migration file produce pannum. antha file-la vachi tha tables create aagum
    #  PS C:\Users\User\PycharmProjects\myapp> python .\manage.py migrate blog->
        # create panna migration and django ulla neraya apps irrukkum athoda migration files run aagirum.
        # run aana piragu table create aagum.
    #  model.py properties change aagumbothula puthu migration file create aagum .
    # athaa table-la change pannanum ->
       # PS C:\Users\User\PycharmProjects\myapp> python .\manage.py migrate ->
            # change aana migration run aagirukku
    # new feild(property) create pannura "created_at = models.dateTimeFeild(auto_now_add = True)"
       #PS C:\Users\User\PycharmProjects\myapp> python .\manage.py makemigrations ->
          # new migration create aagum
          # PS C:\Users\User\PycharmProjects\myapp> python .\manage.py migrate -> new migration run aagum
    # migration use pannurathunala namma enna chaangelam pannurathu ellam namakku theriyum

# web page dynamic content edit pannuratha pakkalam
class AboutUs(models.Model):
    content = models.TextField()
    # data base-la table create aagiruchi . 
    # ithula irrukkura content edit pannanumna admin function create pannanum


