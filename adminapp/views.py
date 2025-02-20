from django.shortcuts import render
from userapp.views import *
from userapp.models import *
from userapp.forms import *
# Create your views here.
def view(request):
    data=Customer.objects.all()
    return render(request,'userapp/view.html',{'data':data})