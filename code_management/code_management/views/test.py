# # import redis
# #
# # # r = redis.Redis(host='localhost',port='6379')
# # # r.set('wudi','shuai')
# # # print(r.get('wudi'))
# #
# # pool = redis.ConnectionPool(host='127.0.0.1',port='6379')
# #
# # r = redis.Redis(connection_pool=pool)
# # r.set('wu','牛')
# # print(r.get('wu'))
# #
# menu_list = [
# 				{'id':1,'title':'菜单1','pid':None},
# 				{'id':2,'title':'菜单2','pid':None},
# 				{'id':3,'title':'菜单3','pid':None},
# 				{'id':4,'title':'菜单1.1','pid':1},
# 				{'id':5,'title':'菜单1.2','pid':1},
# 				{'id':6,'title':'菜单2.1','pid':2},
# 				{'id':7,'title':'菜单3.1','pid':3},
# 				{'id':8,'title':'菜单1.1.1','pid':4},
# 				{'id':9,'title':'菜单1.2.1','pid':5},
# 				{'id':10,'title':'菜单4','pid':None},
# 			]
#
# # menu_dict = {}
# #
# # for item in menu_list:
# #     item['children'] = []
# #     menu_dict[item['id']] = item
# # # print(menu_dict)
# # print(menu_list)
# #
# #
# # reslut = []
# # for row in menu_list:
# #     pid = row['pid']
# #     if not pid:
# #         reslut.append(row)
# #         continue
# #     menu_dict[pid]['children'].append(row)
# #
# # # print(reslut)
#
# menu_dict = {}
# for key in menu_list:
#     key['children'] = []
#     menu_dict[key['id']] = key
#
# result = []
# for item in menu_list:
#     pid = item['pid']
#     if not pid:
#         result.append(item)
#         continue
#     menu_dict[pid]['children'] = item
#
# print(result)

# def index(list,key):
#     if key < list[0]:
#         position = 1
#     elif key > list[-1]:
#         position = len(list)
#     else:
#         for i in range(len(list)):
#             if key > list[i] and list[i+1] > key:
#                 position = i+1
#     return position
#
# a = [1,2,3,4,6,9]
# print(index(a,810))
#

