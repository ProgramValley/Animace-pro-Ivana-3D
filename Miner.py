import pyautogui
import time
import random
import OCR

print("Discord Miner hack v 1.5")

default =(630,298,1450,850)
comd = ["m!m","M!mine","m!M","M!M"]
tiem = [3,5,4,6,2.6,3,5,4,6,2.6]
spam_err = False
kod = "r-s-/M"
hodina = 0
AFK = 0
a = 27
kop="m!mine"
oprav="m!repair"
prodej="m!sell all"
verify = "m!verify "

def mimne():
    pyautogui.typewrite(cmd)
    pyautogui.keyDown("enter")
    pyautogui.keyUp("enter")
    time.sleep(0.5)
def prodeej():
    pyautogui.typewrite(prodej)
    pyautogui.keyDown("enter")
    pyautogui.keyUp("enter")
    print("sold")
    time.sleep(2)
def oprava():
    pyautogui.typewrite(oprav)
    pyautogui.keyDown("enter")
    pyautogui.keyUp("enter")
    time.sleep(2)
def overeny(konec):
    pyautogui.typewrite(verify+" ")
    pyautogui.typewrite(str(konec))
    pyautogui.keyDown("enter")
    pyautogui.keyUp("enter")
    time.sleep(3)
def Human():
    pyautogui.typewrite("I am here")
    pyautogui.keyDown("enter")
    pyautogui.keyUp("enter")
    time.sleep(1)

kode=input("code >>>")
while kode !=kod:
    print("invalid code")
    kode = input("code >>>")
time.sleep(2)

while True:
    time.sleep(0.2)
    cmd = random.choice(comd)
    tims =random.choice(tiem)
    try:
        OCR.SHOT(default)
        OCR.ORC()
        AFK=1
    except:
        print("OCR-fail")
        AFK = AFK+1
        if AFK == 4:
            input("ERROR")
            k= input("reset code >>>")
            while k.lower() != "r-s-/E":
                k = input("reset code >>>")
                print("system reset")
                AFK = 0

    file = open("discord.txt")
    r = file.read()
    file.close()
    #time.sleep(tims)
    time.sleep(2.6)

    #security checkers
    if "m! verify" in r:
        print("verify")
        file = open("discord.txt","r")
        ctu = file.read()
        file.close()
        if "+"in ctu:
            lsit= ctu.split()
            plsuko = lsit.index("+")
            jdenicka= lsit[plsuko+1]
            if jdenicka == "@":
                jdenicka=0
            dvojka = lsit[plsuko-1]
            if dvojka== "@":
                dvojka=0
            try:
                vysledek = int(jdenicka) + int(dvojka)
                if vysledek >=100:
                    input("Fake verify")
                    k=input("reset code >>>")
                    while k.lower() != "r-s-/V":
                        k = input("reset code >>>")
                        print("system reset")

                overeny(vysledek)
            except:
                print("Verify canot be done - reason unknow charecter ")
                print("Please restart system")
                k = input("reset code >>>")
                while k.lower() != "r-s-/V":
                    k = input("reset code >>>")
                    print("system reset")
        else:
            input("verification ERROR")
            reset = input("reset code >>>")
            while reset != "r-s-/VR":
                reset = input("reset code >>>")
    if "auto typer"  in r:
        Human()
        input("WARNING THEY FOUND YOU")
        kode = input("code >>>")
        while kode != "r-s-/HK":
            kode = input("code >>>")
    if "Hynjan" in r.split():
        span = 0
        for i in r.split():
            if i in comd:
                span = span + 1
            if span == 3:
                print("Spam detected-starting spam test")
                time.sleep(5)
                try:
                    OCR.SHOT(default)
                    OCR.ORC()
                    AFK = 1
                except:
                    print("OCR-fail")
                    AFK = AFK + 1
                    if AFK == 4:
                        input("ERROR")
                        k = input("reset code >>>")
                        while k.lower() != "r-s-/E":
                            k = input("reset code >>>")
                            print("system reset")
                            AFK = 0
                file = open("discord.txt")
                r = file.read()
                for i in r.split():
                    if i in comd:
                        span = span + 1
                    if span == 2:
                        print("Spam found for security reasons service blocked for 5 min")
                        time.sleep(400)
    if "@Hynjan" in r.split():
        if "spam" and "stop" in r.split() or spam_err is True:
            print("spam warning detected-priority 10")
            time.sleep(150)
        if  "spamming" in r.split():
            print("spam warning detected-priority 5")
            time.sleep(40)
    if "m!repair" in r or "m! repair" in r:
        prodeej()
        time.sleep(3)
        oprava()
        print("repaired")
    # if "Swissmas" or "Swisser" in r.split():
    # print("Moderator-Warning")
    # time.sleep(130)


    mimne()