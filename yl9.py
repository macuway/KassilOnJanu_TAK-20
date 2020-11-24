k1 = int(input("esimene kylg: "))
k2 = int(input("teine kylg: "))
k3 = int(input("kolmas kylg: "))
if k1 + k2 < k3:
    print("V8imatu")
elif k1 + k3 < k2:
    print("V8imatu")
elif k2 + k3 < k1:
    print("V8imatu")
elif k1 == k2 == k3:
    print("V8rdkylgne kolmnurk")
elif k1 == k3:
    print("V8rdhaarne kolnurk")
elif k2 == k3:
    print("V8rdhaarne kolmnurk")
elif k1 == k2:
    print("V8rdhaarne kolmnurk")
elif k1 != k2 != k3:
    print("Erikylgne kolmnurk")
