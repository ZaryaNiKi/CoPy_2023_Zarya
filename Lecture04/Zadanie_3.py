import random
# Получаем количество чисел 
n = int(input("Введите количество чисел: "))
# Генерируем список случайных целых чисел
random_numbers = [random.randint(1, 100) for _ in range(n)]
print("Сгенерированный список:", random_numbers)
# Применяем сортировку Bogosort 
count = 0 # Количесво перемешиваний
while random_numbers != sorted(random_numbers):
    random.shuffle(random_numbers)
    count += 1
print("Список после сортировки Bogosort:", random_numbers, "за ", count)