# # from functools import reduce
# # from mailcap import show
#
# # import QQ as QQ
# # from Tools.demo.beer import n
# # from Tools.scripts.mailerdaemon import x
#
# # res1 = reduce(lambda x,y:x+y,range(2,6),2)
# # print("ONE:",res1)
# # from Tools.scripts.dutree import show
# # from PIL.ImageShow import show
# # from matplotlib.pyplot import show
# # from numpy.__config__ import show
# import QQ as QQ
# from Tools.demo.beer import n
# from Tools.scripts.dutree import show
#
# res2 = show(n(QQ(7/3),digits=12))
# print("TWO:",res2)
#
# # x=2
# # def f(x):
# #     return x^4
# # print(map(f,range(1,5)))
# # print(f(1))
# # for i in res3:
# #     print(i)
# # print('res3:',res3)
#
# # key = ['name','age']
# # value = ['sun',20]
# # res = dict(zip(key,value))
# # print(res)
# #
# # res4 = list(zip(range(5),range(5,10)))
# # print("res4:",res4)
#
# # res5 = filter(lambda x:x>4,range(8))
# # print("res5:",list(res5))
# import json
#
# with open('et.json','r', encoding='utf-8') as f:
#     load_dict = json.load(f)
#     print(load_dict)


import json
import re
import demjson
with open('st.txt','r', encoding='utf-8') as f:
    res = f.read()
    data = demjson.decode(res.replace('\n','').replace('\t','').replace(' ',''))
    data = str(data).replace("'",'"')
    print(data)

    res = res.replace('\n','').replace('\t','').replace(' ','').replace(',]',']').replace(',}','}').replace('{','{"').replace(':','":').replace("'",'"').replace('",','","')
    print(res)