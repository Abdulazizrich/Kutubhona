from django.contrib import admin
from django.urls import path
from asosiy.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('jadval/',hamma_kitoblar),
    path('royhat/', hamma_mualliflar),
    path('talaba/',bitiruvchi_talaba),
    path('bitta_talaba/<int:aw>/',bitta_talaba),
    path('a_talaba/',a_talaba),
    path('tanlangan/<str:fr>/',tanlangan),
    path('tankitob/<int:rt>/',tan_kitob),
    path('record/', hamma_recordlar),
    path('tirik/',tirik_muallif),
    path('kitoblar/',sahifa_book),
    path('mualliflar/',mehnatkash),
    path('mualliflar/',mehnatkash),
    path('student/',hamma_talaba),
    path('asd/<int:pk>/',talaba_ochir),
    path('delete/<int:pk>/',kitob_ochir),

]
