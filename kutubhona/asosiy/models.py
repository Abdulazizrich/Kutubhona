from django.db import models

# Create your models here.

TURLAR = [
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
]

class Talaba(models.Model):
    ism = models.CharField(max_length=30)
    kurs = models.CharField(max_length=30,choices=TURLAR)
    kitob_nomi = models.CharField(max_length=30)
    def __str__(self):
        return f"{self.ism}   {self.kurs}    {self.kitob_nomi}"
Jinslar = [
    ("Erkak", "Erkak"),
    ("Ayol", "Ayol"),
]
class Muallif(models.Model):
    ism = models.CharField(max_length=30)
    jins = models.CharField(max_length=30, choices=Jinslar)
    tugilgan_sana = models.DateTimeField(max_length=30)
    kitoblar_soni = models.BigIntegerField(max_length=30)
    tirik = models.BooleanField(max_length=30)

    def __str__(self):
        return f"{self.ism}   {self.tugilgan_sana}    {self.kitoblar_soni}"

class Kitob(models.Model):
    nom = models.CharField(max_length=30)
    janr = models.CharField(max_length=30)
    sahifa = models.BigIntegerField(max_length=30)
    muallif = models.ForeignKey(Muallif, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.nom}   {self.janr}    {self.muallif}"

class Kutubhonachi(models.Model):
    ism = models.CharField(max_length=30)
    ish_vaqti = models.CharField(max_length=30)
    def __str__(self):
        return f"{self.ism}   {self.ish_vaqti}"

class Record(models.Model):
    talaba = models.ForeignKey(Talaba, on_delete=models.CASCADE)
    kitob = models.ForeignKey(Kitob, on_delete=models.CASCADE)
    kutubhonachi = models.ForeignKey(Kutubhonachi, on_delete=models.CASCADE)
    olingan_sana = models.DateTimeField()
    qaytardi = models.BooleanField(default=False)
    berilgan_sana = models.DateTimeField()

    def __str__(self):
        return f"{self.talaba}   {self.kitob}    {self.kutubhonachi}"



