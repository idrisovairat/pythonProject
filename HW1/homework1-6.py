while True:
    days = 1
    start1 = float(input('нач результат = '))
    finish1 = float(input('фин результат = '))
    if start1 <= 0 or finish1 < 0:
        print('точно уж не ноль')
    else:
        while start1 < finish1:
            start1  *= 1.1
            days += 1
        print(f'спортсмен добъетмя результата за {days} дней')

