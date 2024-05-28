def toBasis(n, base):
    convertString = "0123456789ABCDEF"
    if n < base:
        return convertString[n]
    else:
        return toBasis(n // base, base) + convertString[n % base]

print("Silahkan masukkan bilangan dan basis")
angka = int(input("Bilangan : "))
basis = int(input("Basis (2/8/16) : "))
print(toBasis(angka, basis))
