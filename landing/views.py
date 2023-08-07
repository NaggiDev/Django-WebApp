from django.shortcuts import render

# Create your views here.
def get_landing(request):
    return render(request, "landing/index.html")

# this is the view for handling errors
def error_handler(request):
    return render(request, '404.html')