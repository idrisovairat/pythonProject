chislo = int(input('введите целое пол.число'))
max = chislo % 10
chislo1 = chislo

while chislo1 > 0:
    chislo2 = chislo1 % 10
    if chislo2 > max:
        max = chislo2

    if chislo2 == 9:
        break

    chislo1 //= 10 # chislo1 = chislo1 // 10
    print(chislo1)

