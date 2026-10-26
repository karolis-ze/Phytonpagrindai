def sutalpinti_lankytojai(lankytojai, biudzetas):
    sutalpinti = []
    bendra_suma = 0

    for lankytojas in pagal_amziu(lankytojai):
        kaina = kaina_is_lankytojo(lankytojas)
        if bendra_suma + kaina <= biudzetas:
            sutalpinti.append(lankytojas)
            bendra_suma += kaina
        else:
            break

    return sutalpinti, bendra_suma
print("Biudžetas:         20 EUR")
sutalpinti, bendra_suma = sutalpinti_lankytojai(lankytojai, 20)
print("Telpa lankytojai:  ", sutalpinti)
print("Bendra suma:       ", f"{bendra_suma:.2f} EUR ({len(sutalpinti)} bilietai)")