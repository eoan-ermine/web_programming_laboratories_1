def main():
	numbers = input("Введите список чисел, разделенных точкой с запятой: ").split(";")
	numbers = list(map(float, numbers))
	print(list(filter(lambda x: x % 1 == 0, numbers)))
	print(list(filter(lambda x: x % 1 != 0, numbers)))