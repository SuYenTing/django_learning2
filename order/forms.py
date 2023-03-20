from django import forms
from order.models import UserInfo, Member, Product

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

class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields="__all__"
        widgets={
            'name': forms.TextInput(attrs={'placeholder': 'Enter Name'}),
            'unit': forms.TextInput(attrs={'placeholder': 'Enter Unit'}),
            'price': forms.NumberInput(attrs={'placeholder': 'Enter Price'}),
            'supplierid': forms.NumberInput(attrs={'placeholder': 'Enter Supplier ID'}),
            'categoryid': forms.NumberInput(attrs={'placeholder': 'Enter Category ID'}),
        }