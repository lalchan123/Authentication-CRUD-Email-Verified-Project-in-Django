from django import forms
from django.contrib.auth.models import User
from .models import CrudModel, ContactModel, AboutModel


#for admin
class AdminSigupForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','email','username','password']

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields=['email','subject','message']

class AboutForm(forms.ModelForm):
    class Meta:
        model = AboutModel
        fields=['aboutimg','title','occupation','desc']        



class CrudForm(forms.ModelForm):

    class Meta:
        model = CrudModel
        fields = [
            'name',
            'email',
            'phone',
            'image',
            'desc'     
        ]
        # fields = "__all__" 


        # widgets = {

        #     'name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Please Enter name'}),
        #     # 'password':forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Please Enter Password'}),
        #     'email':forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Please Enter Email'}),
        #     'phone':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Please Enter Phone'}),
        #     'desc':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Please Enter Phone'}),

        # }