from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def register(request):
    if request.method=='POST':
        uname=request.POST['username']
        fname=request.POST['first_name']
        lname=request.POST['last_name']
        email=request.POST['email']
        pas=request.POST['password']
        cpas=request.POST['password1']
        if pas==cpas:
            if User.objects.filter(username=uname).exists():
                messages.info(request,"Username already existed")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email already registerd")
                return redirect('register')
            else:
                user=User.objects.create_user(username=uname,password=pas,first_name=fname,last_name=lname,email=email)
                user.save()
                print("User created")
                return redirect('login')

        else:
            messages.info(request,"Password is not matching")
            return redirect('register')
        return redirect('/')
    return render(request,"signup.html")


def login(request):
    if request.method=='POST':
       uname=request.POST['username']
       pas=request.POST['password']
       user=auth.authenticate(username=uname,password=pas)
       if user is not None:
           auth.login(request,user)
           return redirect('/')
       else:
           messages.info(request,"Invalid username or password")
           return redirect('login')

    return render(request,"loginn.html")

def logout(request):
    auth.logout(request)
    return redirect('/')