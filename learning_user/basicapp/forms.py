from django import forms
from basicapp.models import UserProfileInfo
from django.contrib.auth.models import User

class UserInfo(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model=User
        fields = ['username','password','email']


class ProfileInfo(forms.ModelForm):

    class Meta:
        model= UserProfileInfo
        fields= ['portfolio_site','profile_pic']
