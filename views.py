from django.shortcuts import render,redirect
from .forms import Detailform
from .models import Detailmodel

# Create your views here.
def index(request):
    emp = Detailmodel.objects.all()
    data = {
        'employee':emp
    }
    return render(request, 'myapp/index.html', data)

def about(request):
    return render(request, 'myapp/about.html')

def contact(request):
    return render(request, 'myapp/contact.html')

def detail(request):
    if request.method == 'POST':
        fm = Detailform(request.POST, request.FILES) 
        if fm.is_valid():
            fm.save()
            fm = Detailform()
            return redirect('save')
    else:
        fm = Detailform()
    data =  {
        'form':fm
        }   
    return render(request, 'myapp/detail.html',data )

def update(request, id):
    if request.method=="POST":
        pi = Detailmodel.objects.get(pk=id)
        fm = Detailform(request.POST, request.FILES, instance=pi) 
        if fm.is_valid():
            fm.save()
            fm = Detailform()
            return redirect('saveupdate')
    else:
        pi = Detailmodel.objects.get(pk=id)
        fm = Detailform(instance=pi)
    data= {
        'form':fm
    }        
    return render(request, 'myapp/update.html', data)

def delete(request, id):
    if request.method=="POST":
        pi = Detailmodel.objects.get(pk=id)
        pi.delete()
        return redirect('/')
    return render(request, 'myapp/index.html')

def save(request):
    return render(request, 'myapp/save.html')

def saveupdate(request):
    return render(request, 'myapp/saveupdate.html')