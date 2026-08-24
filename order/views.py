from django.shortcuts import render

# Create your views here.
def order(request):
    return render(request , 'order_placed.html')
