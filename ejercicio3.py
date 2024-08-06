F1 = input ("ingrese la fecha con este formato DD, MM AAAA: ")
print (F1[4:8])
D = F1[0:2]
A = F1 [-4:]
F2 = F1[4:8] #son 5 letras
F3 = F1[4:9] #son 6 letras
F4 = F1[4:10] #son 7 letras
F5 = F1[4:12] #son 9 letras
F6 = F1[4:13] #son 10 letras
print (F6)
if F2 == "Mayo":
    print ( D , "/ 5 /", A)
#elif:
    