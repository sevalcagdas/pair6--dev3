class öğrenci:
    def __init__(self,ad,soyad,no):
        self.ad = ad
        self.soyad = soyad
        self.no = no
    
    def öğrenci_bilgileri(self):
        return f"Öğrenci Adı: {self.ad} Soyadı: {self.soyad} Öğrenci No: {self.no}"
    

    def öğrenci_ekle(self, öğrenci_listesi):
        öğrenci_listesi.append(self)
        print(f"{self.ad} {self.soyad} öğrenci listesine eklendi...")
       
