def main():
	numbers = input("Введите список чисел, разделенных точкой с запятой: ").split(";")
	print(list(map(lambda x: int(float(x)), numbers)))
	print(list(map(float, numbers)))