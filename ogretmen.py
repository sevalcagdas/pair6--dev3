class öğretmen: 
    def __init__(self,ad,soyad,brans):
        self.ad = ad
        self.soyad = soyad
        self.brans = brans
    
    def öğretmen_bilgileri(self):
        return f"Öğretmen Adı: {self.ad} Soyadı: {self.soyad} brans {self.brans}"
    

    def öğretmen_ekle(self, öğretmen_listesi):
        öğretmen_listesi.append(self)
        print(f"{self.ad} {self.soyad} {self.brans} öğretmen listesine eklendi...")