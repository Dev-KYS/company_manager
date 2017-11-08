from django.shortcuts import render, redirect
# from .forms import InsertUserFrom
from .models import Register_model
from code_manager.models import Code_model
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
import datetime


def CreateUserView(request):
    if request.method == 'POST':
        user_info = Register_model()
        user_info.user_id = request.POST['user_id']
        user_info.user_pw = datetime.datetime.strptime(request.POST['birth'], '%Y-%m-%d').date().strftime('%Y%m%d')
        user_info.user_nm = request.POST['user_nm']
        user_info.email = request.POST['email']
        user_info.position = Code_model(cd=request.POST['position'], grp_cd='position') # 해당 모델이 다른 모델을 FK로 참조할 경우 참조된 모델을 instance로 선언후 입력받을 값에 해당하는 pk에 매핑
        user_info.join_day = request.POST['join_day']
        user_info.birth = request.POST['birth']
        user_info.user_grade = '02'
        user_info.team = Code_model(cd=request.POST['team'], grp_cd='team')
        user_info.save()
        return redirect('/user_manager/list')
    else:
        position = Code_model.objects.filter(grp_cd='position')
        team = Code_model.objects.filter(grp_cd='team')
        return render(request, 'registration/signup.html', {'position':position, 'team':team})


def LoginCheck(request):
    try:
        user_info = Register_model.objects.get(user_id=request.POST['user_id'], user_pw=request.POST['password'])
    except ObjectDoesNotExist:
        messages.add_message(request, messages.INFO, '아이디 또는 비밀번호가 틀렸습니다.')
        return redirect('login')

    if user_info.last_login is None:
        user_info.last_login = timezone.localtime(timezone.now())
        user_info.save()

        request.session["admin_login_yn"] = "Y"
        request.session["user_grade"] = user_info.user_grade
        request.session["user_id"] = user_info.user_id
        request.session["user_nm"] = user_info.user_nm
        return redirect('/user_manager/user_modify')
    else:
        user_info.last_login = timezone.localtime(timezone.now())
        user_info.save()

        request.session["admin_login_yn"] = "Y"
        request.session["user_grade"] = user_info.user_grade
        request.session["user_id"] = user_info.user_id
        request.session["user_nm"] = user_info.user_nm
        return redirect('/user_manager/list')



def UserList(request):
    user_list = Register_model.objects.select_related('position').filter(position__grp_cd='position')
    return render(request, 'user_list.html', {'user_list': user_list})


def UserDetail(request):
    # user_info = Register_model.objects.get(user_id=request.POST['user_id'])
    user_info = Register_model.objects.select_related('position', 'team').get(user_id=request.POST['user_id'], position__grp_cd='position', team__grp_cd='team') # join구문, selet_related에 join비교 컬럼을 지정하고 이후에 조건문
    return render(request, 'user_detail.html', {'user_info':user_info})

def UserInfoModify(request):
    user_info = Register_model.objects.get(user_id=request.session['user_id'])
    return render(request, 'user_modify.html', {'user_info': user_info})

def MyInfo(request):
    user_info = Register_model.objects.get(user_id=request.POST['user_id'])
    return render(request, 'user_detail.html', {'user_info': user_info})




