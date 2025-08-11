from django.shortcuts import render
from .models import Restaurant

def home(request):
    restaurant = Restaurant.objects.first()
        return render(request, 'home/index.html', {'restaurant': restaurant})
   
def about(request):
        return render(request, 'home/about.html')
