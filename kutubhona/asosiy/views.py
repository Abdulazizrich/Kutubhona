from django.shortcuts import render, redirect
from .forms import *


# Create your views here.
def hamma_kitoblar(request):
    data = {
        "books": Kitob.objects.all(),
        "mualliflar": Muallif.objects.all()
    }
    return render(request, "kitoblar.html", data)


# def hamma_mualliflar(request):
#     data = {
#         "writers":Muallif.objects.all()
#     }
#     return render(request,"muallif.html",data)

def bitiruvchi_talaba(request):
    data = {
        "student": Talaba.objects.filter(kurs=3)
    }
    return render(request, "student.html", data)


def bitta_talaba(request, aw):
    data = {
        "bitta_talaba": Talaba.objects.get(id=aw)
    }
    return render(request, "bitta_ta.html", data)


def a_talaba(request):
    data = {
        "students": Talaba.objects.filter(ism__contains='a')
    }
    return render(request, "a_student.html", data)


# Vazifa.Lesson 5. View va url yozish.
# 1-misol
def hamma_mualliflar(request):
    # if request.method == "POST":
    # Muallif.objects.create(
    #     ism=request.POST.get("ismi"),
    #     jins=request.POST.get("j"),
    #     tugilgan_sana=request.POST.get("t_s"),
    #     kitoblar_soni=request.POST.get("k_s"),
    #     tirik=True
    # )
    # return redirect("/royhat")
    data = {
        "writers": Muallif.objects.all()
    }
    return render(request, "muallif.html", data)


# 2-misol
def tanlangan(request, fr):
    data = {
        "selected": Muallif.objects.get(ism=fr)
    }
    return render(request, "tanlangan.html", data)


# 3-misol
# def hamma_kitoblar(request):
#     data = {
#         "books":Kitob.objects.all()
#     }
#     return render(request,"kitoblar.html",data)
# 4-misol
def tan_kitob(request, rt):
    data = {
        "tan_book": Kitob.objects.get(id=rt)
    }
    return render(request, "kitob.html", data)


# 5-misol
def hamma_recordlar(request):
    data = {
        "records": Record.objects.all()
    }
    return render(request, "record.html", data)


# 6-misol
def tirik_muallif(request):
    data = {
        "life": Muallif.objects.filter(tirik="True")
    }
    return render(request, "life_time.html", data)


# 7-misol
def sahifa_book(request):
    data = {
        "book3": Kitob.objects.all().order_by("-sahifa")[0:3]
    }
    return render(request, "kitob3.html", data)


# 8-misol
def mehnatkash(request):
    data = {
        "toiler": Muallif.objects.all().order_by("-kitoblar_soni")[0:3]
    }
    return render(request, "toiler.html", data)


# 9-misol
def record_sana(request):
    data = {
        "record": Record.objects.all().order_by("-olingan_sana")[0:3]
    }
    return render(request, "record_sana.html", data)


# 10-misol
def tirik_kitob(request):
    data = {
        "time": Kitob.objects.filter(muallif__tirik="True")
    }
    return render(request, "tirik_kitob.html", data)


# 11-misol
def kitob_badiiy(request):
    data = {
        "badiiy": Kitob.objects.filter(janr="Badiiy")
    }
    return render(request, "best.html", data)


# 12-misol
def katta_yosh(request):
    data = {
        "katta3": Muallif.objects.all().order_by("tugilgan_sana")[0:3]
    }
    return render(request, "old.html", data)


# 13-misol
def kitob_10(request):
    data = {
        "kitob10": Kitob.objects.filter(muallif__kitoblar_soni__lt=10)
    }
    return render(request, "kitobx.html", data)


# 14-misol
def tan_id(request, jt):
    data = {
        "tanla_id": Record.objects.get(id=jt)
    }
    return render(request, "Recordid.html", data)


# 15-misol
def Record_4(request):
    data = {
        "four": Record.objects.filter(talaba__kurs=4)
    }
    return render(request, "record4.html", data)


# def hamma_talaba(request):
#     natija = Talaba.objects.all()
#     kiritilgan_ism = request.GET.get("ismi")
#     data = {
#         "student":Talaba.objects.all()
#     }
#     return render(request,"hamma_student.html",data)

def hamma_talaba(request):
    if request.method == "POST":
        Talaba.objects.create(
            ism=request.POST.get("ismi"),
            kurs=request.POST.get("k"),
            kitob_nomi=request.POST.get("k_s")
        )
        return redirect("/talabalar")
    natija = Talaba.objects.all()
    kiritilgan_ism = request.GET.get("ism")
    if kiritilgan_ism is not None:
        natija = Talaba.objects.filter(ism__contains=kiritilgan_ism)
    data = {
        "talaba": natija
    }
    return render(request, 'hamma_student.html', data)


def talaba_ochir(request, pk):
    Talaba.objects.get(id=pk).delete()
    return redirect("/student/")


def kitob_ochir(request, pk):
    Kitob.objects.get(id=pk).delete()
    return redirect("/jadval/")


def talaba_tahrirlash(request, id):
    if request.method == 'POST':
        talaba = Talaba.objects.get(id=id)
        talaba.ism = request.POST['ismi']
        talaba.kurs = request.POST['k']
        talaba.kitob_nomi = request.POST['k_s']
        talaba.save()
        return redirect('/talabalar/')
    context = {
        'talaba': Talaba.objects.get(id=id)
    }
    return render(request, 'talaba_tahrirlash.html', context)


# Vazifa 1.Tahrirlash
# 1-misol
def hamma_kutubhonachilar(request):
    data = {
        "lib": Kutubhonachi.objects.all()
    }
    return render(request, "all_lib.html", data)


def kutubhonachi_tahrirlash(request, id):
    if request.method == 'POST':
        kutubhonachi = Kutubhonachi.objects.get(id=id)
        kutubhonachi.ism = request.POST['ismi']
        kutubhonachi.ish_vaqti = request.POST['iv']
        kutubhonachi.save()
        return redirect('/kutub/')
    context = {
        'kutubhonachi': Kutubhonachi.objects.get(id=id)
    }
    return render(request, 'kutub_tahrirlash.html', context)


# 2-misol
def muallif_tahrirlash(request, id):
    if request.method == 'POST':
        muallif = Muallif.objects.get(id=id)
        muallif.ism = request.POST['ismi']
        muallif.jins = request.POST['j']
        muallif.tugilgan_sana = request.POST['t_s']
        muallif.kitoblar_soni = request.POST['k_s']
        muallif.tirik = request.POST.get('Tirik', False) == 'on'
        muallif.save()
        return redirect('/royhat/')
    context = {
        'muallif': Muallif.objects.get(id=id)
    }
    return render(request, 'muallif_tahrirlash.html', context)


# 3-misol
def record_tahrirlash(request, id):
    if request.method == 'POST':
        record = Record.objects.get(id=id)
        record.berilgan_sana = request.POST['b_s']
        record.qaytardi = request.POST.get('qaytardi', False) == 'on'
        record.save()
        return redirect('/record/')
    context = {
        'record': Record.objects.get(id=id)
    }
    return render(request, 'record_tahrirlash.html', context)


def talabalar(request):
    if request.method == 'POST':
        data = TalabaForm(request.POST)
        if data.is_valid():
            Talaba.objects.create(
                ism=data.cleaned_data['ism'],
                kurs=data.cleaned_data['kurs'],
                kitob_nomi=data.cleaned_data['kitob_nomi']
            )
        return redirect('/talabalar/')
    context = {
        'talabalar': Talaba.objects.all(),
        'form': TalabaForm()
    }
    return render(request, 'hamma_student.html', context)

# Vazifa 2.Qoshish.
# 1-misol
def mualliflarr(request):
    if request.method == 'POST':
        data = MuallifForm(request.POST)
        if data.is_valid():
            Muallif.objects.create(
                ism=data.cleaned_data['ism'],
                jins=data.cleaned_data['jins'],
                tugilgan_sana=data.cleaned_data['tugilgan_sana'],
                kitoblar_soni=data.cleaned_data['kitoblar_soni'],
                tirik=data.cleaned_data['tirik']

            )
        return redirect('/mualliflar/')
    context = {
        'writers': Muallif.objects.all(),
        'form': MuallifForm()
    }
    return render(request, 'muallif.html', context)

#2-misol
def recordlar1(request):
    if request.method == 'POST':
        data = RecordForm(request.POST)
        if data.is_valid():
            data.save()
        return redirect('/recordlar1/')
    context = {
        'records': Record.objects.all(),
        'form': RecordForm()
    }
    return render(request, 'recordlar1.html', context)


# 3-misol
def kutubhonachilar(request):
    if request.method == 'POST':
        data = KutubhonachiForm(request.POST)
        if data.is_valid():
            Kutubhonachi.objects.create(
                ism=data.cleaned_data['ism'],
                ish_vaqti=data.cleaned_data['ish_vaqti'],
            )
        return redirect('/kutubhonachilar/')
    context = {
        'lib': Kutubhonachi.objects.all(),
        'form': KutubhonachiForm()
    }
    return render(request, 'all_lib.html', context)
