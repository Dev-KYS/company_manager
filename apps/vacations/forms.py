from django import forms
from .models import Vacation, VacationCode
from apps.users.models import MyUser


class CreateVacationFrom(forms.ModelForm):
    vacation_type = forms.ModelChoiceField(
        required=True,
        label="신청 구분",
        queryset=VacationCode.objects.all(),
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'required' : 'True'
            }
        )
    )

    start = forms.DateField(
        required=True,
        label="휴가 시작일",
        widget=forms.DateInput(
            attrs={
                'class': 'form-control datepicker',
                'required' : 'True'
            }
        )
    )

    end = forms.DateField(
        required=True,
        label="휴가 종료일",
        widget=forms.DateInput(
            attrs={
                'class': 'form-control datepicker',
                'required' : 'True'
            }
        )
    )

    reason = forms.CharField(
        required=True,
        label="사유",
        widget=forms.Textarea(
            attrs={
                'class':'form-control',
                'required' : 'True'
            }
        )
    )

    first_approval_user = forms.ModelChoiceField(
        label="1차 승인자",
        queryset=MyUser.objects.all(),
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        )
    )

    last_approval_user = forms.ModelChoiceField(
        label="최종 승인자",
        queryset=MyUser.objects.all(),
        widget=forms.Select(
            attrs={
                'class': 'form-control'
            }
        )
    )

    class Meta:
        model = Vacation
        fields = ("vacation_type", "start", "end", "reason", "first_approval_user", "last_approval_user")
