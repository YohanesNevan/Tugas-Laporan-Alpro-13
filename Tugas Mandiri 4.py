def jumlah_digit(bilangan):
    if bilangan < 10:
        return bilangan, str(bilangan)
    else:
        hasil, representasi = jumlah_digit(bilangan // 10)
        sisa = bilangan % 10
        return sisa + hasil, representasi + " + " + str(sisa)

def print_jumlah_digit(bilangan):
    hasil, representasi = jumlah_digit(bilangan)
    print(f"{representasi} = {hasil}")

print_jumlah_digit(234)
