# Домашнее задание

import math
a = float(input("Введите длину первой стороны: "))
b = float(input("Введите длину второй стороны: "))
c = float(input("Введите угол между сторонами в градусах: "))
cosinus = math.cos(math.radians(c))
kv_3_storoni = a**2 + b**2 - 2 * a * b * cosinus
dlina_3_storoni = math.sqrt(kv_3_storoni)
print(f"Длина третьей стороны равна:{dlina_3_storoni}")
