from django.conf.urls import url
from django.contrib.staticfiles.templatetags.staticfiles import static

from fresh_shop import settings
from home import views

urlpatterns=[


    #首页
    url(r'^index/',views.index,name='index'),



    # #商品列表
    # url(r'^list/',views.list,name='list'),
    #
    #
    # #用户个人信息
    # url(r'^user_center_info',views.user_center_info,name='user_center_info'),
    #
    # #用户全部订单
    # url(r'^user_center_order',views.user_center_order,name='user_center_order'),
    #
    # #用户收货地址
    # url(r'^user_center_site',views.user_center_site,name='user_center_site'),






]



