import threading
from unrar import rarfile
import os

import itertools as its
import time

from concurrent.futures import ThreadPoolExecutor


def get_pwd(file_path, output_path, pwd):
    '''
    判断密码是否正确
    :param file_path: 需要破解的文件路径，这里仅对单个文件进行破解
    :param output_path: 解压输出文件路径
    :param pwd: 传入的密码
    :return:
    '''
    # 传入被解压的文件路径，生成待解压文件对象
    file = rarfile.RarFile(file_path)
    # 输出解压后的文件路径
    out_put_file_path = 'rar/{}'.format(file.namelist()[0])
    try:
        file.extractall(path=output_path, pwd=pwd)
        print('成功解压')
    except Exception as e:
        return False
    try:
        # 如果发现文件被解压处理，移除该文件
        os.remove(out_put_file_path)
        # 说明当前密码有效，并告知
        print('Find password is "{}"'.format(pwd))
        return True
    except Exception as e:
        # 密码不正确
        # print('"{}" is nor correct password!'.format(pwd))
        # print(e)
        pass
        return False

# 多线程,类方式创建多线程
class MyThread(threading.Thread):
    """
    多线程,类方式创建多线程
    """
    def __init__(self,func,args=()):
        super(MyThread,self).__init__()
        self.func = func
        self.args = args


    def run(self):
        self.result = self.func(*self.args)

    def get_result(self):
        # 获取处理后的结果
        # 如果子线程不使用join方法，此处可能会报没有self.result的错误
        return self.result



def get_password(min_digits, max_digits, words):
    """
    密码生成器
    :param min_digits: 密码最小长度
    :param max_digits: 密码最大长度
    :param words: 密码可能涉及的字符
    :return: 密码生成器
    """
    while min_digits <= max_digits:
        pwds = its.product(words, repeat=min_digits)
        for pwd in pwds:
            yield ''.join(pwd)
        min_digits += 1


file_path = 'sss.rar'
output_path = r'sss'

# 密码范围
words = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'  # 涉及到生成密码的参数
# words = '123sun'
pwds = get_password(4, 10, words)
# 开始查找密码
start = time.time()
num = 0
flag = False
while True:
    try:
        pwd = next(pwds)
    except Exception as e:
        print('出现异常')
        num += 1
        if num > 10:
            break

    # t = MyThread(get_pwd,args=(file_path, output_path, pwd))
    # thread_list = []
    # thread_list.append(t)
    # t.start()
    # for t in thread_list:
    #     # 一定要join，不然主线程比子线程跑的快，会拿不到结果
    #     t.join()
    #     result = t.get_result()
    #     if result:
    #         flag = True
    #         break
    # if flag:
    #     break
    if get_pwd(file_path, output_path, pwd=pwd):
        break
end = time.time()
print('程序耗时{}'.format(end - start))