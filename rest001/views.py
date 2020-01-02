import random
import string

from celery.result import AsyncResult
from django.http import HttpResponse, JsonResponse
from rest_framework import status

from .models import User_info

def re_data():
    data = {
        'code': '',
        'msg': '',
        'data': ''
    }
    return data
# Create your views here.
# 登录
def login(request):
    data = re_data()
    try:
        email = request.GET['email']
        password = request.GET['password']
    except Exception as e:
        data['code'] = '1003'
        data['msg'] = '请输入email号'
        return JsonResponse(data)
    queryset = User_info.objects.filter(email = email).first()
    if queryset:
        if queryset.password == password:
            data['msg'] = 'success'
            data['code'] = status.HTTP_200_OK
            data['data'] = queryset
            return JsonResponse(data)
        else:
            data['msg'] = 'password is error'
            data['code'] = '1001'
            return JsonResponse(data)
    else:
        data['msg'] = 'username is not find'
        data['code'] = '1002'
        return JsonResponse(data)

# 注册
def register(request):
    data = re_data()
    try:
        email = request.GET['email']
        password = request.GET['password']
    except Exception as e:
        data['code'] = '1004'
        data['msg'] = '请输入email号'
        return JsonResponse(data)
    queryset = User_info.objects.filter(email=email).first()
    if queryset:
        data['code'] = '1005'
        data['msg'] = '用户已经注册，请返回登录'
        return JsonResponse(data)
    else:
        User_info.objects.create(email=email,password=password)
        data['msg'] = 'success'
        data['code'] = status.HTTP_200_OK
        data['data'] = {'email':email,'password':password}
        return JsonResponse(data)

#对文件进行切片读取
def file_iterator(file_path, chunk_size=512):
    """
        文件读取迭代器
    :param file_path:文件路径
    :param chunk_size: 每次读取流大小
    :return:
    """
    with open(file_path, 'rb') as target_file:
        while True:
            chunk = target_file.read(chunk_size)
            if chunk:
                yield chunk
            else:
                break
# 对文件进行下载
def download(request):
    """
        文件下载
    :return:
    """
    # file_path = request.values.get('filepath')
    file_name = 'FontAwesome.otf'
    file_path = r'E:\code1\rest_frame\static\fonts\FontAwesome.otf'
    if request.method == "GET":
        response = HttpResponse(file_iterator(file_path))
        response['Content-Type'] = 'application/octet-stream'  # 设置头信息，告诉浏览器这是个文件
        response['Content-Disposition'] = f'attachment;filename="{file_name}"'
        return response


from rest001.tasks import send_email, add1


# def first_celery(request):
#     # 任务函数的异步调用
#     data = re_data()
#     ema = request.GET['email']
#     # ema = 'tiejipiaoliu@163.com'
#     code = random.sample(string.ascii_lowercase + string.ascii_uppercase + string.digits, 5)
#     code = "".join(code)
#
#     # res = add1.apply_async((3,4))
#     # res = add1.delay(3,4)
#     res = send_email.delay(ema,{'code':code})
#     print(res)
#     async_1 = AsyncResult(id=res.id)
#     print(async_1)
#     if async_1.successful():
#         # 得到执行完成的结果
#         # result = async_1.get()
#         data['data'] = {'id': res.id}
#         data['code'] = status.HTTP_200_OK
#         data['msg'] = '成功发送'
#         # result.forget()  # 将结果删除,执行完成，结果不会自动删除
#         # async.revoke(terminate=True)  # 无论现在是什么时候，都要终止
#         # async.revoke(terminate=False) # 如果任务还没有开始执行呢，那么就可以终止。
#     elif async_1.failed():
#         data['code'] = '1001'
#         data['msg'] = '执行失败'
#
#     elif async_1.status == 'PENDING':
#         data['code'] = '1002'
#         data['msg'] = '任务等待中被执行'
#
#     elif async_1.status == 'RETRY':
#         data['code'] = '1003'
#         data['msg'] = '任务异常后正在重试'
#
#     elif async_1.status == 'STARTED':
#         data['code'] = '1004'
#         data['msg'] = '任务已经开始被执行'
#
#     # send_register_email.delay('3069582567@qq.com')
#     return JsonResponse(data)

# 根据在redis中存储的键取出对应的值，在取出值后销毁该值
# def serch_result(request):
#     async_1 = AsyncResult(id="42685fbd-d5c1-4701-be01-0e3b6a47d05a")
#     print('async_1',async_1)
#     if async_1.successful():
#         result = async_1.get()
#         print(result)
#         # result.forget() # 将结果删除
#     elif async_1.failed():
#         print('执行失败')
#     elif async_1.status == 'PENDING':
#         print('任务等待中被执行')
#     elif async_1.status == 'RETRY':
#         print('任务异常后正在重试')
#     elif async_1.status == 'STARTED':
#         print('任务已经开始被执行')
#     return HttpResponse('123')


import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
def show_pdf(request):
    '''
    根据数据生成PDF文件
    :param request:
    :return:
    '''

    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=False, filename='hello.pdf')



# -*- coding: utf-8 -*-


from reportlab.pdfgen.canvas import Canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
pdfmetrics.registerFont(UnicodeCIDFont('STSong-Light'))
from reportlab.pdfbase.ttfonts import TTFont
pdfmetrics.registerFont(TTFont('msyh', 'E:/code1/rest_frame/static/fonts/fontawesome-webfont.ttf'))
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer,Image,Table,TableStyle
import time

def rpt():
    story=[]
    stylesheet=getSampleStyleSheet()
    normalStyle = stylesheet['Normal']

    curr_date = time.strftime("%Y-%m-%d", time.localtime())

    #标题：段落的用法详见reportlab-userguide.pdf中chapter 6 Paragraph
    rpt_title = '<para autoLeading="off" fontSize=15 align=center><b><font face="msyh">XX项目日报%s</font></b><br/><br/><br/></para>' %(curr_date)
    story.append(Paragraph(rpt_title,normalStyle))

    text = '''<para autoLeading="off" fontSize=8><font face="msyh" >程度定义：</font><br/>
    <font face="msyh" color=red>1.Blocker：指系统无法执行。</font><br/><font face="msyh" fontsize=7>例如：系统无法启动或退出等</font><br/>
    <font face="msyh" color=orange>2.Critical：指系统崩溃或严重资源不足、应用模块无法启动或异常退出、无法测试、造成系统不稳定。</font><br/>
    <font face="msyh" fontsize=7>例如：各类崩溃、死机、应用无法启动或退出、按键无响应、整屏花屏、死循环、数据丢失、安装错误等
    </font><br/>
    <font face="msyh" color=darkblue>3.Major：指影响系统功能或操作，主要功能存在严重缺陷，但不会影响到系统稳定性、性能缺陷</font><br/><font face="msyh" fontsize=7>例如：功能未做、功能实现与需求不一致、功能错误、声音问题、流程不正确、兼容性问题、查询结果不正确、性能不达标等
    </font><br/>
    <font face="msyh" color=royalblue>4.Minor：指界面显示类问题</font><br/>
    <font face="msyh" fontsize=7>例如：界面错误、边界错误、提示信息错误、翻页错误、兼容性问题、界面样式不统一、别字、排列不整齐，字体不符规范、内容、格式、滚动条等等
    </font><br/>
    <font face="msyh" color=grey>5.Trivial：本状态保留暂时不用</font><br/>
    </para>'''
    story.append(Paragraph(text,normalStyle))

    text = '<para autoLeading="off" fontSize=9><br/><br/><br/><b><font face="msyh">五、BUGLIST：</font></b><br/></para>'
    story.append(Paragraph(text,normalStyle))

    #图片，用法详见reportlab-userguide.pdf中chapter 9.3 Image
    img = Image('E:/code1/rest_frame/static/images/m.jpg')
    img.drawHeight = 20
    img.drawWidth = 28

    #表格数据：用法详见reportlab-userguide.pdf中chapter 7 Table
    component_data= [['模块', '', '', '',img,''],
    ['标记','bug-1','Major','some wrong','open','unresolved'],
    ['','bug-1','Major','some wrong','closed','fixed'],
    ]
    #创建表格对象，并设定各列宽度
    component_table = Table(component_data, colWidths=[20,50,50, 150, 90, 90])
    #添加表格样式
    component_table.setStyle(TableStyle([
    ('FONTNAME',(0,0),(-1,-1),'msyh'),#字体
    ('FONTSIZE',(0,0),(-1,-1),6),#字体大小
    ('SPAN',(0,0),(3,0)),#合并第一行前三列
    ('BACKGROUND',(0,0),(-1,0), colors.lightskyblue),#设置第一行背景颜色
    ('SPAN',(-1,0),(-2,0)), #合并第一行后两列
    ('ALIGN',(-1,0),(-2,0),'RIGHT'),#对齐
    ('VALIGN',(-1,0),(-2,0),'MIDDLE'),  #对齐
    ('LINEBEFORE',(0,0),(0,-1),0.1,colors.grey),#设置表格左边线颜色为灰色，线宽为0.1
    ('TEXTCOLOR',(0,1),(-2,-1),colors.royalblue),#设置表格内文字颜色
    ('GRID',(0,0),(-1,-1),0.5,colors.red),#设置表格框线为红色，线宽为0.5
    ]))
    story.append(component_table)

    doc = SimpleDocTemplate('D:/python/bugstatdev/rpt/bug.pdf')
    doc.build(story)

if __name__ == '__main__':
    rpt()