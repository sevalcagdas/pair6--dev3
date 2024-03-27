from ogrenci import öğrenci
from ogretmen import öğretmen


öğrenci_listesi= [] 
öğretmen_listesi= []




öğrenci1 = öğrenci("Ali","Yalcın","314")
öğrenci1.öğrenci_ekle(öğrenci_listesi)
öğrenci2 = öğrenci("Mehmet","Yılmaz","215")
öğrenci2.öğrenci_ekle(öğrenci_listesi)


öğretmen1= öğretmen("İrem","Balcı","Tarih")
öğretmen1.öğretmen_ekle(öğretmen_listesi)
öğretmen2= öğretmen("Kaan","Bal","Matematik")
öğretmen2.öğretmen_ekle(öğretmen_listesi)

def tum_öğrenciler(öğrenci_listesi):
    for öğrenci in öğrenci_listesi:
        print(öğrenci.öğrenci_bilgileri())

def tum_öğretmenleri(öğretmen_listesi):
    for öğretmen in öğretmen_listesi:
        print(öğretmen.öğretmen_bilgileri())

print("Tüm Öğrenciler:")
tum_öğrenciler(öğrenci_listesi)

print("Tüm Öğretmenler:")
tum_öğretmenleri(öğretmen_listesi)




