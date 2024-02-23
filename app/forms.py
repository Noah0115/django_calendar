from django import forms
from app.models import UserInfo

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    role = forms.CharField(required=False)  # 显式设置为非必填
    pic = forms.CharField(required=False)  # 显式设置为非必填
    status = forms.IntegerField(required=False)  # 显式设置为非必填
    class Meta:
        model = UserInfo
        fields = ['username', 'password', 'email','role','pic','status']
