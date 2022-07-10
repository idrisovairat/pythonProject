def my_list(x,y):
    try:
        x, y = float(x), int(y)
        if x <= 0 or y >= 0:
            return 'ошибка x должен быть больше 0, а y должен быть меньше 0'
        else:
            result = 1
            for _ in range(abs(y)):
                result *= 1/x
            return f'резуотиаи возведения: {round(result,6)}'
    except ValueError:
        return 'программа работает только с числами'

print(my_list(2, -4))
