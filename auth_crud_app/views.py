from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login,logout,get_user_model
from django.contrib.auth.decorators import login_required,user_passes_test
from django.core.mail import send_mail, message
from django.contrib import messages
from django.conf import settings
from .models import CrudModel, ContactModel, AboutModel
from .forms import CrudForm, AdminSigupForm, ContactForm, AboutForm

from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode

Usermodel = get_user_model()

# Create your views here.

def user_signup_view(request):
    form=AdminSigupForm()
    if request.method=='POST':
        form=AdminSigupForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(user.password)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'You are account Activated'
            message = render_to_string('activation_mail.html',{
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            fromemail=form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[fromemail])
            email.send()
            messages.success(request,"Acount Created Successfully.Activate your account mail verified.")
            return redirect('login')
    return render(request, 'signup.html', {'form':form})  

def activate(request, uidb64, token):
    try: 
        uid=urlsafe_base64_decode(uidb64).decode()
        user=Usermodel._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user=None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, "Your Acount is activated now, please now login your account.")
        return redirect('login')  
    else:
        messages.warning(request, "Activation link is invalid.")    


def user_login_view(request):
    form=AdminSigupForm()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.success(request,"Email Verified or Not a Valid User") 
            return redirect('login')   
            print('user not found.')  
    return render(request,'login.html',{'form':form}) 

def user_logout(request):
    logout(request)
    return redirect('login')     

@login_required(login_url='login')
def indexView(request):
    data = CrudModel.objects.all()
    return render(request, 'index.html',{'data':data}) 

@login_required(login_url='login')
def addStudent_view(request):
    form=CrudForm()
    if request.method=='POST':
        form=CrudForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=False)
            form.save()
        return redirect('index')
    return render(request, 'add_student.html',{ 'form': form })

def updateStudentView(request, id):
    data= CrudModel.objects.get(id=id)
    form= CrudForm(instance=data)
    context= { 
        'form': form,  
    }
    if request.method=='POST':
         form=CrudForm(request.POST, request.FILES, instance=data)
         if form.is_valid():
            form.save(commit=False)
            form.save()
            return redirect('index')
    return render(request, 'update.html', context)    

def deleteStudentView(request, id):
    data= CrudModel.objects.get(id=id)    
    data.delete()
    return redirect('index')

@login_required(login_url='login')
def aboutView(request):
    data = AboutModel.objects.all()
    return render(request, 'about.html', {'data': data}) 

@login_required(login_url='login')
def contactView(request):
    form = ContactForm()
    if request.method=='POST':
        fromemail = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        send_mail(
                  subject,
                  message, 
                  fromemail,
                  #settings.EMAIL_HOST_USER,
                  [settings.EMAIL_HOST_USER,], 
                  fail_silently=False,
                )     
        form = ContactForm(request.POST or None)
        if form.is_valid():
            form.save(commit=False)
            form.save()  
            return redirect('contact')    
    return render(request, 'contact.html', { 'form':form })     

def createView(request): 
    form= CrudForm(request.POST or None) 
    if form.is_valid():
        form.save(commit=False)
        form.save()
        return redirect('index')
