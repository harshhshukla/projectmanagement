from django.shortcuts import render

# Create your views here.



def Project(request):
   
    return render(request, "project/index.html")
