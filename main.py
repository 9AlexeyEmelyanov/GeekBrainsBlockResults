first_list = ["Hello", "2", "world", ":-)"]
second_list = ["1234", "1567", "-2", "computer science"]
third_list = ["Russia", "Denmark", "Kazan"]
# Создаем пустой список


def formingNewLine(lst : list):
    # Инициализируем пустой массив
    new_arr = []
    # Проходим по всем элементам исходного массива
    for i in range(len(lst)):
        # Если длина текущей строки меньше или равна 3 символам, то добавляем ее в новый массив
        if len(lst[i]) <= 3:
            new_arr.append(lst[i])
    return new_arr



def main():
    # Выводим полученный массив
    print("Новый массив: ", formingNewLine(first_list))
    print("Новый массив: ", formingNewLine(second_list))
    print("Новый массив: ", formingNewLine(third_list))

if __name__ == "__main__":
    main()