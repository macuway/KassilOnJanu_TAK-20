puuviljad = ["Õun",  "Viinamari", "Pirn"]
print(puuviljad)
print(puuviljad[0])
puuviljad.append("Sidrun")
print(puuviljad[3])
puuviljad[1] = "Kiivi"
print(puuviljad)
if "Õun" in puuviljad:
    print("Õun on listis")
else:
    print("Õun ei ole listis")
print(len(puuviljad))
puuviljad.remove("Õun")
print(puuviljad)
puuviljad.reverse()
print(puuviljad)
puuviljad.sort()
print(puuviljad)