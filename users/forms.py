from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm , UserCreationForm

from users.models import User

class UserLoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField()

#class UserLoginForm(forms.ModelForm):
#    username = forms.CharField(
#        label = 'Имя',
#        widget=forms.TextInput(attrs={"autofocus": True,
#                                      'class':'form-control',
#                                      'placeholder':'Введите ваше имя пользувателя'}))
#    password = forms.CharField(
#        label = 'Пароль',
#        widget=forms.PasswordInput(attrs={"autocomplete": "current-password",
#                                          'class':'form-control',
#                                          'placeholder':'Введите ваш пароль' }),
#    


password = forms.CharField(
         label = 'Пароль',
         widget=forms.PasswordInput(attrs={"autocomplete": "current-password",
                                           'class': 'form-control',
                                           'placeholder': 'Введите ваш пароль'})
     )

class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        )

image = forms.ImageField(required=False)
first_name = forms.CharField()
last_name = forms.CharField()
username = forms.CharField()
email = forms.CharField()        
    
#
      
class ProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            "image",
            "first_name",
            "last_name",
            "username",
            "email",)
        
        image = forms.ImageField(
         widget=forms.FileInput(attrs={"class": "form-control mt-3"}), required=False
        )
    
    image = forms.ImageField(required=False)
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()
    
       
      