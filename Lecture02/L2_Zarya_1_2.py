cifra = ["ноль", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
desatok = ["десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"]
desatok_ybilai = ["", "", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]

number = input("Введите число от 0 до 99: " )

if number in ' '.join(map(str, list(range(100)))):
    number = int(number)
    if number < 0 or number > 99: print("Неправильный ввод") 
    if number < 10:  print(cifra[number])
    elif number < 20: print(desatok[number - 10])
    else: print( desatok_ybilai[number // 10] + (" " + cifra[number % 10] if number % 10 != 0 else ""))
else:
    print("Вы ввели не правильную строку")