from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .models import notify
from django.contrib.auth.models import User
import datetime
from django.http import HttpResponse
from django.shortcuts import render
from datetime import date


class SignUp(generic.CreateView):

    form_class = UserCreationForm
    success_url = reverse_lazy('login')

    template_name = 'signup.html'

def notif(request):
    id=request.user.id
    x=request.user.date_joined
    x=(str)(x)
    x=x.split(" ")
    crntdate=x[0].split("-")
    uyr=(int)(crntdate[0])
    umn=(int)(crntdate[1])
    uday=(int)(crntdate[2])
    usertime=request.user.date_joined.strftime('%H:%M:%S')
    crr=datetime.datetime.now().strftime('%H:%M:%S')
    crd=datetime.datetime.now().date()

    crd=(str)(crd)
    crd=crd.split("-")
    crday=(int)(crd[2])
    crmn=(int)(crd[1])
    cry=(int)(crd[0])
    delta=date(cry,crmn,crday)-date(uyr,umn,uday)


    use=usertime.split(":")
    crtime=crr.split(":")
    useh=(int)(use[0])
    usem=(int)(use[1])
    crh,crm,crs=(int)(crtime[0]),(int)(crtime[1]),(int)(crtime[2])
    diffmn=0
    year=[0,31,28,31,30,31,30,31,31,30,31,30,31]
    diffnm=0

    if(delta.days==0):
        difhr=abs(crh-useh)
        mindf=abs(usem-crm)
    else:
        while(True):
            diffnm+=1
            usem+=1
            if(usem>60):
                usem=0
                useh+=1
                if(useh>24):
                    usem=0
                    useh=0
                    uday+=1
                    if(uday>year[umn]):
                        umn+=1
                        uday=1
                        usem=0
                        useh=0
                        if(umn>12):
                            umn=1
                            uday=1
                            usem=0
                            useh=0
                            uyr+=1
                            if (( uyr%400 == 0)or (( uyr%4 == 0 ) and ( uyr%100 != 0))):
                                year[2]==29
            if(uyr==cry and umn==crmn and uday==crday and useh==crh and usem==crm):
                break


    qwerty=notify.objects.all()
    res=[]
    for v in qwerty:
        time=(v.day*60*60)+(v.hrs*60)+v.min
        if(delta.days==0):
            if(((difhr*60)+mindf)>=time):
                res.append(v.notif)
        else:
            if(time<=diffnm):
                res.append(v.notif)
    return render(request,'notification.html',{'z' : res})
