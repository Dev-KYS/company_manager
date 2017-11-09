from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .forms import SignupFrom
from .models import MyUser


def signup(request):
    signupform = SignupFrom()
    if request.method == 'POST':
        signupform = SignupFrom(request.POST)
        if signupform.is_valid():
            user = signupform.save(commit=False)
            user.save()
            return HttpResponseRedirect(
                reverse("sign_ok")
            )
    return render(request, "registration/signup.html", {"signupform": signupform})


def userlist(request):
    object = MyUser.objects.select_related().all()
    return render(request, "user_list.html", {'userlist': object})


def userdetail(request):
    object = MyUser.objects.select_related().get(uid=request.POST['uid'])
    return render(request, "user_detail.html", {'data':object})