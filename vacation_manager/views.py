from django.shortcuts import render, redirect
from user_manager.models import Register_model
from .models import Vacation_model
from code_manager.models import Code_model


def Vacation_list(request):

    vacation_list = Vacation_model.objects.select_related('type', 'user').filter(type__grp_cd='vacation')
    return render(request, 'vacation_list.html', {'vacation_list':vacation_list})


def My_vacation_list(request):
    vacation_list = Vacation_model.objects.select_related('type').filter(user_id=request.session['user_id'], type__grp_cd='vacation')
    return render(request, 'my_vacation_list.html', {'vacation_list': vacation_list})


def Vacation_detail(request):
    return render(request, 'vacation_detail.html')


def Vacation_modify(request):
    return render(request, 'vacation_modify.html')


def Register_vacation(request):
    return render(request, 'register_vacation.html')


def Vacation_register(request):
    if request.method == 'POST':
        vacation = Vacation_model()
        vacation.type = Code_model(cd=request.POST['type_cd'])
        vacation.user = Register_model(user_id=request.session['user_id'])
        vacation.sta_dt = request.POST['sta_dt']
        vacation.end_dt = request.POST['end_dt']
        vacation.reason = request.POST['reason']
        vacation.save()
        return redirect('/vacation/vacation_list')
    else:
        type_code = Code_model.objects.filter(grp_cd='vacation')
        return render(request, 'vacation_register.html', {'type_code':type_code})