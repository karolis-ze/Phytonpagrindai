"""
I užduotis:
    Sukurti funkcijas, kurios:
        Gražintų visų paduotų skaičių sumą (su *args argumentu)
        Gražintų paduoto skaičiaus šaknį (panaudoti math.sqrt())
        Gražintų paduoto sakinio simbolių kiekį (su len())
        Gražintų rezultatą, skaičių x padalinus iš y

    Nustatyti standartinį logerį (logging) taip, kad jis:
        Saugotų pranešimus į norimą failą
        Saugotų INFO lygio žinutes
        Pranešimai turi būti tokiu formatu: data/laikas, lygis, žinutė

    Kiekviena funkcija turi sukurti INFO lygio log pranešimą apie tai, ką atliko, pvz.:
        logging.info(f'Skaiciu {args} suma lygi: {sum(args)}')
"""


# Jūsų kodas

import logging



logging.basicConfig(
    filename='modulis.log',
    level=logging.INFO,
    format='%(asctime)s -%(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    encoding='utf-8'
)
logging.info("Aplikacija sėkmingai paleista.")
logging.warning("Įspėjimas: trūksta kai kurių duomenų.")
logging.error("Klaida: nepavyko prisijungti prie duomenų bazės.")
logging.debug("Ši žinutė nebus įrašyta, nes DEBUG yra žemesnio lygio nei INFO.")


def skaiciu_suma(*skaiciai):
    suma = sum(skaiciai)
    logging.info(f"Skaiciu {skaiciai} suma lygi {suma}")
    return suma

def skaiciaus_saknis(skaicius):
    if skaicius < 0:
        rezultatas = "Klaida neigiamas skaicius neturi saknies"
        logging.info(f"Mėginta traukti šaknį iš neigiamo skaičiaus ({skaicius}): {rezultatas}")
        return rezultatas
    rezultatas = skaicius ** 0.5
    logging.info(f'Skaičiaus {skaicius} kvadratinė šaknis lygi: {rezultatas}')
    return rezultatas

def kiek_zodis_simboliu(zodis):
    if not isinstance(zodis, str) or not zodis.isalpha():
        klaida = f"Klaida: Įvesta ne raidės/žodis ('{zodis}')"
        logging.error(klaida)  # arba logging.info pagal poreikį
        return klaida
    
    kiekis = len(zodis)
    logging.info(f'Teksto "{zodis}" simbolių kiekis yra: {kiekis}')
    return kiekis

def dalyba(x, y):
    if y == 0:
        rezultatas = "Klaida: dalyba iš nulio negalima"
        logging.info(f'Mėginta dalinti {x} iš 0: {rezultatas}')
        return rezultatas
    
    rezultatas = x / y
    logging.info(f'Dalybos {x} / {y} rezultatas lygus: {rezultatas}')
    return rezultatas


skaiciu_suma(2, 5, 10)
skaiciaus_saknis(16)
kiek_zodis_simboliu("256")
dalyba(10, 2)


"""
II užduotis
    Perdaryti 1 užduoties programą, kad:
        Į šaknies funkciją padavus string tipo argumetrą, į log failą būtų išsaugoma išimties klaida su norimu tekstu
        Į dalybos funkciją antrą argumentą padavus 0, į log failą būtų išsaugoma išimties klaida su norimu tekstu
    Patarimas: panaudoti try/except/else, logging.exception()
"""


# Jūsų kodas



"""
III užduotis
    Perdaryti 2 užduoties programą, kad:
        Būtų sukurtas savo logeris, kuris fikstuotus visus anksčiau aprašytus pranešimus
        Sukurtas logeris ne tik išsaugotų pranešimus faile, bet ir atvaizduotų juos konsolėje
"""


# Jūsų kodas


