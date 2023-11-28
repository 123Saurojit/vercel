from django.shortcuts import render

from .forms import SignupForm,LoginForm

from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from django.contrib.auth import login
from django.http import HttpResponse
from django.contrib.auth import authenticate,logout

from django.core.mail import send_mail
from vercel_app import settings





def signup(request):    
    # s=User.objects.get(username="saurojitkarmakar947@gmail.com")
    # s.delete()
    # q=request.GET.get('q')
    # x=request.session.get('b',0)
    # x=request.session['b']=x+1
    
    # request.session['a']=x+1
    
    
    if not request.user.is_authenticated:
    
        fm=SignupForm()

        if request.method == "POST":
            fm = SignupForm(request.POST)
            if fm.is_valid():
                email = fm.cleaned_data["email"]
                pas = fm.cleaned_data["pas"]
               # send_mail("gd","HELOOOOO",settings.EMAIL_HOST_USER,[email])
                
                # Assuming you have a custom User model with a method set_password
                # Make sure your User model has a set_password method to handle password hashing
                user = User(username=email,password=make_password(pas))
                user.save()
                

    # Hash the password and set it to the user
                # password = "your_password_here"
                # hashed_password = make_password(password)
                # user.password = hashed_password

                # user.save()

                return HttpResponse("Done")
                
        return render(request,"signup.html",{'form':fm})
    else:
        return redirect("signout")
    

        


def signin(request):
    if not request.user.is_authenticated:

        fm=LoginForm()
        if request.method == "POST":
            fm = LoginForm(request.POST)
            if fm.is_valid():
                email = fm.cleaned_data["email"]
                pas = fm.cleaned_data["pas"]
                user=authenticate(request,username=email,password=pas)
                login(request,user)
                
               # send_mail("gd","HELOOOOO",settings.EMAIL_HOST_USER,[email])
            #display success message on login
                messages.success(request, "You have successfully logged in.")

                return redirect("signout")
                
        return render(request,"signin.html",{'form':fm})
    else:
        return redirect("signout")








    
def signout(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            logout(request)
            messages.success(request, "You have successfully logged out.")

            return redirect('signin')
        return render(request,"signout.html")
    else:
        return redirect('signin')




