def get_cats_info(path):
    cats_info = [] # Список для збереження інформації про котів

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                cat_id, name, age = line.strip().split(',')

                cat = {
                    "id": cat_id,
                    "name": name,
                    "age": age
                }

                cats_info.append(cat)

    except FileNotFoundError:
        print("Файл не знайдено")
    except OSError:
        print("Помилка при читанні файлу")
    except ValueError:
        print("Помилка у форматі даних")

    return cats_info

cats_info = get_cats_info("cats_file.txt")
for cat in cats_info:
    print(f"ID: {cat['id']}")
    print(f"Ім'я: {cat['name']}")
    print(f"Вік: {cat['age']} років")
    print("-" * 40)