from django.shortcuts import render
from basicapp.models import User,UserProfileInfo
from basicapp import forms

from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import  authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request,'basicapp/index.html')

def register(request):
    form_user=forms.UserInfo()
    form_profile=forms.ProfileInfo()
    d={'form_user':form_user,'form_profile':form_profile}
    d["registered"]=False

    if request.method=="POST":
        form_user=forms.UserInfo(request.POST)
        form_profile=forms.ProfileInfo(request.POST)

        if form_user.is_valid() and form_profile.is_valid():
            d["registered"]=True
            user=form_user.save()
            user.set_password(user.password)
            user.save()

            profile=form_profile.save(commit=False)
            profile.user=user
            if request.FILES.get('profile_pic',False):
                profile.profile_pic=request.FILES['profile_pic']

            profile.save()

            return render(request,"basicapp/register.html",d)

    return render(request,"basicapp/register.html",d)


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def user_login(request):

    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(username=username,password=password)
        if user:
            if user.is_active:
                print("details are correct")
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                print("Not active, COme back Later")
        else:
            print("Wrong Info")
            return HttpResonse("Wrong Informations")
    else:
        return render(request,"basicapp/login.html")
