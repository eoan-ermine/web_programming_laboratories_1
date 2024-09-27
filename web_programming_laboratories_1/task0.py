def main():
	full_name = input("Введите ваше ФИО: ").split(" ")
	if len(full_name) != 3:
		print("Введено неправильное ФИО")
		return
	last_name, first_name, third_name = full_name
	print(f"Ваша фамилия: {last_name}")
	print(f"Ваше имя: {first_name}")
	print(f"Ваше отчество: {third_name}")