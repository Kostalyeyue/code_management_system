#ATM & 购物车（在ATM的第八个‘购物’功能里）
'''
1、print ATM system select_list
2、根据不同的choice分发不同的功能func（）
3,目前先实现了第1,2,3,8步骤
  ‘1':['登陆',login],
   '2':['注册',register],
   '3':['查看余额',my_earnings],
   '4':['转账',transfer],（目前存在一个error，不能讲改动了的余额数据重新写入data文本，有待改进）
   '5':['还款',repayment],
   '6':['取款',withdrawal],
   '7':['查看流水',check_running],
   '8':['购物',trade],（目前此步单独作为func()运行，为调用任何data出来给ATM使用，后续有待改进）
   '9':['查看购买商品',view_purchase],
}
4，目前先实现了单个模块的集成运行，后续在考虑大体框架的连通
'''

login_status={'user':None,'status':False}
db='atm_user.txt'
select_choice=[]
select_user=''

def auth(auth_type='file'):#login登陆功能的装饰器，实现登陆即保存数据，不用重复登陆
    def outter(func):
        def wrapper(*args,**kwargs):
            if login_status['user'] and login_status['status']:
                return func(*args,**kwargs)
            if auth_type == 'file':
                list_name = []
                list_pwd = []
                with open(db,encoding='utf-8') as f:
                  while True:
                    for line in f:
                        list_name.append(line.strip().split(',')[1])
                        list_pwd.append(line.strip().split(',')[2])
                        name = input('username>>>: ').strip()
                        pwd = input('password>>>: ').strip()
                        if name in list_name and pwd in list_pwd:
                            login_status['user'] = name
                            login_status['status'] = True
                            res = func(*args,**kwargs)
                            list_name.clear()
                            list_pwd.clear()
                            return res
                            break
                        else:
                            list_name.clear()
                            list_pwd.clear()
                            print('username or password error')
            elif auth_type == 'sql':
                   pass
            else:
                   pass
        return wrapper
    return outter

@auth(auth_type='file')
def login():
    '''
    目前的从txt文件查找user,pwd的方式比较low,因为为了后面增删改查的方便用的
    是for d in line的方式，后续可以考虑优化优化
    '''
    print('login successful')

def register():#严格按照输入模式注册新用户信息
    print('welcome to register:')
    print("请输入客户姓名，密码，余额形如：add into atm_user.txt alex,123,123455")
    command_data=input('输入您要注册的客户信息：')
    data=command_data.strip().split(' ')
    list_data=data[3].split(',')
    list_all=[]
    with open(db, 'r', encoding='utf-8') as f, \
            open('atm1234.txt', 'w', encoding='utf-8') as f_new:
            for line in f:
                list_all.append(line.strip().split(',')[1])
                f_new.write(line)
            if not list_data[0] in list_all:
                staff_id = str(len(list_all) + 1)
                list_data.insert(0, str(staff_id))
                f_new.write(','.join(list_data))
                print('注册成功')
            else:
                print("该用户已经存在")
                f.close()

@auth(auth_type='file')
def my_earnings():#调用文本查看余额
    print('welcome to view earnings')
    with open(db,encoding='utf-8') as f:
        for line in f:
            if login_status['user']==line.strip().split(',')[1]:
                balance=line.strip().split(',')[3]
        print('您所剩余额为：%s ¥'%(balance))

def transfer():
    '''
    只能转给同一登陆了ATM信息的客户,先实现简单的转账功能，暂不考虑同姓名问题
    '''
    print('welcome to transfer')
    transfer_name=input('who you want to transfer:').strip()
    transfer_money=input('how much money you want to transfer:').strip()
    transfer_bill=0
    transfered_bill=0
    with open(db, encoding='utf-8') as f, \
        open('atm1234.txt', 'w', encoding='utf-8') as f_write:
        for line in f:
            if transfer_name == line.strip().split(',')[1]:
                if transfer_money.isdigit():
                    transfer_money=int(transfer_money)
                    if transfer_money<=int(line.strip().split(',')[3]):
                        transfered_bill=int(line.strip().split(',')[3])+transfer_money
                        data=line.strip().split(',')[3].replace(line.strip().split(',')[3],str(transfer_bill))
                        f.write(data)         ###################################此步报错，io.UnsupportedOperation: not writable

    with open(db, encoding='utf-8') as f, \
            open('atm1234.txt', 'w', encoding='utf-8') as f_write:
         for line in f:
            if login_status['user'] == line.strip().split(',')[1]:
             transfer_bill=int(line.strip().split(',')[3])-transfer_money
             data = line.strip().split(',')[3].replace(line.strip().split(',')[3], transfer_bill)
             f.write(data)

def repayment():
    pass

def withdrawal():
    pass

def check_running():
    pass

def trade():
    login_status = {'user': None, 'status': False}
    shop_list = {
        '1': {'apple': 7000},
        '2': {'bicyle': 1000},
        '3': {'xiaomi': 3000},
        '4': {'huawei': 6000},
    }
    db = 'cache.txt'
    curr_user = ''
    shopping_cart = []

    def print_goodslist():  # 打印商品列表
        print('Here is the goodslist'.center(30, '-'))
        print('%s   %s   %s' % ('商品号', '商品名', '价格'))
        for i in shop_list:
            for j in shop_list[i]:
                print('%s   %s   %s' % (i, j, shop_list[i][j]))

    def showcar(data):  # d打印购物车列表
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
            def wrapper(*args, **kwargs):
                if login_status['user'] and login_status['status']:
                    return func(*args, **kwargs)

                if auth_type == 'file':
                    with open(db, encoding='utf-8') as f:
                        dic = eval(f.read())
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
                q_choice = input('please select:').strip()
                if q_choice == '1':
                    pass  # ATM结账
                    print('您已经消费成功，感谢您的惠顾')
                    break
                elif q_choice == '2':
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

def view_purchase():
    pass

atm_menu_show = {
   '1':['登陆',login],
   '2':['注册',register],
   '3':['查看余额',my_earnings],
   '4':['转账',transfer],
   '5':['还款',repayment],
   '6':['取款',withdrawal],
   '7':['查看流水',check_running],
   '8':['购物',trade],
   '9':['查看购买商品',view_purchase],
}

def main_atm():
    while True:
        print('welcome to use ATM system'.center(30,'-'))
        print('ATM功能表如下：'.center(30,'-'))
        for i in atm_menu_show:
            print('%s  %s'%(i,atm_menu_show[i][0]))
        choice=input('请输入您的选择(按q退出）：').strip()
        if choice=='q':
            break
        elif choice in atm_menu_show:
               atm_menu_show[choice][1]()
        else:
            print('输入格式错误')


main_atm()

