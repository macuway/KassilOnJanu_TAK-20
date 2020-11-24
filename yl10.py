name = input("Sisesta oma nimi: ")
print("Ahoj, " + name + "!")
town = input("Kus on te elukoht?: ")
if town == "Kuressaare":
    print("Tunnen sygavalt kaasa :(")
age = int(input("Teie vanus: "))
if age < 18:
    print("Oled veidike noor, et autot juhtida!")
elif age > 18:
    print("Oled piisavalt vana, et juhtida autot!")
else:
    print("8nne t2iskasvanuks saamisel!")
