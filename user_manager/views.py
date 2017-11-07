from django.shortcuts import render, redirect
from .forms import InsertUserFrom
from .models import Register_model


def CreateUserView(request):
    posts = Register_model.objects.all()
    form = InsertUserFrom()

    context = {
        'form': form,
        'posts': posts
    }

    if request.method == 'POST':
        form = InsertUserFrom(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('/user_manager/list')
    else:
        form = InsertUserFrom()

    return render(request, 'registration/signup.html', context)


def LoginCheck(request):
    user_info = Register_model.objects.filter(user_id=request.POST['user_id'], user_pw=request.POST['password']).count()
    if user_info == 1:
        return redirect('/vacation/')
    else:
        return redirect('login')


def UserList(request):
    user_list = Register_model.objects.all()
    return render(request, 'user_list.html', {'user_list': user_list})


def UserDetail(request):
    user_info = Register_model.objects.get(user_id=request.POST['user_id'])
    return render(request, 'user_detail.html', {'user_info':user_info})




