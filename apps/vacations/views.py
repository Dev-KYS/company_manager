from django.shortcuts import render
from django.conf import settings
from django.db.models import Q

from .forms import CreateVacationFrom
from .models import Vacation


def vacation_list(request):
    object = Vacation.objects.select_related().all()
    return render(request, "vacation_list.html", {'vacation_list': object})


def vacation_mylist(request):
    object = Vacation.objects.select_related().filter(user_id=request.user.uid)
    return render(request, "my_vacation_list.html", {'vacation_list': object})


def vacation_teamlist(request):
    object = Vacation.objects.select_related().filter(Q(first_approval_user=request.user.uid) | Q(last_approval_user=request.user.uid))
    return render(request, "vacation_list.html", {'vacation_list': object})


def vacation_create(request):
    vacationform = CreateVacationFrom()
    if request.method == 'POST':
        vacationform = CreateVacationFrom(request.POST)
        if vacationform.is_valid():
            vacation = vacationform.save(commit=False)
            vacation.user_id = request.user.uid
            vacation.save()

    return render(request, "register_vacation.html", {'vacationform': vacationform})


def vacation_detail(request):
    object = Vacation.objects.select_related().get(user_id=request.POST['user_uid'])
    return render(request, "vacation_detail.html", {'info': object})


def agree(request):
    return


def denied(request):
    return