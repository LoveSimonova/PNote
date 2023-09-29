from Notes import write, find_date, read_all

def choose(choice):
    if choice == '1': write(input("Введите заголовок заметки: "))
    if choice == "2": find_date(input("Введите время создания или редактирования заметки: "))
    if choice == "3": read_all()
    if choice == "4": exit()

def print_instructions():
    return print('Выберите действие: \n 1 - Создать заметку \n 2 - Найти заметку по дате \n '
                 '3 - Показать все заметки \n 4 - Остановка программы')

