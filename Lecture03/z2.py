while True:
    try:
        num1 = int(input("Введите первое целое число > 0: "))
        if num1 <= 0:
            raise ValueError("Число должно быть  > 0.")
        num2 = int(input("Введите второе целое число > 0: "))
        if num2 <= 0:
            raise ValueError("Число должно быть > 0.")
        # Вычисление НОД с использованием алгоритма Евклида
        while num2:
            num1, num2 = num2, num1 % num2
        print(f"НОД чисел: {num1}")
        break  # Выходим из цикла, если все вводы корректны
    except ValueError as e:
        print(f"Ошибка: {e}.")