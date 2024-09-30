def main():
	L = input("Введите список слов: ")
	L = L.split(",")
	L = map(lambda x: x.strip(), L)
	L = map(lambda x: x.lower(), L)
	print(list(L))