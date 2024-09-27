import math
import ast

def main():
	L = input("Введите список слов (каждое слово должно быть в кавычках): ")
	L = ast.literal_eval(f"[{', '.join(L.split(','))}]")
	L = map(lambda x: x.strip(), L)
	L = map(lambda x: x.lower(), L)
	print(str(list(L)))