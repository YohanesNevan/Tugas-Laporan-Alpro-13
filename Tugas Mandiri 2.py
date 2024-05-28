def cek_palindrom(kalimat):
    kalimat = kalimat.replace(" ", "").lower()
    if len(kalimat) <= 1:
        return True
    elif kalimat[0] == kalimat[-1]:
        return cek_palindrom(kalimat[1:-1])
    else:
        return False

kalimat = input("Masukkan kalimat: ")
if cek_palindrom(kalimat):
    print(f"'{kalimat}' adalah palindrom.")
else:
    print(f"'{kalimat}' bukan palindrom.")
    
