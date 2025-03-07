from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse 
import logging
from .models import post, Catagory, AboutUs
from django.http import Http404
from django.core.paginator import Paginator
from .forms import ContactForm


      # static demo data
# posts =[
#         {'id': 1, 'title': 'post 1', 'content':'content of post 1'},  #  for tag use panni for loop mathiri use pannurom 
#         {'id': 2, 'title': 'post 2', 'content':'content of post 2'},  # 1 card use panni 2 more cards create pannurom 
#         {'id': 3, 'title': 'post 3', 'content':'content of post 3'},  # athoda contant change pannurom
#         {'id': 4, 'title': 'post 4', 'content':'content of post 4'}
#     ]
    # post is empty-a irruntha index.html entha content-m katathu 
    # so use if tag



# Create your views here.
def index(request):
    return HttpResponse("hELLO wORLD, you are blog index") # HttpResponse - client kudukkura request httpResponse return pannurom

def detail(request,num):  # url-la http://post/{1} intha mathiri url kku 2 parameter vanganum
    return HttpResponse(f"you are viewing post detail page is {num} ")

def old_url_redir(request):
    return redirect(reverse('blog:new_page_url'))  # redirect - old_url called new_url
                            # blog - variable      # reverse - (url.py) variable-la vachi path name call pannurom.
                                                    #            namma enna name call pannuromo athoda url call aagum 

def new_url_redir(request):
    return HttpResponse("This is new Redirect")   

def renderMathod(request):
    blog_title = "Latest post" #Variable interpolation - namakkku thevaiyana topics HTML ({{blog_title}})insert panna mudiyum
    
    all_post = post.objects.all() # post model vachi database-oda All records get panni oru variable-la vachirukku
    # getting data from post model

    #paginate
    paginator = Paginator(all_post,5) # oru pagela ethana card irrukknumnu kudukkanum
    # pagintor -> ovveru pagelayum etghana content vaikkanum , next , prev  

    page_number = request.GET.get('page')
    page_obj =  paginator.get_page(page_number)
    # http://127.0.0.1:8000/render_url -> 5 cards show pannum
    # http://127.0.0.1:8000/render_url?page=2 -> next page-la 5 cards show pannum

    return render(request,'index.html',{'key': blog_title , 'post':page_obj})

    #return render(request,'index.html',{'key': blog_title , 'post':all_post})
    # variable interpolation use panna render() 3 parameter kudukkanum, 3rd parameter return pannum

    #return render(request,'index.html')   # render method -  html page return pannuthu
                                          # Template not found error - correct url kudukkalana varum error

def renderMethod2(request, id):
    #post = next((item for item in posts if item['id']==int(val)),None) #phython for loop use panni oru ID ya hoice pannuthu
       # static data use pannum pothu use pannirukku
    try:
        # getId = post.objects.get(pk = id) # post module vachi database-la oru record get panni oru veriable store pannuthu
    # Getting data from model by post Id (pk - primaryKey )

        getId = post.objects.get(slug = id) # id post module-ku slug url varum
        # working - html {url -> id-a slug } vangi, urls.py -> url/<str:id(slug)> , slum string rebnderMathod2-la
        # id-a varum  get method-la (slug = id) string slug url marrirum , then render method call server gave 
        # slum url http address.

        related_posts  = post.objects.filter(category = getId.category).exclude(pk=getId.id)
        # category vachi tha intha filter() pannurom . but , post module use pannurathunala, post table filter pannum
        # so, exclude(pk=post.id) -> getId oru id value eduthuttu varuthu athaa naa disturb panna koodathu

    except post.DoesNotExist:
        raise Http404("post Does not Exist! ")
    # logger = logging.getLogger("SUMMA") # logger onnu create pannurom.s, import logging
    # logger.debug(f'post variable is {post}') # console-la check pannurathukku.logging connect panna GJango document->logging code->settings
        #console check pannurathukku use pannurom
    
    return render(request,'details.html',{'post':getId,'related_post':related_posts}) # details.html title change pannuthu. 3rd parameter must

def custom_page_not_Found(request,exception):
    return render(request,"404.html",status=404)
    # Exception handle pannura method request and exception 2 parameter vangum
    # render varra request, create panna 404.html file, status=404,500
    # irrunthalum exception handle pannathu 

                  #setting.py
    # DEBUG = true -> False change pannanum
    #LCAL_HOST =[ 'localhost', (ip address) '127.0.0.1']
    #TEMPLATES =['dirs':['templates']] templates -> 404.html file vachirukkura oru module

                        
def contactMathod(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)  # contactform-oda object return pannum
        name = request.POST.get('name')
        email = request.POST.get('email')
        message =request.POST.get('message')

        logger = logging.getLogger("TESTING")
        if form.is_valid():  # valid-aana form object-nu check pannuthu
            logger.debug(f"post data is {form.cleaned_data['name']}  {form.cleaned_data['email']},{form.cleaned_data['message']} ")
            success_message = 'your Email has been sent! '
            return render(request,"contact.html", { 'success_message':success_message,'form':form})  
        else:
            logger.debug("Form validation failure")
             
        return render(request,"contact.html", {'name':name, 'email':email, 'message':message,'form':form})  ;  
    return render(request,"contact.html")

def about_view(request):
    take_content = AboutUs.objects.first().content 
    # AboutUs model table first content eduthuttuvanthu content kudu
    return render(request,'about.html',{'take_content': take_content})

    # Admin -> Terminal -> python .\manage.py createsuperuser