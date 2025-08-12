from django.shortcuts import render
from .models import Restaurant

def home(request):
    restaurant = Restaurant.objects.first()
        return render(request, 'home/index.html', {'restaurant': restaurant})
   
def about(request):
        return render(request, 'home/about.html')
def menu(request):
        menu_items = [
                {'name': 'Margherita Pizza', 'price': '$12.99', 'description': 'Fresh tomato and mozzarella'},
                        {'name': 'Chicken Pasta', 'price': '$15.99', 'description': 'Creamy alfredo sauce'},
                                {'name': 'Caesar Salad', 'price': '$8.99', 'description': 'Fresh greens with dressing'},
                                        {'name': 'Beef Burger', 'price': '$11.99', 'description': 'Juicy beef with fries'},
                                                {'name': 'Fish & Chips', 'price': '$13.99', 'description': 'Crispy battered fish'},
                                                    ]
                                                        return render(request, 'home/menu.html', {'menu_items': menu_items})