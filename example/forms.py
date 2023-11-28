from django import forms
 
from django.core.validators import *


from django.contrib.auth import authenticate

from django.contrib.auth.models import User
# iterable 

# creating a form
class SignupForm(forms.Form):

    #first_name =forms.CharField(widget=forms.TextInput(attrs={'class': 'my-class','placeholder':'Enter your first name'}))
    
    email=forms.EmailField(label_suffix=' ')

   # last_name = forms.CharField(validators=[Name],widget=forms.TextInput(attrs={'class': 'my-class2','placeholder':'Enter your last name'}))

    pas = forms.CharField(label=' Password',widget = forms.PasswordInput(attrs={'class': 'my-class3','placeholder':'Enter your password '}))
    
    cpas = forms.CharField(label='Confirm Password',widget = forms.PasswordInput(attrs={'class': 'my-class3','placeholder':'Enter your password again '}))

   # roll_no = forms.IntegerField()
    
    

    def clean(self):
        cleaned_data=super().clean()
        valpass=self.cleaned_data.get('pas')
        valcpass=self.cleaned_data.get('cpas')
        email=self.cleaned_data.get('email')
        if email:
            if User.objects.filter(username=email):
                raise forms.ValidationError("Account Exists")
            
        if valcpass and valpass:
            if valcpass!=valpass:
                raise forms.ValidationError("Confirm Password not matched")
        


class LoginForm(forms.Form):
    email=forms.EmailField(label_suffix=' ')
    pas = forms.CharField(label=' Password',widget = forms.PasswordInput(attrs={'class': 'my-class3','placeholder':'Enter your password again '}))
    def clean(self):
        cleaned_data=super().clean()
        email=self.cleaned_data.get('email')
        pas=self.cleaned_data.get('pas')
        if email:
            if not User.objects.filter(username=email):

                raise forms.ValidationError("Account Doesnot Exist")

        if email and pas:
            
            user=authenticate(username=email,password=pas)

            if user is None:
                raise forms.ValidationError("Invalid Password") 