from django.shortcuts import render
from django.conf import settings
from django.db.models import Q
from django.http import JsonResponse
from apps.users.models import MyUser, Grant, Agent
from apps.teams.models import Team
from .models import VacationCode
from django.db.models import Subquery, OuterRef
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
        vacationform.first_approval_user = request.POST['first_approval_user']
        vacationform.last_approval_user = request.POST['last_approval_user']
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

    first_approval = None
    team_id = MyUser.objects.get(uid=request.user.uid).team_id
    team_master = Team.objects.get(tid=team_id).team_master_id
    grant_obj = Grant.objects.get(user_id=team_master)
    if grant_obj is not None:
        if grant_obj.agent_id is not None:
            now_date = datetime.datetime.now().strftime('%Y-%m-%d')
            if datetime.datetime.strptime(str(grant_obj.agent.start), '%Y-%m-%d') <= datetime.datetime.strptime(str(now_date), '%Y-%m-%d') <= datetime.datetime.strptime(str(grant_obj.agent.end), '%Y-%m-%d'):
                first_approval = {'user_id': grant_obj.agent.user_id, 'user_nm': grant_obj.agent.user.name}
            else:
                first_approval = {'user_id': grant_obj.user_id, 'user_nm': grant_obj.user.name}
        else:
            first_approval = {'user_id': grant_obj.user_id, 'user_nm': grant_obj.user.name}
    else:
        first_approval = None

    last_approval = None
    team_master2 = Team.objects.get(tid=team_id).upper_team.team_master_id
    grant_obj2 = Grant.objects.get(user_id=team_master2)
    if grant_obj2 is not None:
        if grant_obj2.agent_id is None:
            last_approval = {'user_id':grant_obj2.user_id, 'user_nm' : grant_obj2.user.name}
        else:
            last_approval = {'user_id':grant_obj2.agent.user_id, 'user_nm' : grant_obj2.agent.user.name}
    else:
        last_approval = None

    return render(request, "register_vacation.html", {'vacationform': vacationform, 'first_approval': first_approval, 'last_approval':last_approval})


def vacation_check(request):
    vacation_check = Vacation.objects.filter(Q(user_id=request.user.uid) & (Q(start__range=(request.POST['start'], request.POST['end'])) | Q(end__range=(request.POST['start'], request.POST['end'])))).count()
    if vacation_check > 0:
        return JsonResponse({'result':'FAIL'})
    else:
        return JsonResponse({'result':'SUCCESS'})


def vacation_detail(request):
    object = Vacation.objects.select_related().get(user_id=request.POST['user_uid'], id=request.POST['v_id'])
    return render(request, "vacation_detail.html", {'info': object, 'flag':'all'})


def my_vacation_detail(request):
    object = Vacation.objects.select_related().get(id=request.POST['v_id'])
    return render(request, "vacation_detail.html", {'info': object, 'flag': 'my'})


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


def select_users(request):
    object = Grant.objects.select_related().annotate(
        agent_nm=Subquery(Agent.objects.select_related().filter(id=OuterRef('agent_id')).values('user__name')),
        agent_id=Subquery(Agent.objects.filter(id=OuterRef('agent_id')).values('user__uid')),
        start=Subquery(Vacation.objects.filter(user_id=OuterRef('user_id'), first_approval='Y', last_approval='Y').values('start')),
        end=Subquery(Vacation.objects.filter(user_id=OuterRef('user_id'), first_approval='Y', last_approval='Y').values('end'))
    ).all()
    return render(request, 'select_users.html', {'user_list': object, 'now_date' : datetime.datetime.today()})
