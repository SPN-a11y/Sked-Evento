from django.shortcuts import redirect,render
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import evento,customer,register

# Create your views here.
def adminloginview(request):
    return render(request,"skedapp/adminlogin.html")

def authenticateadmin(request):
    username = request.POST['username']
    password = request.POST['password']
    
    user = authenticate(username = username,password = password)
    
    if user is not None and user.username=="admin":
        login(request,user)
        return redirect('adminhomepage')
    
    if user is None:
        messages.add_message(request,messages.ERROR,"Invalid Credentials")
        return redirect('adminloginpage')

def adminhomepageview(request):
    context = {'events' : evento.objects.all()}
    return render(request,"skedapp/adminhomepage.html",context)

def logoutadmin(request):
    logout(request)
    return redirect('adminloginpage')

def addevent(request):
    name = request.POST['ename']
    date = request.POST['edate']
    time = request.POST['etime']
    loc = request.POST['eloc']
    num = request.POST['enum']
    disc = request.POST['edisc']
    evento(ename = name,edate = date,etime = time,eloc = loc,enum = num,edisc = disc).save()
    return redirect('adminhomepage')

def deleteevent(request,eventpk):
    evento.objects.filter(id = eventpk).delete()
    return redirect('adminhomepage')

def homepageview(request):
    return render(request,"skedapp/homepage.html")

def signupuser(request):
    username = request.POST['username']
    password = request.POST['password']
    phoneno = request.POST['phoneno']
    
    if User.objects.filter(username = username).exists():
        messages.add_message(request,messages.ERROR, "User Already Exist")
        return redirect('homepage')
    
    User.objects.create_user(username = username,password = password).save()
    lastobject = len(User.objects.all())-1
    customer(userid = User.objects.all()[int(lastobject)].id,phoneno = phoneno).save()
    messages.add_message(request,messages.ERROR, "User Succesfully Created")
    
    return redirect('homepage')

def userloginview(request):
    return render(request,"skedapp/userlogin.html")

def userauthentication(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username = username,password = password)
    
    if user is not None:
        login(request,user)
        return redirect('customerpage')
    
    if user is None:
        messages.add_message(request,messages.ERROR,"Invalid Credentials")
        return redirect('userloginpage')
    
def customerwelcomeview(request):
    username = request.user.username
    context = {'username' : username,'events' :evento.objects.all()}
    return render(request,'skedapp/customerwelcome.html',context)

def userlogout(request):
    logout(request)
    return redirect('userloginpage')

def reg(request):
    username = request.user.username
    registeredevents = ""
    
    for event in evento.objects.all():
        ename = event.ename 
    
    registeredevents = registeredevents + ename + " "
    
    if register.objects.filter(username = username,registeredevents = registeredevents).exists():
        messages.add_message(request,messages.ERROR, "Event Already Registered...")
        return redirect('customerpage')
    
    register(username = username,registeredevents = registeredevents).save()
    messages.add_message(request,messages.ERROR,"Event Registered Succesfully")
    return redirect('customerpage')

def studlist(request):
    registers = register.objects.all()
    context = {'registers' : registers}
    return render(request,'skedapp/studlist.html',context)

def deleteevents(request,eventpk):
    register.objects.filter(id = eventpk).delete()
    return redirect('studlist')
    


    
    
    

    