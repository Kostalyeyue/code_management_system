#shopping mall
'''
1、打印商品列表
2、choice之后不同判断执行，加入购物车前先做购物车装饰器认证，认证一次就可以了
3、一直到选择‘q'结束，并计算打印结果
'''
login_status={'user':None,'status':False}
shop_list={
    '1':{'apple':7000},
    '2':{'bicyle':1000},
    '3':{'xiaomi':3000},
    '4':{'huawei':6000},
}
db='cache.txt'
curr_user=''
shopping_cart=[]

def print_goodslist():  #打印商品列表
    print('Here is the goodslist'.center(30,'-'))
    print('%s   %s   %s'%('商品号','商品名','价格'))
    for i in shop_list:
        for j in shop_list[i]:
             print('%s   %s   %s' % (i,j,shop_list[i][j]))

def showcar(data): #d打印购物车列表
    print("你的购物车列表：")
    sum = 0
    for i in data:
          for j in i:
             print("商品名：%-10s  价格：%s元" % (j, i[j]))
    sum += i[j]
    print("\t\t\t\t合计：%s元" % sum)
    return int(sum)

def auth(auth_type='file'):
    def outter(func):
        def wrapper(*args,**kwargs):
            if login_status['user'] and login_status['status']:
                return func(*args,**kwargs)

            if auth_type == 'file':
                with open(db,encoding='utf-8') as f:
                    dic=eval(f.read())
                name = input('username>>>: ').strip()
                pwd = input('password>>>: ').strip()
                if name in dic and pwd == dic[name]:
                    login_status['user'] = name
                    login_status['status'] = True
                    res = func(*args, **kwargs)
                    return res
                else:
                    print('username or password error')
            elif auth_type == 'sql':
                   pass

            else:
                   pass

        return wrapper
    return outter

@auth(auth_type='file')
def shopcar(name):
    shopping_cart.append(name)

def writelog():
    pass

def main_shopping():
    while True:
        print_goodslist()
        choice = input("请选择你要购买的商品号（按q结束,c查看购物车）：").strip()
        if choice and choice in shop_list:
            curr_user = shopcar(shop_list[choice])
            if curr_user:
                  print("加入购物车成功")
        elif choice == 'q':
            print('您目前已选择:'.center(30, '-'))
            shopping = showcar(shopping_cart)
            print('是否需要结账（1为结账，2为清空购物车退出）：')
            q_choice=input('please select:').strip()
            if q_choice=='1':
                pass       #ATM结账
                print('您已经消费成功，感谢您的惠顾')
                break
            elif q_choice=='2':
                shopping_cart.clear()
                break
            else:
                print('输入格式错误')
        elif choice == 'c':
            print('您目前已选择:'.center(30, '-'))
            shopping = showcar(shopping_cart)

        else:
            print("你选择的商品不存在，请重新选择:")

main_shopping()




















