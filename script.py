
from os import remove, makedirs, path, listdir
y = 'c:/заметки'

if not path.exists(y):
    makedirs(y)

while True:
    x = input("Что вы хотите сделать: для чтения заметок пишите 'r', для создания заметки 'w', для удаления заметки 'd', для выхода 'exit': ")

    if x == 'exit':
        break

    if x == 'w':
        n = input("Введите название заметки: ")
        file_path = path.join(y, n)

        with open(file_path, "a", encoding="utf-8") as f:
            p = input("Введите текст заметки: ")
            f.write(p)  

    elif x == 'r':
        contents = listdir(y)
        if contents:
            result = ', '.join(contents)
            print("Содержимое директории:", result)

            ff = input("Какую заметку вы хотите прочитать: ")
            if ff in contents:
                file_path = path.join(y, ff)
                try:
                    with open(file_path, "r", encoding="utf-8") as h:
                        m = h.read()
                        print(m)
                except Exception as e:
                    print(f"Ошибка при чтении файла: {e}")
            else:
                print(f"Файл '{ff}' не найден в директории.")
        else:
            print("В директории нет заметок.")

    elif x == 'd':
        contents = listdir(y)
        if contents:
            result = ', '.join(contents)
            print("Содержимое директории:", result)

            dd = input("Какую заметку хотите удалить: ")
            if dd in contents:
                file_to_delete = path.join(y, dd)
                try:
                    remove(file_to_delete)
                    print(f'Файл "{dd}" был успешно удален.')
                except Exception as e:
                    print(f"Ошибка при удалении файла: {e}")
            else:
                print(f"Файл '{dd}' не найден в директории.")
        else:
            print("В директории нет заметок для удаления.")
    else:
        print("Неверная команда. Пожалуйста, попробуйте снова.")

