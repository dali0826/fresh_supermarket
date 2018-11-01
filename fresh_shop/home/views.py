
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse


from goods.models import GoodsCategory, Goods
# from home.forms import UserForm
from users.models import User



#注册
# def register(request):
#     if request.method=='GET':
#         return render(request,'register.html')
#     if request.method=='POST':
#         #校验页面输入的信息，是否完整
#         form=UserForm(request.POST)
#         #is_valid（）：判断表单是否验证通过
#         if form.is_valid():
#             #获取校验后的用户名和密码
#             username=form.cleaned_data.get('username')
#             password=form.cleaned_data.get('password')
#             password2=form.cleaned_data.get('password2')
#             email=form.cleaned_data.get('email')
#             #判断密码是否相同
#             if password==password2:
#                 #创建普通用户create_user,创建超级管理员用户create_superuser
#                 User.objects.create(username=username,password=password)
#                 return HttpResponseRedirect(reverse('home:login'))
#             else:
#                 return render(request,'register.html')
#         else:
#             return render(request,'register.html',
#                           {'form':form})
#






#首页
def index(request):
    if request.method=='GET':

        #获取商品所有的分类
        category_types=GoodsCategory.CATEGORY_TYPE
        #按照id降序，获取商品
        goods=Goods.objects.all().order_by('-id')
        #循环商品分类，并组装结果
        data_all={}
        for type in category_types:
            data=[]
            count=0
            for good in goods:
                #计数count，大于5时，不再添加展示数据
                if count<5:
                    if type[0]==good.category.category_type:
                        data.append(good)
                        count+=1
            data_all['goods_'+str(type[0])]=data

        return render(request,'index.html',{'data_all':data_all,
                                            'catrgory_types':category_types})


#
# #商品列表
# def list(request):
#     if request.method=='GET':
#         return render(request,'list.html')
#
#
# #用户个人信息
# def user_center_info(request):
#     if request.method=='GET':
#         return render(request,'user_center_info.html')
#
# #用户全部订单
# def user_center_order(request):
#     if request.method=='GET':
#         return render(request,'user_center_order.html')
#
# #用户收货地址
# def user_center_site(request):
#     if request.method=='GET':
#         return render(request,'user_center_site.html')
