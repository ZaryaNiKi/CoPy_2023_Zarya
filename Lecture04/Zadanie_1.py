import random
# Получаем количество чисел 
n = int(input("Введите количество чисел: "))
# Генерируем список случайных целых чисел
random_numbers = [random.randint(1, 100) for _ in range(n)]
print("Сгенерированный список:", random_numbers)