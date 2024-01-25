from django.shortcuts import render,redirect
from .models import *
# Create your views here.
# def hamma_kitoblar(request):
#     data = {
#         "books":Kitob.objects.all()
#     }
#     return render(request,"kitoblar.html",data)

# def hamma_mualliflar(request):
#     data = {
#         "writers":Muallif.objects.all()
#     }
#     return render(request,"muallif.html",data)

def bitiruvchi_talaba(request):
    data = {
        "student":Talaba.objects.filter(kurs=3)
    }
    return render(request,"student.html",data)

def bitta_talaba(request,aw):
    data = {
        "bitta_talaba":Talaba.objects.get(id=aw)
    }
    return render(request,"bitta_ta.html",data)

def a_talaba(request):
    data = {
        "students":Talaba.objects.filter(ism__contains='a')
    }
    return render(request,"a_student.html",data)

#1-misol
def hamma_mualliflar(request):
    data = {
        "writers":Muallif.objects.all()
    }
    return render(request,"muallif.html",data)

#2-misol
def tanlangan(request,fr):
    data = {
        "selected":Muallif.objects.get(ism=fr)
    }
    return render(request,"tanlangan.html",data)
#3-misol
def hamma_kitoblar(request):
    data = {
        "books":Kitob.objects.all()
    }
    return render(request,"kitoblar.html",data)
#4-misol
def tan_kitob(request,rt):
    data = {
        "tan_book":Kitob.objects.get(id=rt)
    }
    return render(request,"kitob.html",data)
#5-misol
def hamma_recordlar(request):
    data = {
        "records":Record.objects.all()
    }
    return render(request,"record.html",data)
#6-misol
def tirik_muallif(request):
    data = {
        "life":Muallif.objects.filter(tirik="True")
    }
    return render(request,"life_time.html",data)
#7-misol
def sahifa_book(request):
    data = {
        "book3":Kitob.objects.all().order_by("-sahifa")[0:3]
    }
    return render(request,"kitob3.html",data)
#8-misol
def mehnatkash(request):
    data = {
        "toiler":Muallif.objects.all().order_by("-kitoblar_soni")[0:3]
    }
    return render(request,"toiler.html",data)
#9-misol
def mehnatkash(request):
    data = {
        "toiler":Muallif.objects.all().order_by("-kitoblar_soni")[0:3]
    }
    return render(request,"toiler.html",data)

#10-misol
def tirik_kitob(request):
    data = {
        "time":Kitob.objects.filter(muallif__tirik="True")
    }
    return render(request,"tirik_kitob.html",data)



# def hamma_talaba(request):
#     natija = Talaba.objects.all()
#     kiritilgan_ism = request.GET.get("ismi")
#     data = {
#         "student":Talaba.objects.all()
#     }
#     return render(request,"hamma_student.html",data)

def hamma_talaba(request):
    natija = Talaba.objects.all()
    kiritilgan_ism = request.GET.get("ism")
    if kiritilgan_ism is not None:
        natija = Talaba.objects.filter(ism__contains=kiritilgan_ism)
    data={
        "talaba": natija
    }
    return render(request, 'hamma_student.html', data)



def talaba_ochir(request,pk):
    Talaba.objects.get(id=pk).delete()
    return redirect("/student/")

def kitob_ochir(request,pk):
    Kitob.objects.get(id=pk).delete()
    return redirect("/jadval/")




