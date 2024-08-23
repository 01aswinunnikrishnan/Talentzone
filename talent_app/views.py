
from django.shortcuts import render, redirect
from  django.contrib.auth.models import auth,User
from django.contrib import messages
from django.views.generic import TemplateView
from django.contrib.auth import login
from django.views.generic.base import View

from django.core.mail import EmailMessage
from django.conf import settings
from talent_app.models import UserType, user_register,artist_register,organisation_register
# # Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'


class user_registration(TemplateView):
    template_name="userreg.html"
    def post(self,request,*args,**kwargs):
        name=request.POST['name']
        mobile=request.POST['mobile']
        email=request.POST['email']
        
        
        address=request.POST['address']
        password=request.POST['password']
        try:
            user = User.objects.create_user(first_name=name,email=email,password=password,username=email,last_name='0')
            user.save()
            tableu=user_register()
            tableu.user =user
            tableu.mobile =mobile
           
            tableu.address = address
            
            tableu.save()
            usertype = UserType()
            usertype.user = user
            usertype.type ='user'
            usertype.save()
            messages = "Successfully Registered"
            return render(request,'index.html',{'message':messages})
        except:
            messages = "Enter Another Username, user already exist"
            return render(request,'index.html',{'message':messages})
        

class login_view(TemplateView):
    template_name="login.html"
    def post(self,request,*args,**kwargs):
        username=request.POST['username']
        print(username)
        password =request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not  None:
            login(request,user)
            if user.last_name=='1':
                if user.is_superuser:
                    return redirect('/admin')
                elif UserType.objects.get(user_id=user.id).type=="artist":
                    return redirect('/artist')
                elif UserType.objects.get(user_id=user.id).type == "organisation":
                    return redirect('/organisation')
                elif UserType.objects.get(user_id=user.id).type == "user":
                    return redirect('/user')
                else:
                    return render(request,'login.html',{'message':" User Account Not Authenticated"})

            else:
                return render(request,'login.html',{'message':" User Account Not Authenticated"})
        else:
            return render(request,'index.html',{'message':"Invalid Username or Password"})



class artist_registration(TemplateView):
    template_name="artistreg.html"
    def post(self,request,*args,**kwargs):
        name=request.POST['name']
        mobile=request.POST['mobile']
        email=request.POST['email']
        
        
        address=request.POST['address']
        password=request.POST['password']
        try:
            user = User.objects.create_user(first_name=name,email=email,password=password,username=email,last_name='0')
            user.save()
            tableu=artist_register()
            tableu.user =user
            tableu.mobile =mobile
           
            tableu.address = address
            
            tableu.save()
            usertype = UserType()
            usertype.user = user
            usertype.type ='artist'
            usertype.save()
            messages = "Successfully Registered"
            return render(request,'index.html',{'message':messages})
        except:
            messages = "Enter Another Username, user already exist"
            return render(request,'index.html',{'message':messages})
        

class organisation_registration(TemplateView):
    template_name="organisationreg.html"
    def post(self,request,*args,**kwargs):
        name=request.POST['name']
        mobile=request.POST['mobile']
        email=request.POST['email']
        
        
        address=request.POST['address']
        password=request.POST['password']
        try:
            user = User.objects.create_user(first_name=name,email=email,password=password,username=email,last_name='0')
            user.save()
            tableu=organisation_register()
            tableu.user =user
            tableu.mobile =mobile
           
            tableu.address = address
            
            tableu.save()
            usertype = UserType()
            usertype.user = user
            usertype.type ='organisation'
            usertype.save()
            messages = "Successfully Registered"
            return render(request,'index.html',{'message':messages})
        except:
            messages = "Enter Another Username, user already exist"
            return render(request,'index.html',{'message':messages})
        
