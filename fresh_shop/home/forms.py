# from django import forms
# from django.contrib.auth.models import User
#
#
# class UserForm(forms.Form):
#     """
#     校验注册信息
#     """
#     username=forms.CharField(required=True,
#                               error_messages={'required':'用户名必填'})
#     password=forms.CharField(required=True,
#                         error_messages={'required': '密码必填'})
#     password2=forms.CharField(required=True,
#                          error_messages={'required': '确认密码必填'})
#     email=forms.CharField(required=True,
#                           error_messages={'required': '电子邮件必填'})
#
#     def clean(self):
#         #1.校验用户名是否已经注册
#         user=User.objects.filter(username=self.cleaned_data.get('username'))
#         # 如果已经注册过
#         if user:
#             #抛出异常显示
#             raise forms.ValidationError({'username':'用户已经注册过'})
#
#         #2.校验密码和确认密码是否相同
#         #如果密码和确认的密码不相同
#         if self.cleaned_data.get('password')!=self.cleaned_data.get('password2'):
#             # 抛出异常显示
#             raise forms.ValidationError({'password2':'两次密码不相同'})
#
#         return self.cleaned_data
#
#
