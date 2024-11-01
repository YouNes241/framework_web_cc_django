from django.shortcuts import render , get_object_or_404
from collec_management.models import Collec

def about(request) :
    return render(request, 'about.html')

def collec_infos(request,n) :
    collecn = get_object_or_404(Collec,id=n)
    return render(request, 'collecinfos.html',{'collec':collecn})

def collec_list(request) :
    collec_list = Collec.objects.order_by("-date")
    return render(request,'all.html',{'collec_list':collec_list})