from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login
from django.core.urlresolvers import reverse

from .forms import LoginForm

# Create your views here。
def user_login(request):
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username = cd['username'],password = cd['password'])

            if user:
                login(request,user)
                return HttpResponseRedirect(reverse("article:article_column"))
            else:
                return HttpResponse("账号或密码错误")
        else:
            return HttpResponse("格式不正确")

    if request.method == "GET":
        login_form = LoginForm()
        return render(request,"account/login.html",{"form":login_form})
