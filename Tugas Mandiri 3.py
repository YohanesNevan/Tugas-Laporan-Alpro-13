def deret_ganjil(n):
    if n == 1:
        return 1
    else:
        return n + deret_ganjil(n - 2)

def jumlah_deret_ganjil(n):
    if n <= 0:
        return 0
    else:
        return deret_ganjil(n) + jumlah_deret_ganjil(n - 2)
n = 7
print(f"Jumlah deret ganjil dari 1 hingga {n} adalah {jumlah_deret_ganjil(n)}")
