from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from cart.models import ShoppingCart
from goods.models import Goods

#加入购物车
def add_cart(request):
    if request.method=='POST':
        #添加到session中数据的格式为：
        #key--->goods
        #value---> [[id1,num,1],[id2,num,0],[id3,num,1]......]

        #1.没有登录时
        #1.1添加到购物车的数据，其实就是添加到session中
        #1.2如果商品已经加入到session中，则修改session中商品的个数
        #1.3,如果商品没有添加到session中，就添加

        #获取从ajax中传递的商品的id和商品的个数
        goods_id=request.POST.get('goods_id')
        goods_num=request.POST.get('goods_num')
        #组装存储的数结果
        goods_list=[goods_id,goods_num,1]
        #判断在session中是否存储了商品信息
        if request.session.get('goods'):
            #标识符：用于判断当前加入到购物车的商品
            #如果购物车中已经存在了该商品，就修改flag为1，否则flag还是0
            flag=0
            #说明购物车中已经存储了商品信息
            session_goods=request.session['goods']
            for goods in session_goods:
                #循环判断，判断加入到session中的商品是否已经存在session中
                if goods_id==goods[0]:
                    goods[1]=goods[1]+goods_num
                    flag=1
            #如果flag为0 ，就表示添加到session中的商品之前并没有添加
            if not flag:
                session_goods.append(goods_list)
            #修改成功session中 商品的信息
            request.session['goods']=session_goods
            cart_count=len(session_goods)
        else:
            #说明购物车中还没有储存商品信息
            data=[]
            data.append(goods_list)
            request.session['goods']=data
            cart_count=1

        return JsonResponse({'code':200,'cart_count':cart_count})


#购物车
def cart(request):
    if request.method=='GET':
        #需要判断用户是否登录， session['user_id']
        #1. 如果登录，则购物车中展示当前登录用户的购物车表中的数据
        #2.若没有登录，则在购物车中展示session中的数据
        user_id=request.session.get('user_id')
        if user_id:
            #登录系统用户，获取购物车中的商品信息

            shop_cart=ShoppingCart.objects.filter(user_id=user_id)
            goods_all=[(cart.goods,cart.is_select,cart.nums) for cart in shop_cart]

            return render(request,'cart.html',{'goods_all': goods_all})

        else:

            # 没有登录
            session_goods = request.session.get('goods')

            # 拿到session中所有的商品id值
            if session_goods:
                # [[goods objects, 是否选择 , 商品数量], [goods objects, 是否选择 , 商品数量]]
                goods_all = [(Goods.objects.get(pk=good[0]), good[2], good[1])
                             for good in session_goods]
            else:
                goods_all = ''

            return render(request, 'cart.html', {'goods_all': goods_all})


def f_price(request):
    """
    返回购物车或session中的商品价格，和总价
    {key:[[id1,price1],[id2,price2]],key2:total_price}
    """
    user_id=request.session.get('user_id')
    if user_id:
        #获取当前登录系统的用户的购物车的数据
        carts=ShoppingCart.objects.filter(user_id=user_id)
        cart_data={}
        cart_data['goods_price']=[ (cart.goods_id,cart.nums*cart.goos.shop_price) for cart in carts]
        all_price=0
        # 总的价格
        for cart in carts:
            if cart.is_select:
                all_price+=cart.nums*cart.goods.shop_price
        cart_data['all_price']=all_price
    else:
        # 拿到session中所有的商品信息goods=[id,num(数量),is_select（是否勾选）]
        session_goods = request.session.get('goods')
        #返回数据结构，{‘goods_price':[[id1,price1],[id2,price2]]    id：商品；price：商品的杰哥
        cart_data = {}
        data_all = []
        #计算总价
        all_price = 0
        for goods in session_goods:
            data = []
            data.append(goods[0])
            g = Goods.objects.get(pk=goods[0])
            data.append(int(goods[1]) * g.shop_price)
            #生成data为：[id1,price]
            data_all.append(data)
            # 判断如果商品勾选了，才计算总价
            if goods[2]:
                all_price += int(goods[1]) * g.shop_price
        cart_data['goods_price'] = data_all
        cart_data['all_price'] = all_price
    return JsonResponse({'code': 200, 'cart_data': cart_data})