from django.shortcuts import render
from django.http import HttpResponse
from .forms import ConnectForm,ContactMe

# Create your views here.
def index(request):
    return HttpResponse("Hello it's V & Welcome to my blog")

def contact_me(request):
    context = {}
    form = ConnectForm(request.POST or None)
    context['form'] = form
    return render(request,"thanks.html",context)
