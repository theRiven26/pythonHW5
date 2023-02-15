# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# 2 2
# 4


a = int(input("A = "))
b = int(input("B = "))

def Summa(a, b):
	if b > 0:
		return a + Summa(1, b - 1)
	else:
		return a
print(Summa(a, b))