from django.contrib import admin
from .models import *

class TalabaAdmin(admin.ModelAdmin):
    list_display = ["id","ism","kurs","kitob_nomi"]
    list_display_links = ["id","ism"]
    list_editable = ["kurs","kitob_nomi"]
    list_filter = ["kurs"]
    search_fields = ["id"]
    search_help_text = "id boyicha qidiring"
    list_per_page = 5



class KitobAdmin(admin.ModelAdmin):
    list_display = ["id","nom","janr","sahifa","muallif"]
    list_display_links = ["id","nom"]
    list_editable = ["janr","sahifa"]
    list_filter = ["janr","muallif"]
    search_fields = ["id","nom"]
    search_help_text = "id,nom boyicha qidiring"
    autocomplete_fields = ["muallif"]
    list_per_page = 5

#Vazifa
#1-misol
class KutubhonachiAdmin(admin.ModelAdmin):
    list_display = ["id","ism","ish_vaqti"]
    list_display_links = ["id","ism"]
    list_filter = ["ish_vaqti"]
    search_fields = ["id","ism"]
    search_help_text = "id yoki ism boyicha qidiring"
#2-misol
class MuallifAdmin(admin.ModelAdmin):
    list_display = ["id","ism","jins","tugilgan_sana","kitoblar_soni","tirik"]
    list_display_links = ["id","ism"]
    list_editable = ["kitoblar_soni","tirik"]
    list_filter = ["tirik"]
    search_fields = ["id","ism","tugilgan_sana"]
    search_help_text = "id,ism,tugilgan sana boyicha qidiring"
    date_hierarchy = "tugilgan_sana"
    list_per_page = 5
#3-misol
class RecordAdmin(admin.ModelAdmin):
    list_display = ["talaba","kitob","kutubhonachi","olingan_sana","qaytardi","berilgan_sana"]
    autocomplete_fields = ["talaba","kitob","kutubhonachi"]
    list_per_page = 5
#4-misol

admin.site.register(Talaba,TalabaAdmin)
admin.site.register(Kitob,KitobAdmin)
admin.site.register(Muallif,MuallifAdmin)
admin.site.register(Kutubhonachi,KutubhonachiAdmin)
admin.site.register(Record,RecordAdmin)


