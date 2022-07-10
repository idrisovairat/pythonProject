sec = int(input('введите время в секунданх:'))
sec1 = sec % 60
hours = sec // 3600
minutes = (sec // 60) - (hours * 60)
print(f"{hours:02}:{minutes:02}:{sec1:02}")
