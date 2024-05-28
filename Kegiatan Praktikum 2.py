def pangkat(bil1, bil2):
    if bil2 == 1:
        print("%d = " % (bil1), end='')
        return bil1
    else:
        print("%d * " % (bil1), end='')
        return bil1 * pangkat(bil1, bil2 - 1)

print(pangkat(2, 4))
