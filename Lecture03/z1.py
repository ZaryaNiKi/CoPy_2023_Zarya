try:
    N = int(input("Введите число N: "))
    if N < 2:
        raise ValueError("Число N должно быть >= 2.")
except ValueError as e:
    print(f"Ошибка: {e}")
else:
    sieve = [True] * (N + 1) #Создаём таблицу "Истиности"
    sieve[0] = sieve[1] = False #Вычёркиваем числа из таблицы "Истиности"

    for current in range(2, int(N**0.5) + 1):
        if sieve[current]:
            for multiple in range(current*current, N+1, current):#Вычёркиваем числа от [n**2,N+1] с шагом n
                sieve[multiple] = False

    prime_numbers = [x for x in range(2, N + 1) if sieve[x]]

    print(f"Простые числа от 2 до {N}: {prime_numbers}")
