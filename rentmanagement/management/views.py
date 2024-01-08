from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    title= "Account signup"
    site_name= "Rent Management"
    # template = loader.get_template('account.html')
    return render(request, 'account.html',{'title':title,'site_name':site_name})
