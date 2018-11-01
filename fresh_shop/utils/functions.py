import datetime
import random

def get_order_sn():
    """
    生成随机编号

    """
    sn=''
    s='sadfhfijkcmcjfij'
    for i in range(10):
        sn+=random.choice(s)
    sn+=datetime.now().strftime('%Y%m%d%H%M%S')

    return sn
