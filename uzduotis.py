# Uzduotis: veikia
# Leistų žaisti dviems žaidėjams (X ir O)+++
# Teisingai fiksuotų žaidėjo laimėjimą ir stabdytų žaidimą+++
# Žaidimas vyktų konsolėje, grafinio interfeiso nereikia (bet galima daryti, tada konsolės nebereikia)+++
# Sukurtą žaidimą paskelbti github repozitorijoje, nuorodą paskelbti teamsuose, tam skirtoje
# užduotyje (Assignments) public arba itraukti i coloborators
#
# PAPILDOMAI (nebūtina):
#
# Kad baigus žaidimą, programa neišsijungtų, o leistų pakartoti žaidimą. Taip pat
# būtų galimybė išjungti programą.++
# Kad žaidimas skaičiuotų abiejų žaidėjų sesijos laimėjimus.
# Leistų žaisti prieš kompiuterį (sukurti logiką, kaip jis elgsis)
# Padaryti GUI (su tkinter, pygame, dar kažkuo)


print('\nSveiki atvykę į žaidimą tik-tak-toe!\n')


def atspausdinti_lenta(lenta):
    """
    Atspausdina lentą.
    """
    print('----------')
    print(lenta[7] + ' | ' + lenta[8] + ' | ' + lenta[9])
    print('----------')
    print(lenta[4] + ' | ' + lenta[5] + ' | ' + lenta[6])
    print('----------')
    print(lenta[1] + ' | ' + lenta[2] + ' | ' + lenta[3])
    print('----------')


def zaidimas():
    """
    Pagrindinis žaidimo loopas
    """
    while True:
        lenta = [' '] * 10
        zaidejas = 'X'
        nugaletojas = None
        atspausdinti_lenta(lenta)

        while not nugaletojas:
            ejimas = input(f"\nŽaidėjau {zaidejas}, pasirinkite skaičių intervale (1-9): ")

            # Tikrina ar įvedimas skaičius

            if not ejimas.isdigit():
                print("\nPabandykite įvesti dar kartą. Prašome įvesti skaičių tik intervale (1-9).")
                continue

            ejimas = int(ejimas)

        # Tikrina ar įvedimas yra intervale

            if ejimas < 1 or ejimas > 9:
                print("\nĮvestas skaičius nepriklauso intervalui (1-9). Prašome pabandyti dar kartelį.")
                continue

            if lenta[ejimas] == ' ':
                lenta[ejimas] = zaidejas
                atspausdinti_lenta(lenta)
                nugaletojas = tikrina_laimetoja(lenta)

                if not nugaletojas:
                    # Tikrina ar lygiosios
                    if all(mark != ' ' for mark in lenta[1:]):
                        print("Lygiosios!")
                        break

                    zaidejas = 'O' if zaidejas == 'X' else 'X'
            else:
                print("Šis langelis jau užimtas. Pabandykite dar kartą.")

        if nugaletojas:
            print(f"\nSveikiname žaidėjau {nugaletojas}! Laimėjai žaidimą.")
            print("  _____          __  __ ______    ______      ________ ______")
            print(" / ____|   /\   |  \/  |  ____|  / __ \ \    / /  ____|  __  |")
            print("| |  __   /  \  | \  / | |__    | |  | \ \  / /| |__  | |__) |")
            print("| | |_ | / /\ \ | |\/| |  __|   | |  | |\ \/ / |  __| | __  / ")
            print("| |__| |/ ____ \| |  | | |____  | |__| | \  /  | |____| | \ \ ")
            print(" \_____/_/    \_\_|  |_|______|  \____/   \/   |______|_|  \_|")

        while True:
            pasirinkimas = input("\nAr norite žaisti dar kartą? (Taip/Ne): ")
            if pasirinkimas.lower() == "taip":
                break
            elif pasirinkimas.lower() == "ne":
                print("\nAčiū, kad žaidėte!")
                return
            else:
                print("\nNeteisingas pasirinkimas. Prašome pasirinkti Taip arba Ne.")


def tikrina_laimetoja(lenta):
    """
    Tikrina ar žaidimas buvo laimėtas ir grąžina laimėtoją
    """
    for zaidejas in ['X', 'O']:
        if (lenta[1] == lenta[2] == lenta[3] == zaidejas or
                lenta[4] == lenta[5] == lenta[6] == zaidejas or
                lenta[7] == lenta[8] == lenta[9] == zaidejas or
                lenta[1] == lenta[4] == lenta[7] == zaidejas or
                lenta[2] == lenta[5] == lenta[8] == zaidejas or
                lenta[3] == lenta[6] == lenta[9] == zaidejas or
                lenta[1] == lenta[5] == lenta[9] == zaidejas or
                lenta[3] == lenta[5] == lenta[7] == zaidejas):
            return zaidejas

    return None


# Pradeda žaidimą(inicijuoja)
zaidimas()
