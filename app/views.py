from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.models import *

def insert_topic(request):
    tn=input('enter the topic name')
    TO=Topic.objects.get_or_create(topic_name=tn)
    if TO[1]:
        return HttpResponse('topic name is created')
    else:
        return HttpResponse('topic name is already exists')
    
    
def insert_webpage(request):
    tn=input('enter topic name')
    TO=Topic.objects.get(topic_name=tn)
    na=input('enter name')
    url=input('enter url')
    
    TWO=WebPage.objects.get_or_create(topic_name=TO,name=na,url=url)
    if TWO[1]:
        return HttpResponse('webpage is created')
    else:
        return HttpResponse('webpage is already exists')
    

def insert_webpage(request):
    tn=input('enter topic name')
    LTO=Topic.objects.filter(topic_name=tn)
    if LTO:
        TO=LTO[0]
        na=input('enter name')
        url=input('enter url')

        TWO=WebPage.objects.get_or_create(topic_name=TO,name=na,url=url)
        if TWO[1]:
            return HttpResponse('webpage is created')
        else:
            return HttpResponse('webpage is already exists')
        
    else:
        return HttpResponse('topic is not available,please enter valid data')
    
# def insert_accessrecord(request):
#     tn=input('enter topic name')
#     LTO=Topic.objects.filter(topic_name=tn)
#     if LTO:
#         TO=LTO[0]
#         na=input('enter name')
#         url=input('enter url')

#         LWO=WebPage.objects.filter(topic_name=TO,name=na,url=url)
#         if LWO:
#             WO=LWO[0]
#             an=input('enter author name')
#             da=input('enter date')
#             ARO=AccessRecord.objects.get_or_create(name=WO,author=an,date=da)
#             if ARO[1]:
#                 return HttpResponse('accessrecord is created')
#             else:
#                 return HttpResponse('accessrecord is already exists')
#         else:
#             return HttpResponse('webpage is not available,please enter valid data')
#     else:
#         return HttpResponse('topic is not available,please enter valid data')

def insert_accessrecord(request):
    wid=int(input('enter webpage id'))
    WO=WebPage.objects.get(id=wid)
    author=input('enter the author name')
    date=input('enter the date')
    ARO=AccessRecord.objects.get_or_create(name=WO,author=author,date=date)
    if ARO[1]:
        return HttpResponse('accessrecord is created')
    else:
        return HttpResponse('accessrecord is already exists')


def display_topic(request):
    QLTO=Topic.objects.all()
    d={'QLTO':QLTO}
    return render(request,'display_topic.html',d)
def display_webpage(request):
    QLWO=WebPage.objects.all()
    d={'QLWO':QLWO}
    return render(request,'display_webpage.html',d)
def display_accessrecord(request):
    QLAO=AccessRecord.objects.all()
    QLAO=AccessRecord.objects.filter(date='2025-10-11')
    
    d={'QLAO':QLAO}
    return render(request,'display_accessrecord.html',d)
def update_webpage(request):
    #updating query
    # WebPage.objects.filter(name='msd').update(url='https://msdhoni.com')
    # WebPage.objects.filter(topic_name='football').update(email='ronaldo@gmail.com')
    # WebPage.objects.filter(name='ashwin').update(url='https://ashwin.com')
    # WebPage.objects.filter(name='rohit').update(topic_name='cricket')
    # WebPage.objects.filter(name='virat').update(topic_name='chess')
    
    # WebPage.objects.update_or_create(name='virat',defaults={'url':'https://viratkohli.com'})
    # WebPage.objects.update_or_create(topic_name='cricket' ,defaults={'email':'cricket@gmail.com'})
    # WebPage.objects.update_or_create(name='raina', defaults={'url':'https://viratkohli.gmail.com'})
    
    CTO=Topic.objects.get(topic_name='cricket')
    # WebPage.objects.update_or_create(name='msd',defaults={'topic_name':CTO})
    
    WebPage.objects.update_or_create(name='raina',defaults={'topic_name':CTO})
    
    #after updation we are fetching all the data
    QLWO=WebPage.objects.all()
    d={'QLWO':QLWO}
    return render(request,'display_webpage.html',d)

def delete_webpage(request):
    WebPage.objects.filter(name='ronaldo').delete()
    WebPage.objects.filter(name='messi').delete()
    
    QLWO=WebPage.objects.all()
    d={'QLWO':QLWO}
    return render(request,'display_webpage.html',d)