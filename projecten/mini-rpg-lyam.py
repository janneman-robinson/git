print("\033[32m██╗░░░░░██╗░░░██╗░█████╗░███╗░░░███╗██╗░██████╗░░░░░░███╗░░░███╗██╗███╗░░██╗██╗░░░░░░██████╗░██████╗░░██████╗░\033[0m")
print("\033[32m██║░░░░░╚██╗░██╔╝██╔══██╗████╗░████║╚█║██╔════╝░░░░░░████╗░████║██║████╗░██║██║░░░░░░██╔══██╗██╔══██╗██╔════╝░\033[0m")
print("\033[32m██║░░░░░░╚████╔╝░███████║██╔████╔██║░╚╝╚█████╗░█████╗██╔████╔██║██║██╔██╗██║██║█████╗██████╔╝██████╔╝██║░░██╗░\033[0m")
print("\033[32m██║░░░░░░░╚██╔╝░░██╔══██║██║╚██╔╝██║░░░░╚═══██╗╚════╝██║╚██╔╝██║██║██║╚████║██║╚════╝██╔══██╗██╔═══╝░██║░░╚██╗\033[0m")
print("\033[32m███████╗░░░██║░░░██║░░██║██║░╚═╝░██║░░░██████╔╝░░░░░░██║░╚═╝░██║██║██║░╚███║██║░░░░░░██║░░██║██║░░░░░╚██████╔╝\033[0m")
print("\033[32m╚══════╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░░░░╚═╝░░░╚═════╝░░░░░░░╚═╝░░░░░╚═╝╚═╝╚═╝░░╚══╝╚═╝░░░░░░╚═╝░░╚═╝╚═╝░░░░░░╚═════╝░\033[0m")

print("\033[32mWelkom bij de Mini RPG!\033[0m")
print("\033[32mBij een keuze typ je 1, 2, 3, etc. om je keuze te maken.\033[0m")
print("\033[32mJe kan een keuze ook overslaan door op ENTER te drukken.\033[0m")
print("\033[32mVeel succes!\033[0m")

import time
time.sleep(5)

print("\033[33mJe wordt wakker in een donker bos... voor je vind je een duister pad, en achter je een grot met een paar touwen.\033[0m")
keuze = input("\033[43mBetreed het (1) duistere pad of (2) grot?\033[0m")

if keuze == "1":
    print("\033[33mJe volgt het pad en vindt een verlaten houten hut.\033[0m")
    keuze_pad = input("\033[43mna het betreden van de hut vind je een (1) luikje naar de kelder en een (2) mysterieuze soep die verrassend lekker ruikt.\033[0m")

    if keuze_pad == "1":
        print("\033[33mHet luik kraakt terwijl je hem opent, er komt een groene gloed uit de opening, in de kelder staat een heks, ze heeft 2 pillen in haar hand.\033[0m")
        keuze_luik = input("\033[43mNeem de (1) rode pil, of neem de (2) blauwe pil.\033[0m")

        if keuze_luik == "1":
            print("\033[33mJe neemt de rode pil, na enkele seconden zie je de waarheid van het universum, en dat de wereld bestaat uit binaire code. je bent gestegen boven het menselijk bestaan.\033[0m")
            time.sleep(2)
            print("\033[31mEinde 1: Waarheid van het universum\033[0m")
        elif keuze_luik == "2":
            print("\033[33mJe neemt de blauwe pil, er lijkt eerst niks te gebeuren, maar voordat je iets kunt zeggen wordt je wat licht in je hoofd... je wordt wakker in een donker bos...\033[0m")
            time.sleep(2)
            print("\033[31mEinde 2: Loop\033[0m")
        else:
            print("\033[33mde keuze duurde te lang, de heks keek je boos aan en propte uit woede beide pillen in je mond, de heks lachte terwijl je zelf ook langzaam in een heks veranderde\033[0m")
            time.sleep(2)
            print("\033[31mEinde 3: Heks \033[0m")
    elif keuze_pad == "2":
        print("\033[33mje neemt een slokje van de soep, en voordat ook maar iets kan doen smelt je tot een plasje slijm.\033[0m")
        time.sleep(2)
        print("\033[31mEinde 4: Snert\033[0m")
    else:
        print("\033[33mTerwijl je twijfelt over je keuze stapt er een heks uit het luikje en gooit en fles zuur over je heen.\033[0m")
        time.sleep(2)
        print("\033[31mEinde 5: Dat is zuur\033[0m")
elif keuze == "2":
    print("\033[33mJe loopt de grot in... je komt aan in een holle ruimte, in de kamer bevind zich een paars- gloeiend ei, en een grote zak goud\033[0m")
    keuze_grot = input("\033[43mOnderzoek het (1) ei, of bekijk de (2) grote zak met goud.\033[0m")
    if keuze_grot == "1":
        print("\033[33mJe raakt het ei zachtjes aan, opeens begint deze erg snel te draaien en veller te gloeien, door alle plots beweging knalt hij tegen een muur en breekt hij in wel 100 stukjes\033[0m")
        print("\033[33mer springt er een gillende alien uit, voordat je ook maar een gedachte kan krijgen over deze vreemde situatie, schiet de alien je dood met een lazer pistool.\033[0m")
        time.sleep(2)
        print("\033[31mEinde 6: gillende alien\033[0m")
    elif keuze_grot == "2":
        print("\033[33mje loopt naar de zak met goud, er is niemand die de zak bewaakt, je kan hem meenemen, of natuurlijk laten staan.\033[0m")
        keuze_zak = input("\033[43m(1) neem de zak mee, of (2) laat hem staan.")
        if keuze_zak == "1":
            print("\033[33m'Net als je de zak op wil pakken springt er een goblin tussen het goud vandaan.\033[0m")
            print("\033[33m'Mijn naam is kevin de goblin, en dit goud is van mij! je mag de zak best hebben, maar alleen als je wat vragen juist weet te beantwoorden!'\033[0m")
            print("\033[33m'Vraag 1: wie schilderde de Mona Lisa?\033[0m")
            keuze_vraag_1 = input("\033[43m(1) leonardo dicaprio, (2) leonardo da vinci, of was het (3) leonardo vibonacci?\033[0m")
            if keuze_vraag_1 == "1":
                print("\033[33m'DAT IS FOUT MUAHAHAHH, DEZE ZAK GOUD BLIJFT LEKKER VAN MIJ\033[0m")
                time.sleep(2)
                print("\033[31mEinde 7: Fout andwoord :(\033[0m")
            elif keuze_vraag_1 == "2":
                print()



else:
    print("\033[33mJe blijft net iets te lang stil staan. Iets komt dichterbij...\033[0m")
    print("\033[33mEr verschijnt een bigfoot voor je! wat ga je doen?\033[0m")
    keuze_bigfoot = input("\033[43mje (1) Slaat bigfoot op zijn hoofd met een stok, of kan je toch beter (2) wegrennen...\033[0m")

    if keuze_bigfoot == "1":
        print("\033[33mJe voelt (zonder oogcontact te verliezen) over de grond op zoek naar een stok, je vind een dikke tak en breekt hem op bigfoots hoofd, uit woede trekt hij je armen er af :(\033[0m")

        time.sleep(2)
        print("\033[31mEinde 6: Lunch van bigfoot\033[0m")

    elif keuze_bigfoot == "2":
        print("\033[33mJe rend to hard als je kan weg, en bigfoot rend schreeuwend achter je aan, je komt uit op een verharde weg, voor je het weet lig je op de motorkap van een carglass busje\033[0m")
        time.sleep(2)
        print("\033[31mEinde 7: carglass repareert, carglass vervangt\033[0m")