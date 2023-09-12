import math

first_side = float(input('Введите длину первой стороны = '))
second_side = float(input('Введите длину второй стороны = '))
angle_btwn_sides =float(input('Введите угол между сторонами в радианах = '))

if -1 < math.cos(angle_btwn_sides) < 1:
   last_side = first_side**2 + second_side**2-2*first_side*second_side*math.cos(angle_btwn_sides)
   print('Длина третьей староны по теореме косинусов = ', math.sqrt(last_side))
else:
   print('Триугольника не существует')
