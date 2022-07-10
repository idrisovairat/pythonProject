def div(a,b):
    try:
        a, b = int(a), int(b)
        davab = a / b
    except zerodivisionerror:
        return 'делить на ноль нельзя'
    return round(davab, 4)

print(div(input('введите первое число:'),input('введите второе число:')))