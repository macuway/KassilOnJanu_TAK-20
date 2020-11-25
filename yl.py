stuff = list(input("Sisesta suvalised sümbolid: "))
stuff = [x.strip() for x in stuff]
middle = float(len(stuff))/2
if len(stuff) > 6 and len(stuff) % 2 != 0:
    print(stuff[int(middle-1.5)] + stuff[int(middle-0.5)] + stuff[int(middle+0.5)])
else:
    print("Sümboleid peab olema vähemalt 7 ja paaritu arv!")