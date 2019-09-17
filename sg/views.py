from django.shortcuts import render
from django.http import HttpResponse

from .forms import SgFlagForm
from .models import SgFlag
# Create your views here.
def flag(request):
    if request.method == "GET":
        sg = SgFlagForm()
        return render(request,"sg/sg.html",{"sg":sg})

    if request.method == "POST":
        sgflag_form = SgFlagForm(request.POST)
        if sgflag_form.is_valid():
            sgflag_cd = sgflag_form.cleaned_data
            try:
                sgflag = SgFlag.objects.get(qqnumber = sgflag_cd["qqnumber"])
            except:
                return HttpResponse("您不是本群用户")
            sgflag.flag = sgflag_cd["flag"]
            sgflag.email = sgflag_cd["email"]
            sgflag.save()
        return HttpResponse("保存成功")
