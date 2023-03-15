from django import forms
from order.models import UserInfo, Member

class UserInfoForm(forms.ModelForm):
    class Meta:
        model=UserInfo
        fields="__all__"
        # fileds=['username', 'password']

class MemberForm(forms.ModelForm):
    class Meta:
        model=Member
        # fields="__all__"
        fields=('email', 'pwd', 'uname')
        widgets={
            'email': forms.EmailInput(attrs={'placeholder': 'Enter Email'}),
            'pwd': forms.PasswordInput(attrs={'placeholder': 'Enter Password'}),
            'uname': forms.TextInput(attrs={'placeholder': 'Enter Name'}),
        }

class MemberLoginForm(forms.ModelForm):
    class Meta:
        model=Member
        # fields="__all__"
        fields=('email', 'pwd')
        widgets={
            'email': forms.EmailInput(attrs={'placeholder': 'Enter Email'}),
            'pwd': forms.PasswordInput(attrs={'placeholder': 'Enter Password'}),
        }