from django.conf.urls import url

from orders import views

urlpatterns=[
    # 提交订单
    url(r'^place_order', views.place_order, name='place_order'),

]