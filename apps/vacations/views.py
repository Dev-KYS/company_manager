from django.shortcuts import render
from django.conf import settings
from django.db.models import Q
from django.http import JsonResponse
from apps.users.models import MyUser
from .models import VacationCode
import datetime
import json

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
            users = MyUser.objects.get(uid=vacation.user_id)
            minus_day = VacationCode.objects.get(id=vacation.vacation_type_id)
            if minus_day.id == 1:
                minus_days = (vacation.start - vacation.end) * minus_day.minus_day
                users.v_day = users.v_day + minus_days.days
            else:
                users.v_day = users.v_day - minus_day.minus_day
            users.save()

    return render(request, "register_vacation.html", {'vacationform': vacationform})


def vacation_check(request):
    vacation_check = Vacation.objects.filter(Q(user_id=request.user.uid) & (Q(start__range=(request.POST['start'], request.POST['end'])) | Q(end__range=(request.POST['start'], request.POST['end'])))).count()
    if vacation_check > 0:
        return JsonResponse({'result':'FAIL'})
    else:
        return JsonResponse({'result':'SUCCESS'})


def vacation_detail(request):
    object = Vacation.objects.select_related().get(user_id=request.POST['user_uid'])
    return render(request, "vacation_detail.html", {'info': object})


def agree(request):
    v_id = request.POST.get('v_id')
    object = Vacation.objects.get(pk=v_id)
    if object.first_approval_user.uid == request.user.uid:
        object.first_approval = 'Y'
        object.save()
    elif object.last_approval_user.uid == request.user.uid:
        object.last_approval = 'Y'
        object.save()
    return JsonResponse({'result':'SUCCESS'})


def denied(request):
    v_id = request.POST.get('v_id')
    object = Vacation.objects.get(pk=v_id)
    if object.first_approval_user.uid == request.user.uid:
        object.first_approval = 'N'
        object.save()
    elif object.last_approval_user.uid == request.user.uid:
        object.last_approval = 'N'
        object.save()
    return JsonResponse({'result':'SUCCESS'})
