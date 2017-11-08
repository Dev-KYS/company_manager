from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .forms import SignupFrom


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