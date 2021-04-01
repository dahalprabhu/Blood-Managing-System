from django.shortcuts import render,redirect
from .models import bloodmanagement
from django.shortcuts import HttpResponse
from .models import cust
from django.db.models import Q
from django.contrib import auth,messages
from django.http import *
from .models import campaign
from .models import redcross_donater
from .models import hackersclub_donater
from .models import cust

import csv
# Create your views here.
def index(request):
    
    return render(request,"home.html")

    
def profile(request):
    obj=cust.objects.all() 
    return render(request,"profile.html",{"obj":obj})
    

def info(request):
    obj=bloodmanagement.objects.all() 
    obj1=cust.objects.all() 
    return render(request,"info.html",{"obj":obj},{"obj1":obj1})


def search(request):
  if request.method== 'POST':
    srch = request.POST['srh']
    if srch:
     
      match = bloodmanagement.objects.filter(Q(blood_group__icontains=srch))
      
      if match:
        return render(request,'search.html',{'sr':match})
      else:
                messages.error(request,'no results found')
    else:
            return HttpResponseRedirect('/search')
    
            
    return render(request,'search.html')                   
         
def upload_fetch(request):

  upls=campaign.objects.all()
  return render (request, 'info.html', {'upls':upls})

def upload(request):
    if request.method=='POST':
        Camp_name=request.POST['camp_name']
        Venue=request.POST['venue']
        datetime=request.POST['datetime']
        file1=request.FILES['img']
        desc=request.POST['desc']

        Campaign=campaign.objects.create(camp_name=Camp_name , venue=Venue , time=datetime , img=file1 , desc=desc )
        Campaign.save()
        print( 'campaign created')
        return redirect('/info.html')
    else:
        return render ( request, 'upload.html')

def barchart1(request):
    c=0
    d=0
    e=0
    f=0
    g=0
    h=0
    i=0
    queryset = bloodmanagement.objects.all()
    for qset in queryset:
        asa=qset.blood_group
        if asa=='O+ve':
            c=c+1    
        elif asa=='O-ve':
            d=d+1
        elif asa=='B+ve':
            e=e+1
        elif asa=='B-ve':
            f=f+1
        elif asa=='A+ve':
            g=g+1
        elif asa=='A-ve':
            h=h+1
        else:
            i=i+1
    return render(request, 'hackersclub.html', {'setss':[c,d,e,f,g,h,i], 'queryset':queryset})



def getfile1(request):
    if request.method=='POST':
        response=HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="file.csv"' 
        bms=bloodmanagement.objects.all()
        writer=csv.writer(response)
        for bm in bms:
            writer.writerow([bm.name,bm.age1, bm.blood_group,bm.phone_no,bm.address])
        return response
    else:
        return render (request,'hackersclub.html',)

def barchart2(request):
    c=0
    d=0
    e=0
    f=0
    g=0
    h=0
    i=0
    queryset = redcross_donater.objects.all()
    for qset in queryset:
        asa=qset.blood_group
        if asa=='O+ve':
            c=c+1    
        elif asa=='O-ve':
            d=d+1
        elif asa=='B+ve':
            e=e+1
        elif asa=='B-ve':
            f=f+1
        elif asa=='A+ve':
            g=g+1
        elif asa=='A-ve':
            h=h+1
        else:
            i=i+1
    return render(request, 'hackersclub.html', {'setss':[c,d,e,f,g,h,i], 'queryset':queryset})



def getfile2(request):
    if request.method=='POST':
        response=HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="file.csv"' 
        bms=redcross_donater.objects.all()
        writer=csv.writer(response)
        for bm in bms:
            writer.writerow([bm.name,bm.age1, bm.blood_group,bm.phone_no,bm.address])
        return response
    else:
        return render (request,'hackersclub.html',)

def barchart3(request):
    c=0
    d=0
    e=0
    f=0
    g=0
    h=0
    i=0
    queryset = hackersclub_donater.objects.all()
    for qset in queryset:
        asa=qset.blood_group
        if asa=='O+ve':
            c=c+1    
        elif asa=='O-ve':
            d=d+1
        elif asa=='B+ve':
            e=e+1
        elif asa=='B-ve':
            f=f+1
        elif asa=='A+ve':
            g=g+1
        elif asa=='A-ve':
            h=h+1
        else:
            i=i+1
    return render(request, 'hackersclub.html', {'setss':[c,d,e,f,g,h,i], 'queryset':queryset})



def getfile3(request):
    if request.method=='POST':
        response=HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="file.csv"' 
        bms=hackersclub_donater.objects.all()
        writer=csv.writer(response)
        for bm in bms:
            writer.writerow([bm.name,bm.age1, bm.blood_group,bm.phone_no,bm.address])
        return response
    else:
        return render (request,'hackersclub.html',)


def barchart4(request):
    c=0
    d=0
    e=0
    f=0
    g=0
    h=0
    i=0
    queryset = cust.objects.all()
    for qset in queryset:
        asa=qset.blood_group
        if asa=='O+ve':
            c=c+1    
        elif asa=='O-ve':
            d=d+1
        elif asa=='B+ve':
            e=e+1
        elif asa=='B-ve':
            f=f+1
        elif asa=='A+ve':
            g=g+1
        elif asa=='A-ve':
            h=h+1
        else:
            i=i+1
    return render(request, 'hackersclub.html', {'setss':[c,d,e,f,g,h,i], 'queryset':queryset})


def getfile4(request):
    if request.method=='POST':
        response=HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="file.csv"' 
        bms=cust.objects.all()
        writer=csv.writer(response)
        for bm in bms:
            writer.writerow([bm.name,bm.age1, bm.blood_group,bm.phone_no,bm.address])
        return response
    else:
        return render (request,'hackersclub.html')

def new(request):
    return render(request,"test.html")