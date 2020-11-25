string = input("Sisesta string: ")
stripstring = string.strip()
sslenght = len(stripstring)
if sslenght < 7 or (sslenght % 2) == 0:
    print("String peab olema vähemalt 7 sümbolit ja peab olema paaritu arv sümboleid")
pos = sslenght / 2 + 0.5
rpos = round(pos)
pos1 = (rpos - 1)
pos3 = (rpos + 1)
print(string[pos1 - 1] + string[rpos - 1] + string[pos3 - 1])