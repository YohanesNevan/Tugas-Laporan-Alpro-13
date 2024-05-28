def permutasi(m, n):
    # m : batas atas dan n : batas bawah, dimana m > n
    if n == 0:
        # jika n = 0, maka hasil adalah m!/(m-(n-1))! = 1
        return 1
    else:
        # jika n > 0, panggil method permutasi secara rekursif dengan parameter n-1 sampai n
        return permutasi(m, n-1) * (m-n+1)
        # kembalikan nilai permutasi dengan parameter m dan n-1 dikalikan dengan (m-n+1)

print(permutasi(10, 4))  # Hasilnya adalah 5040, karena P(10, 4) = 10 * 9 * 8 * 7 = 5040
