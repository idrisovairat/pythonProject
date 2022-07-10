virucka = float(input('выручка='))
rashodi = float(input('расходы='))
pribil = virucka - rashodi
if pribil > 0:
    print(f'рентабильность - {pribil/ virucka}')
    kolichestvol = int(input('сколько людей в компании работает = '))
    print(f'прибыль на 1 сотрудника - {pribil / kolichestvol}')
elif result < 0:
    print(f'работаете с убытком - {pribil}')
else:
    print(f'прибыль равна нулю')


