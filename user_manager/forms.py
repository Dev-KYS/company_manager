from django import forms
from .models import Register_model


class InsertUserFrom(forms.ModelForm):

    class Meta:
        model = Register_model
        fields = ("user_id", "user_nm", "email", "position", "join_day")
        widgets = {
            'user_id': forms.TextInput(attrs={'class':'form-control', 'placeholder':'아이디'}),
            'user_nm': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'이름'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'이메일'}),
            'position': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'직책'}),
            'join_day': forms.DateInput(attrs={'class': 'form-control', 'placeholder':'입사일'}),

        }
