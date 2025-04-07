print("\033[44mJe wordt wakker in een donker bos...\033[0m")
keuze = input("\033[43mGa je naar het (1) pad of (2) grot?\033[0m")

if keuze == "1":
    print("\033[44mJe volgt het pad en vindt een verlaten hut.\033[0m")
    keuze_pad = input("\033[43mna het betreden van de hut vind je een (1) deur naar de kelder en een (2) mysterieuze soep die erg lekker ruikt.\033[0m")
    if keuze_pad == "1":
        print("\033[43m...\033[0m")
    elif keuze_pad == "2":
        print("\033[43mje neemt een slokje van de soep, en je ontploft.\033[0m")
elif keuze == "2":
    print("\033[44mJe loopt de grot in... en hoort iets grommen.\033[0m")
else:
    print("\033[44mJe blijft stil staan. Iets komt dichterbij...\033[0m")