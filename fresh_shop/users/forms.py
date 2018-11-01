
from django import forms

from users.models import User

#注册时候的验证
class UserRegisterForm(forms.Form):
    """
    用户注册验证表单
    """

    user_name=forms.CharField(required=True,max_length=20,min_length=5,
                              error_messages={'required':'用户名必填',
                                              'max_lenght':'用户名最长不能超过20个字符',
                                              'min_lenght':'用户名最少5个字符'})
    pwd=forms.CharField(required=True,max_length=20,min_length=8,
                              error_messages={'required':'密码必填',
                                              'max_lenght':'用户名最长不能超过20位',
                                              'min_lenght': '用户名最少8个字符'})

    pwdc=forms.CharField(required=True,max_length=20,min_length=8,
                              error_messages={'required':'确认密码必填',
                                              'max_lenght':'用户名最长不能超过20位',
                                              'min_lenght': '用户名最少8个字符'})

    email = forms.CharField(required=True,
                            error_messages={'required': '电子邮件必填'})

    allow=forms.CharField(required=True,
                          error_messages={'required':'使用协议必选'})



    def clean(self):
        username=self.cleaned_data.get('user_name')
        pwd=self.cleaned_data.get('pwd')
        pwdc=self.cleaned_data.get('pwdc')

        #1.校验用户名是否已经注册
        user=User.objects.filter(username=username)
        # 如果已经注册过
        if user:
            #抛出异常显示
            raise forms.ValidationError({'username':'用户已经注册过'})

        #2.校验密码和确认密码是否相同
        #如果密码和确认的密码不相同
        if pwd!=pwdc:
            # 抛出异常显示
            raise forms.ValidationError({'pwd':'两次密码不相同'})

        # return self.cleaned_data




#登录时候的验证
class UserLoginForm(forms.Form):
    username = forms.CharField(required=True, max_length=20, min_length=5,
                                error_messages={'required': '用户名必填',
                                                'max_lenght': '用户名最长不能超过20个字符',
                                                'min_lenght': '用户名最少5个字符'})
    pwd = forms.CharField(required=True, max_length=20, min_length=8,
                          error_messages={'required': '密码必填',
                                          'max_lenght': '用户名最长不能超过20位',
                                          'min_lenght': '用户名最少8个字符'})

    def clean(self):
        #验证用户名是否注册过
        user=User.objects.filter(username=self.cleaned_data.get('username'))
        if not user:
            raise forms.ValidationError({'username':'没有用户，请注册'})
        # return self.cleaned_data