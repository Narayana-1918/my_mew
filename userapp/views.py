from django.shortcuts import render,HttpResponse,redirect
from .models import *
from .forms import *
from adminapp.models import *
from django.urls import reverse
# Create your views here.
def register(request):
    if request.method=='POST':
        form=CustomerForm(request.POST,request.FILES)
        if form.is_valid():
            form.save(commit=True)
        else:
            print("hello")
        return HttpResponse("<h1>registered successfully</h1>")
    return render(request,'userapp/reg.html')

def view(request):
    data=Customer.objects.all()
    return render(request,'userapp/view.html',{'data':data})

def products(request):
    data=Product.objects.all()
    return render(request,'userapp/product.html',{'data':data})

def update(request,id):
    data=Customer.objects.get(id=id)
    form=CustomerForm(instance=data)
    if request.method=='POST':
        form=CustomerForm(request.POST,request.FILES,instance=data)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/userapp/view/')
    return render(request,'userapp/update.html',{'form':form,'data':data})

def delete_data(request,id):
    data=Customer.objects.get(id=id)
    if request.method=='POST':
        data.delete()
        return redirect(('/userapp/view/'))
    return render(request,'userapp/delete.html',{'data':data})
