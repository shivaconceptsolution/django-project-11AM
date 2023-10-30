from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Contact,Register

def home(request):
    if request.method=="POST":
        obj = Contact(name=request.POST['txtname'],phoneno=request.POST['txtphone'],email=request.POST['txtemail'],message=request.POST['txtmsg'])
        obj.save()
        return render(request,"parentsapp/index.html",{"key":"Registration successfully"})

    return render(request,"parentsapp/index.html")

def aboutus(request):
    
    return render(request,"parentsapp/about.html")
 

def editstudent(request):
    data = Contact.objects.get(pk=request.GET["id"])
    if request.method=="POST":
        data.name = request.POST.get("txtname")
        data.phoneno=request.POST["txtphone"]
        data.email = request.POST["txtemail"]
        data.message = request.POST["txtmessage"]
        data.save()
        return redirect('/parentsapp/aboutus')

    return render(request,"parentsapp/editstudent.html",{'key':data})


def deletestudent(request):
    data = Contact.objects.get(pk=request.GET["id"])
    if request.method=="POST":
        data.delete()
        return redirect('/parentsapp/aboutus')
    return render(request,"parentsapp/deletestudent.html",{'key':data})

def services(request):
    return render(request,"parentsapp/services.html")
 

def gallery(request):
    return render(request,"parentsapp/gallery.html")
 

def contactus(request):
    return render(request,"parentsapp/contactus.html")

def signup(request):
    if request.method=="POST":
        obj = Register(emailid=request.POST["txtemail"],password=request.POST["txtpass"],mobile=request.POST["txtmobile"],fullname=request.POST["txtname"])
        obj.save()
        return redirect('/parentsapp/signin')

    return render(request,"parentsapp/signup.html")

def signin(request):
    if request.method=="POST":
        obj = Register.objects.filter(emailid=request.POST["txtemail"],password=request.POST["txtpass"])
        if(obj.count()>0):
            return redirect('/parentsapp/dashboard')
        else:
            return render(request,"parentsapp/signin.html",{"key":"login fail"})
    return render(request,"parentsapp/signin.html")
def dashboard(request):
    data = Contact.objects.all()
    return render(request,"parentsapp/dashboard.html",{'key':data})