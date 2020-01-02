from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from rest_framework.response import Response

from .forms import NameForm, ContactForm


@csrf_exempt
def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            data = {
                'code':'0',
                'msg':'success',
                'data':form.cleaned_data
            }
            return JsonResponse(data)
            # return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})



from django.core.mail import send_mail
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_frame.settings import STATICFILES_DIRS
def test_002(request):
    '''
    对form表单进行clean测试
    :param request:
    :return:
    '''
    data = {'subject': 'hello',
            'message': 'Hi there',
            'sender': 'foo@example.com',
            'cc_myself': True
            }
    path = STATICFILES_DIRS[0] + '/html/name.html'
    file_data = {'mugshot': SimpleUploadedFile('face.jpg', path)}
    if request.method == 'POST':
        form = ContactForm(data = request.POST,initial = data)
        # 判断表单数据是否发生变化
        if form.has_changed():
            if form.is_valid():
                subject = form.cleaned_data['subject']
                message = form.cleaned_data['message']
                sender = form.cleaned_data['sender']
                cc_myself = form.cleaned_data['cc_myself']
                recipients = ['info@example.com']
                if cc_myself:
                    recipients.append(sender)
                    print('有数据')
            # send_mail(subject, message, sender, recipients)
                #验证成功返回数据
                return JsonResponse(form.cleaned_data)
            else:
                # 验证失败返回数据
                return JsonResponse(form.errors)
        else:
            return JsonResponse(data)
        # return HttpResponseRedirect('/thanks/')
    else:
        form = ContactForm(data,file_data)
        form = form.as_ul()
        return render(request, 'name001.html', {'form': form})
