import math

def main():
	L = input("Введите список значений доходов домохозяйств за месяц: ")
	L = map(float, L.split(","))
	L = map(math.log, L)
	print(", ".join(map(str, L)))