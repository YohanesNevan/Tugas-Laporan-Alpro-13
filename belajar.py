x=3
total = x
for i in range(3):
    total += 1
    if i==2:
        print(f"{x-i}", end="")
        break
    print(f"{x-i} + ", end='')
    total +=1
print(f" = {total}")


def rekrusif(x):
    print(f" = {x},= ", end='')
    if x ==1:
        
        return x
    else:
        print(f" = {x}+ ", end='')
        return 'x' + rekrusif(x-1)
print(rekrusif(3))

def function_name(parameter_list):
    ...
    function_name(...)
    ...
    
def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return faktorial(n-1) * n

print(faktorial(4))

