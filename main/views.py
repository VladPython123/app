from django.http import HttpResponse
from django.shortcuts import render

from goods .models import Catagories
 
def index(request) -> HttpResponse:
    
    
    
    context: dict = {
        'title': 'Home - Главная',
        'content':'Магазин мебели HOME',
       
    }
    return render(request,'main/index.html',context)

def about(request) -> HttpResponse:
    context: dict = {
        'title': 'Home - О нас',
        'content':'О нас',
        'text_on_page':'Текст о том почему етот магазин такой класнийб и какой хороший товар.'
    }
    return render(request,'main/about.html',context)
