def cek_prima(bilangan, pembagi=None):
    if pembagi is None:
        pembagi = bilangan - 1

    if bilangan <= 1:
        return False
    elif pembagi == 1:
        return True
    elif bilangan % pembagi == 0:
        return False
    else:
        return cek_prima(bilangan, pembagi - 1)

angka = int(input("Masukkan bilangan: "))
if cek_prima(angka):
    print(f"{angka} adalah bilangan prima.")
else:
    print(f"{angka} bukan bilangan prima.")
