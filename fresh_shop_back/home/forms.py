
from django import forms

class UserLoginForm(forms.Form):
    #验证账号
    username=forms.CharField(required=True,
                             error_messages={'required':'账号必填'})
    #验证密码
    password=forms.CharField(required=True,
                             error_messages={'required':'密码必填'})