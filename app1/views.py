from django.shortcuts import render

# Create your views here.
from app1.models import*
def topic(request):
    QLTO=Topic.objects.all()
    d={'topic':QLTO}
    return render(request,'topic.html',d)

def webpage(request):
    QLWO=Webpage.objects.all()
    d={'webpage':QLWO}
    return render(request,'webpage.html',d)


def accessrecord(request):
    QLAO=AccessRecord.objects.all()
    d={'accessrecord':QLAO}
    return render(request,'accessrecord.html',d)

def inserttopic(request):
    tn=input('enter topic name')
    NTO=Topic.objects.get_or_create(topic_name=tn)[0]
    NTO.save()
    QLTO=Topic.objects.all()
    d={'topic':QLTO}
    return render(request,'topic.html',d)

def insertwebpage(request):
    tn=input('enter tn')
    n=input('enter name')
    u=input('enter url')
    to=Topic.objects.get(topic_name=tn)
    NWO=Webpage.objects.get_or_create(topic_name=to,name=n,url=u)[0]
    NWO.save()
    QLWO=Webpage.objects.all()
    d={'webpage':QLWO}
    return render(request,'webpage.html',d)

def insertaccessrecord(request):
    pk=int(input('enter pk value of webpage'))
    d=input('enter date')
    a=input('enter author')
    wo=Webpage.objects.get(pk=pk)
    NAO=AccessRecord.objects.get_or_create(name=wo,author=a,date=d)[0]
    NAO.save()
    QLAO=AccessRecord.objects.all()
    d={'accessrecord':QLAO}
    return render(request,'accessrecord.html',d)


























    return HttpResponse('accessrecord is created')


