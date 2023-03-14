from django.shortcuts import render

# Create your views here.
def  conditions(request):
    d={'a':40,'b':300,'c':1000}
    return render(request,'conditions.html',d)

def loop(request):
    d={'name':'SURI'}
    return render (request,'loop.html',d)
