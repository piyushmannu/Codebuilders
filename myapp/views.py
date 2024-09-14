from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.sessions.models import Session



# Create your views here.
def index_show(request):
        context = {
        'show': about_img.objects.all()[0],
        'gal': porfolio.objects.all()[:3],
        'fourth_image' : porfolio.objects.all()[3] ,
        'logo' : porfolio.objects.all()[4]
        }
        return render(request, 'index.html', context)



def enquire(request):
        if request.method == "POST":
                name = request.POST['name']
                email = request.POST['mail']
                subject = request.POST['subject']
                message = request.POST['message']
                Enquiry.objects.all(name=name,email=email,subject=subject,message=message)
                return HttpResponse('submitted successfully')
        else :
                return render(request, 'index.html')
        
def user_create(request):
        if request.method == "POST":
                user= request.POST['user']
                fname = request.POST['fname']
                lname = request.POST['lname']
                email = request.POST['email']
                phone = request.POST['phone']
                password = request.POST['password']
                cpassword = request.POST['cpassword']
                if password == cpassword:
                        a = User.objects.create_user(username=user,first_name=fname,last_name=lname,email=email,password=password)
                        a.save()
                        return render(request,'index.html') #user1 pass 123456
                else:
                        return render(request,'login.html')
        else:
                return render(request,'signup.html')
        

def login_user(request):
        if request.method == "POST":
                user = request.POST['id']
                password = request.POST['key']
                verfication_user = authenticate(username=user,password=password)
                if verfication_user is not None:
                        request.session['is_login'] = True
                        return render(request,'logout.html')
                else:
                        return HttpResponse('Inavlid User')
        else:
                return render(request,'login.html')
        
def logout(request):
        return render(request,'logout.html')
        

 