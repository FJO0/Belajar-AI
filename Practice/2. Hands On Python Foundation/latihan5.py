def calculator(simbol, *angka):

    if len(angka) <2 :
        return "Masukkan minimal 2 angka"
    if simbol == "+":
        return sum(angka)
    elif simbol == "-":
        start = angka[0]
        for x in angka[1:] : 
            start -=x
        return start
    elif simbol =="*":
        start = angka[0]
        for x in angka[1:]:
            start *=x
        return start
    elif simbol == "/":
        start = angka[0]
        for x in angka[1:]:
            if x == 0:
                return "Tidak bisa dibagi dengan 0"
            start /=x
        return start 
    elif simbol == "%":
        start = angka[0]
        for x in angka[1:]:
            start %=x
        return start
    elif simbol == "**":
        start = angka[0]
        for x in angka[1:]:
            start **=x
        return start
    else : 
        return "error"  

a = calculator("+", 10, 5)

print(a)