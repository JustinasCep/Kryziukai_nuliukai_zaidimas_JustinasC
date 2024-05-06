print('kryziukai nuliukai')
ejimas = 0
lentele = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]
zaidejas = True
def sukurti_lentele(lentele):
    for eilute in lentele:
        for stulpelis in eilute:
            print(stulpelis,  end="")
        print()

def koordinates(zaidejo_skaicius):
    eilute = int(zaidejo_skaicius/3)
    stulpelis = zaidejo_skaicius
    if stulpelis>2: stulpelis =int(stulpelis % 3)
    return (eilute, stulpelis)


def uzimta(kord, lentele):
    eilute = kord[0]
    stulpelis = kord[1]
    if lentele[eilute][stulpelis] != "-":
        print("Langelis uzimtas")
        return True
    else: return False



def ikelti_simboli (kord, lentele, aktyvus_zaidejas):
    eilute = kord[0]
    stulpelis = kord[1]
    lentele[eilute][stulpelis] = aktyvus_zaidejas

def tikrina_eilutes (zaidejas, lentele):
    if lentele[0][0] == lentele[0][1] == lentele[0][2] == zaidejas: return True
    elif lentele[1][0] == lentele[1][1] == lentele[1][2] == zaidejas: return True
    elif lentele[2][0] == lentele[2][1] == lentele[2][2] == zaidejas: return True
    else: return False
def tikrina_stulpelius (zaidejas, lentele):
    if lentele[0][0] == lentele[1][0] == lentele[2][0] == zaidejas: return True
    elif lentele[0][1] == lentele[1][1] == lentele[2][1] == zaidejas: return True
    elif lentele[0][2] == lentele[1][2] == lentele[2][2] == zaidejas: return True
    else: return False
def tikrina_istrizaines (zaidejas, lentele):
    if lentele[0][0] == lentele[1][1] == lentele[2][2] == zaidejas: return True
    elif lentele[0][2] == lentele[1][1] == lentele[2][0] == zaidejas: return True
    else: return False

def laimetojas (zaidejas, lentele):
    if tikrina_eilutes(zaidejas, lentele): return True
    if tikrina_stulpelius(zaidejas, lentele): return True
    if tikrina_istrizaines(zaidejas, lentele): return True
    else: return False


def zaidejas_2 (zaidejas):
    if zaidejas: return "x"
    else: return "o"

while ejimas < 9:
    aktyvus_zaidejas = zaidejas_2(zaidejas)
    print(sukurti_lentele(lentele))
    zaidejo_skaicius = input("Iveskite pozicijos skaiciu lenteleje nuo 1 iki 9:")
    zaidejo_skaicius = int(zaidejo_skaicius) - 1
    kord = koordinates(zaidejo_skaicius)
    if uzimta(kord, lentele):
        print("Uzimta, bandyti dar karta")
        continue
    ikelti_simboli(kord, lentele, aktyvus_zaidejas)
    if laimetojas(aktyvus_zaidejas, lentele):
        print(f'{aktyvus_zaidejas.upper()} Laimejo!')
        break
    ejimas +=1
    if ejimas == 9: print("lygiosios")
    zaidejas = not zaidejas
