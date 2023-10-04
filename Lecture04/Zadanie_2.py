import random
# Получаем количество чисел 
n = int(input("Введите количество чисел: "))
# Генерируем список случайных целых чисел
random_numbers = [random.randint(1, 100) for _ in range(n)]
print("Сгенерированный список:", random_numbers)
# Сортируем сгенерированный список
for i in range(len(random_numbers)):
    for j in range(0, len(random_numbers) - i - 1):
        if random_numbers[j] > random_numbers[j + 1]:
            random_numbers[j], random_numbers[j + 1] = random_numbers[j + 1], random_numbers[j]
# Выводим отсортированный список
print("Отсортированный список методом пузырька:", random_numbers)