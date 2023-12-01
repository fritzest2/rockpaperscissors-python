#kivipaberkäärid.py
from random import *

while True:
    print(f"\n-------------------------------------------------------\nTere! Oled jõudnud mängu nimega kivi, paber või käärid!") # optimaalseks kuvamiseks f-string

    kasutaja_valik = input("Kivi, paber või käärid? ")

    juhuslik_arv = randint(1, 3) # kuna valikuid on 3, siis randint on 1,3 vahel

    if juhuslik_arv == 1:
        arvuti_valik = "kivi"
    
    elif juhuslik_arv == 2:
        arvuti_valik = "paber"
    
    else:
        arvuti_valik = "käärid"
    
    print("")
    print("Mängja valik: " + kasutaja_valik)
    print("Arvuti valik: " + arvuti_valik)
    
    if arvuti_valik == "kivi" and kasutaja_valik == "paber":
        print("")
        print("Mängija võitis!")
    
    elif arvuti_valik == "paber" and kasutaja_valik == "käärid":
        print("")
        print("Mängija võitis!")
    
    elif arvuti_valik == "käärid" and kasutaja_valik == "kivi":
        print("")
        print("Mängija võitis!")

    elif arvuti_valik == "kivi" and kasutaja_valik == "käärid":
        print("")
        print("Mängija kaotas!")
    
    elif arvuti_valik == "paber" and kasutaja_valik == "kivi":
        print("")
        print("Mängija kaotas!")

    elif arvuti_valik == "käärid" and kasutaja_valik == "paber":
        print("")
        print("Mängija kaotas!")
    
    else:
        print("")
        print("Sa jäid arvutiga viiki!")
    
    uus_mang = input("Kas soovid uuesti mängida? (Jah/Ei) ")
    if uus_mang.lower() != "jah": # küsib, kas mängija soovib uuesti mängida ja kui vastus ei ole "jah", siis lõpetab programm töö. Sama hästi võiks teha [if uus_mang.lower() == "ei" .. break], aga väga vahet pole.  
        break