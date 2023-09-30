from django.shortcuts import render,redirect

# Create your views here.
from .models import List
def home(request):
       info =List.objects.all()
       context ={
            'info':info,
        }
       return render(request,'index.html',context)
def add_client(request):
    if request.method == "POST":
        Task=request.POST.get('Task')
        Description =request.POST.get('Description')
        status =request.POST.get('status')
        status = True if status == "true" else False
        data = List(Task=Task,Description=Description,status=status)
        data.save()
        return redirect(home)
    return render(request,'index.html')
def delete_client(request,id):
        info = List.objects.get(id=id)
        info.delete()
        return redirect(home)
def edit_client(request,id):
    if request.method == "POST":
        Task=request.POST.get('Task')
        Description =request.POST.get('Description')
        status =request.POST.get('status')
        status = True if status == "true" else False
        info = List.objects.get(id=id)
        info.Task= Task
        info.Description = Description
        info.status = status
        info.save()
        return redirect(home)
    else:
        info =List.objects.get(id=id)
        context ={
            'info':info,
        }
        return render(request,'edit.html',context)
        
    

    
    
    
    
    




