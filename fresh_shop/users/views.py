

from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from users.forms import UserRegisterForm, UserLoginForm
from users.models import User

#注册
def register(request):
    if request.method=='GET':

        return render(request,'register.html')
    if request.method=='POST':
        #表单验证
        #验证通过后，使用自定义的User.objects.cate
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            #保存
            User.objects.create(username=form.cleaned_data['user_name'],
                                password=make_password(form.cleaned_data['pwd']),
                                email=form.cleaned_data['email'])
            return HttpResponseRedirect(reverse('users:login'))
        else:
            return render(request,'register.html',{'form':form})


#登录
def login(request):
    if request.method=='GET':
        return render(request,'login.html')
    if request.method=='POST':
        form=UserLoginForm(request.POST)
        if form.is_valid():
            #获取当前登录的用户对象
            user=User.objects.filter(username=form.cleaned_data['username']).first()
            #验证密码是否正确
            if not check_password(form .cleaned_data['pwd'],user.password):
                return HttpResponseRedirect(reverse('users:login'))

            #添加登录成功的验证
            request.session['user_id']=user.id
            return HttpResponseRedirect(reverse('home:index'))
        else:
            return render(request,'login.html',{'form':form})