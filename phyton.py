# class Penguen():
#     sinif = "Quş"
    
#     def __init__(self, ad = None ,yas = None, reng = None):
#         self.ad = ad
#         self.yas = yas
#         self.reng = reng
#         # print(self)
        
#     def uze_bilme(self):
#         return f"{self.ad} uze bilir"
    
#     def reqs_ede_bilme(self, reqs_ede_bilme = False):
#         if reqs_ede_bilme:
#             return f"{self.ad} reqs ede bilir"
#         else:
#             return f"{self.ad} reqs ede bilmir"
                                
        
# kralPinqivin = Penguan()
# sariPinqivin = Penguan("Sari Pinqivin", 3, "Sari")

# print(f"{sariPinqivin.ad}-nin {sariPinqivin.yas} yasi var")
# print(sariPinqivin.uze_bilme())
# print(sariPinqivin.reqs_ede_bilme(True))



# -------------------------------------------------------

# Inheritance
"""
Miras almaq menasina gelir. Parent bir classin butun ozelliklerini child classda cagira, istifade ede bilerik.
Bir classin butun ozelliklerini diger bir classda istifade etmek ucundur.

"""
# class Qus():
#     def __init__(self):
#         print("Qus yaradildi")
        
#     def menKimem(self):
#         print("Bu qusdur")
        
#     def ucma(self):
#         print("Quslar uca bilir")
        
#     def uzme(self):
#         print("Quslar uze bilmir")
        
        
# qus = Qus()
# qus.menKimem()
# qus.uzme()
        
        
# class Bayqus(Qus):
#     def __init__(self):
#         super().__init__()
#         print("Bayqus yaradildi")
        
#     # Override method    
#     def menKimem(self):
#         print("Bu bayqusdur")
        
#     def gece_gorme(self):
#         print("Bayquslar gece gore bilir")
        
# bayqus = Bayqus()
# bayqus.uzme()
# bayqus.ucma()
# bayqus.menKimem() # Override >> uzerine cixmaq
# bayqus.gece_gorme()
    
# ------------------------------------------------
# Encupsulation
"""
Gizleme ya da oz elimizde saxlamaq ucun istifade olunur.
Bir classin bir deyerini (methodunu) yalniz oz daxilinde deyise ve istifade ede bilerik.

Hansi deyeri gizletmek isteyirikse onune "__" iki alt xett ile qeyd edirik.
"""

# class Telefon():
#     def __init__(self):
#        self.__qiymet = 1000
#        print("Telefon yaradildi")
       
#     def set_qiymet(self, yeniQiymet):
#         if yeniQiymet >= 0:
#             self.__qiymet = yeniQiymet
#         else:
#             print("Telefonun qiymeti menfi ola bilmez")
        
#     def get_qiymet(self):
#         return self.__qiymet
       
# tel = Telefon()
# tel.__qiymet = 200
# tel.reng = "Qara"
# print(f"Telefonun qiymeti {tel.__qiymet}, rengi ise {tel.reng} dir")

# print(f"Telefonun onceki qiymeti: {tel.get_qiymet()}")
# tel.set_qiymet(500)
# print(f"Telefonun sonraki qiymeti: {tel.get_qiymet()}")

# -------------------------------------------------
# Polymorphism

# class Qus():
#     def __init__(self):
#         print("Qus yaradildi")
        
#     def menKimem(self):
#         print("Bu qusdur")
        
#     def ucma(self):
#         print("Quslar uca bilir")
        
#     def uzme(self):
#         print("Quslar uze bilmir")
               
        
# class Bayqus(Qus):
#     def __init__(self):
#         super().__init__()
#         print("Bayqus yaradildi")
        
#     # Override method    
#     def menKimem(self):
#         print("Bu bayqusdur")
        
#     def gece_gorme(self):
#         print("Bayquslar gece gore bilir")
        
        
# class Penguen(Qus):
#     def __init__(self):
#         super().__init__()
#         print("Pinqivin yaradildi")
        
#     # Override method    
#     def menKimem(self):
#         print("Bu pinqivin")
        
#     def uzme(self):
#         print("Pinqivinler uze bilir")
        
#     def ucma(self):
#         print("Pinqivinler uca bilmir")
        
        
    
# qus = Qus()
# bayqus = Bayqus()
# pinqivin = Penguen()


# def test_uca_bilme(test_olunmus_qus):
#     test_olunmus_qus.ucma()
    
# test_uca_bilme(qus)
# test_uca_bilme(bayqus)
# test_uca_bilme(pinqivin)




# ------------------------------------------------------------------------------------

# ............NEW TASK............


# sahmat ile bagli olaraq inheritance  istifade ederek bir numune yaratmaq

# class chess():
#     def __init__(self):
#         print("Sahmat taxtasi yaradildi")
        
#     def white(self, white = True):
#         if white:
#             return f"{self.white} agdir"
#         else:
#             return f"{self.white} qaradir"
        
 
              
#     def purpose(self):
#         print("Meqsed Reqibi mat etmekdir")
#         print("Zamana nezaret ed")
        
        
# chess = chess()
# chess.white()
# chess.purpose()
        
        
# class king(chess):
#     def __init__(self):
#         super().__init__()
  
#     def vezife(self):
#         print("Sahi qarsi teref alsa mat olunur")
        
#     def gedisi(self):
#         print("Her cur gedisi var")
        
# king = king()
# king.vezife()
# king.gedisi()
# king.white() 
# king.purpose()




# polymorphism istifade ederek bir sahmatla bagli numune


# class chess():
#     def __init__(self):
#         print("Sahmat taxtasi yaradildi")

#     def purpose(self):
#         print("Meqsed Reqibi mat etmekdir")
#         print("Zamana nezaret ed")
        
               
        
# class king(chess):
#     def __init__(self):
#         super().__init__()
#         print("Sah fiquru yaradildi")
        
#     def fiqur(self):
#         print("Bu sahdir")
        
#     def gedisi(self):
#         print("Her cur irelileye bilir")
        
        
# class pawn(chess):
#     def __init__(self):
#         super().__init__()
#         print("Piyada fiquru yaradildi")
        
#     def fiqur(self):
#         print("Bu piyadadir")
        
#     def gedisi(self):
#         print("Saga,sola,asagi,yuxari duz irelileyir")
        
        
        
    
# Chess = chess()
# King = king()
# Pawn = pawn()


# def test(test_olunmus_fiqur):
#     test_olunmus_fiqur.purpose()
    
# test(chess)
# test(king)
# test(pawn)




# # Encupsulation

# class masin:
#     def __init__(self, marka, model, reng):
#         self.marka = marka
#         self.model = model
#         self.renk = reng
#         self.__suret = 0  


#     def sureti(self, suret):
#         if suret < 0:
#             print("menfi olmaz!")
#         else:
#             self.__suret = suret
#             print("sureti var:",suret)

#     def sureti_artir(self, artis):
#         self.__suret += artis
#         print("suret artirildi:", self.__suret)

#     def sureti_azalt(self, azalis):
#         self.__hiz -= azalis
#         print("suret azaltıldı.", self.__suret)

# car = masin()
# car.__suret = 100
# print(f"Masinin sureti {car.__suret} dir")

# print(f"Masinin artmis sureti: {car.sureti_artir()}")
# car.sureti_azalt_(50)
# print(f"Masinin azalmis sureti: {car.sureti_azalt()}")









