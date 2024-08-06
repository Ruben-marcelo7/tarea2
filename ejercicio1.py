M1 = int(input("ingrese su primera nota: "))
M2 = int(input("ingrese su segunda nota: "))
M3 = int(input("ingrese su tercera nota: "))
M4 = int(input("ingrese su cuarta nota: "))

P = ( M1 + M2 + M3 + M4 ) / 4 

if P >=  90:
    print ("usted califico con A")
elif P >= 80:
    print ("usted califico con B")
elif P >= 70:
    print ("usted califico con C")
elif P >= 60:
    print ("usted califico con D")
    