from django.shortcuts import render

def home(request):
    return render(request , 'home.html')

def shop(request):
    return render(request , 'shop.html')

def cart(request):
    return render(request , 'cart.html')

def categories(request):
    return render(request , 'categories.html')

def offers(request):
    return render(request , 'offers.html')

def about(request):
    return render(request , 'about.html')

def contact(request):
    return render(request , 'contact.html')


def wishlist(request):
    return render(request , 'wishlist.html')