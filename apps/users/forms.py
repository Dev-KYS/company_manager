from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import MyUser


class SignupFrom(UserCreationForm):
    POSITION_TYPES = (
        ('a', '대표'),
        ('b', '팀장'),
        ('c', '과장'),
        ('d', '대리'),
        ('e', '주임'),
        ('f', '사원'),
        ('g', '인턴'),
    )

    username = forms.CharField(
        required=True,
        label="아이디",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder': '아이디',
                'required' : 'True',
            }
        )
    )

    name = forms.CharField(
        required=True,
        label="이름",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '아이디',
                'required': 'True',
            }
        )
    )
    email = forms.EmailField(

        required=False,
        label="이메일",
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': '이메일',
                'required': 'True',
            }
        )
    )
    position = forms.ChoiceField(
        required=False,
        label="직급",
        choices=POSITION_TYPES,
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'required' : 'True',
            }
        )

    )
    birth = forms.DateField(
        label="생일",
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'required': 'True',
            }
        )
    )
    date_joined = forms.DateField(
        required=True,
        label="입사일",
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'required': 'True',
            }
        )
    )

    class Meata:
        model = MyUser
        fields = ("username", "name", "email", "birth", "date_joined")


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=10,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '아이디',
                'required': 'True',
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': '패스워드',
                'required': 'True',
            }
        )
    )