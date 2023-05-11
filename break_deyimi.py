kullanici_adi = ".ibrahim_iskender"
parola = "Ibrahim2003"

while True:
    
    soru1 = input("Kullanici adini giriniz: ")
    soru2 = input("Parolayi giriniz: ")
    
    if soru1 == kullanici_adi and soru2 == parola:
        print("Kullanaici adi ve parola onaylandi")
        break 
    
    else:
        print("Kullani adiniz veya parolaniz yanlis!")
        print("Lutfen tekrar deneyiniz!")
    
    