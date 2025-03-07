from typing import Any
from blog.models import Catagory
from django.core.management.base import BaseCommand
  
class Command(BaseCommand):  # Demo data insert pannurathukku Command (or) BaseCommand  use pannurom
    help = "This commands inserts post data"

    def handle(self, *args: Any ,**options: Any):
        # self - intha class self parameter self-ve attributes access panna mudiyum
        # *args:Any - "Any :entha dataType varalam" "*args: positional argument with tuple functionukku anuppum"
        # positional Argument - user kudukkura input line upla vachirukkum
        # **options:any - keyword Arguments with Dictionarya functionukku anuppum
        # keyword Argument - key value vachi access pannuthu. ithukku order thevai illai 

                            # delete All records 
        Catagory.objects.all().delete()
        # post model vachi database-la irrukkura ella record-m delete aagirum

        catagories = [
            'Sports',
            'Technology',
            'Science',
            'Art',
            'Food'
        ]

        for catagory_name in catagories:
            Catagory.objects.create(name = catagory_name)
    
        # Catagory- model(class) from blogs.models import post
        # objects = create(catagory_name)
        # Catagory - database records add pannura module (terminal -> python .\manage.py populate_categories)
        
        self.stdout.write(self.style.SUCCESS("Completed inserting data! "))
        # Command run pannumbothu terminalla kamikkum

                    # Records Add pannurathukku
            # Terminal -> python manage.py populate_posts

