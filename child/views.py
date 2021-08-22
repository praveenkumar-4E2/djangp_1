from django.shortcuts import render

# Create your views here.



def Hello(request):
    return render(request,'child/base.html')

def link(request):
    return render(request,'child/link.html')