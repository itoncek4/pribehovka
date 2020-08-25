import random
print("vítám tě ve hře šibenice classic")
def uvod(nic):
    print("Ahoj, zvol si prosím téma na které chceš mít šibenici")
    print("TÉMATA: hudba, příroda, sport, svět, věda")
    volba = input(str("volím si téma "))  
    return vyber_tematu(volba)

#uživatel si zvolí téma

def vyber_tematu(volba):
        if volba in "hudba":
            dokument = 1
        elif volba in "příroda":
            dokument = 2
        elif volba in "sport":
            dokument = 3
        elif volba in "svět":
            dokument = 4
        elif volba in "věda":
            dokument = 5
        else:
            dokument = 0
        return dokument
    
#zhodnotí a očisluje volbu tématu

def hudba(nic):
    nahodne_cislo = random.randint(0,9)
    seznam_dokumentace = []
    with open ("databaze_hudba.txt", encoding = "utf-8") as soubor:
        for i in soubor:
            seznam_dokumentace.append(i)
        slovo = seznam_dokumentace[nahodne_cislo]
        seznam_slovo = []
        for i in slovo:
            seznam_slovo.append(i)
        del(seznam_slovo[-1])
        return seznam_slovo

#napojí se do databáze hudba, vybere jedno náhodný slovo a udělá z něj seznam

def priroda(nic):
    nahodne_cislo = random.randint(0,9)
    seznam_dokumentace = []
    with open ("databaze_priroda.txt", encoding = "utf-8") as soubor:
        for i in soubor:
            seznam_dokumentace.append(i)
        slovo = seznam_dokumentace[nahodne_cislo]
        seznam_slovo = []
        for i in slovo:
            seznam_slovo.append(i)
        del(seznam_slovo[-1])
        return seznam_slovo

#-"- příroda -"-

def sport(nic):
    nahodne_cislo = random.randint(0,9)
    seznam_dokumentace = []
    with open ("databaze_sport.txt", encoding = "utf-8") as soubor:
        for i in soubor:
            seznam_dokumentace.append(i)
        slovo = seznam_dokumentace[nahodne_cislo]
        seznam_slovo = []
        for i in slovo:
            seznam_slovo.append(i)
        del(seznam_slovo[-1])
        return seznam_slovo

#-"- sport -"-
        
def svet(nic):
    nahodne_cislo = random.randint(0,9)
    seznam_dokumentace = []
    with open ("databaze_svet.txt", encoding = "utf-8") as soubor:
        for i in soubor:
            seznam_dokumentace.append(i)
        slovo = seznam_dokumentace[nahodne_cislo]
        seznam_slovo = []
        for i in slovo:
            seznam_slovo.append(i)
        del(seznam_slovo[-1])
        return seznam_slovo

#-"- svět -"-
        
def veda():
    nahodne_cislo = random.randint(0,9)
    seznam_dokumentace = []
    with open ("databaze_veda.txt", encoding = "utf-8") as soubor:
        for i in soubor:
            seznam_dokumentace.append(i)
        slovo = seznam_dokumentace[nahodne_cislo]
        seznam_slovo = []
        for i in slovo:
            seznam_slovo.append(i)
        del(seznam_slovo[-1])
        return seznam_slovo

#-"- věda -"-

def pismeno(nic):
    pismeno = input(str("Písmeno "))
    if pismeno in seznam_slovo:
        for i in range(len(seznam_slovo)):
            if pismeno in seznam_slovo[i]:
                seznam_vypis[i] = pismeno
        print("Správně!")
        chyba = 0
    else:
        chyba = 1
        print("Toto písmeno tam není")
    seznam_ne.append(pismeno)
    print(seznam_vypis)
    print("Použitá písmena: ", seznam_ne)
    return chyba
while True:   
    a = 0
    while a == 0:
        volba = uvod("")
        if volba != 0:
            print("Dobře")
            a = 1
        else:
            print("Neplatná volba!")
    if volba == 1:
        seznam_ne = []
        seznam_slovo = hudba("")
        seznam_vypis = []
        for i in range(len(seznam_slovo)):
            if seznam_slovo != "-":
                seznam_vypis.append("_")
            else:
                seznam_vypis.append("-")
        print(seznam_vypis)
        chyba = 0
        while chyba < 7 and seznam_vypis != seznam_slovo:
            chyba =chyba + pismeno("")
            print("Počet chyb: ", chyba)
            if chyba == 7:
                print("")
                print("POVĚSILI TĚ!:(, PRO POKRAČOVÁNÍ ZMÁČKNI ENTER")
                print("")
                input()
            if seznam_vypis == seznam_slovo:
                print("")
                print("VÝBORNĚ, VYHRÁL JSI!:D, PRO POKRAČOVÁNÍ ZMÁČKNI ENTER")
                print("")
                input()
    elif volba == 2:
        seznam_ne = []
        seznam_slovo = priroda("")
        seznam_vypis = []
        for i in range(len(seznam_slovo)):
            if seznam_slovo != "-":
                seznam_vypis.append("_")
            else:
                seznam_vypis.append("-")
        print(seznam_vypis)
        chyba = 0
        while chyba < 7 and seznam_vypis != seznam_slovo:
            chyba =chyba + pismeno("")
            print("Počet chyb: ", chyba)
            if chyba == 7:
                print("")
                print("POVĚSILI TĚ!:(, PRO POKRAČOVÁNÍ ZMÁČKNI ENTER")
                print("")
                input()
            if seznam_vypis == seznam_slovo:
                print("")
                print("VÝBORNĚ, VYHRÁL JSI!:D, PRO POKRAČOVÁNÍ ZMÁČKNI ENTER")
                print("")
                input()
    elif volba == 3:
        seznam_ne = []
        seznam_slovo = sport("")
        seznam_vypis = []
        for i in range(len(seznam_slovo)):
            if seznam_slovo != "-":
                seznam_vypis.append("_")
            else:
                seznam_vypis.append("-")
        print(seznam_vypis)
        chyba = 0
        while chyba < 7 and seznam_vypis != seznam_slovo:
            chyba =chyba + pismeno("")
            print("Počet chyb: ", chyba)
            if chyba == 7:
                print("")
                print("POVĚSILI TĚ!:(, PRO POKRAČOVÁNÍ ZMÁČKNI ENTER")
                print("")
                input()
            if seznam_vypis == seznam_slovo:
                print("")
                print("VÝBORNĚ, VYHRÁL JSI!:D, PRO POKRAČOVÁNÍ ZMÁČKNI ENTER")
                print("")
                input()
    elif volba == 4:
        seznam_ne = []
        seznam_slovo = svet("")
        seznam_vypis = []
        for i in range(len(seznam_slovo)):
            if seznam_slovo != "-":
                seznam_vypis.append("_")
            else:
                seznam_vypis.append("-")
        print(seznam_vypis)
        chyba = 0
        while chyba < 7 and seznam_vypis != seznam_slovo:
            chyba =chyba + pismeno("")
            print("Počet chyb: ", chyba)
            if chyba == 7:
                print("")
                print("POVĚSILI TĚ!:(, PRO POKRAČOVÁNÍ ZMÁČKNI ENTER")
                print("")
                input()
            if seznam_vypis == seznam_slovo:
                print("")
                print("VÝBORNĚ, VYHRÁL JSI!:D, PRO POKRAČOVÁNÍ ZMÁČKNI ENTER")
                print("")
                input()
    elif volba == 5:
        seznam_ne = []
        seznam_slovo = veda("")
        seznam_vypis = []
        for i in range(len(seznam_slovo)):
            if seznam_slovo != "-":
                seznam_vypis.append("_")
            else:
                seznam_vypis.append("-")
        print(seznam_vypis)
        chyba = 0
        while chyba < 7 and seznam_vypis != seznam_slovo:
            chyba =chyba + pismeno("")
            print("Počet chyb: ", chyba)
            if chyba == 7:
                print("")
                print("POVĚSILI TĚ!:(, PRO POKRAČOVÁNÍ ZMÁČKNI ENTER")
                print("")
                input()
            if seznam_vypis == seznam_slovo:
                print("")
                print("VÝBORNĚ, VYHRÁL JSI!:D, PRO POKRAČOVÁNÍ ZMÁČKNI ENTER")
                print("")
                input()
