groupmates = [
    {
        "name": "Антон",
        "surname": "Ягельский",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [4, 2, 5]
    },
    {
        "name": "Игорь",
        "surname": "Петров",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [3, 4, 4]
    },
    {
        "name": "Максим",
        "surname": "Смирнов",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [5, 4, 5]
    }
]

def filter_and_print_students(students_list):
    # 1. Запрашиваем пороговый средний балл
    threshold_average = float(input("Введите минимальный средний балл для фильтрации: "))

    print(f"\n--- Студенты со средним баллом выше {threshold_average:.2f}: ---\n")

    # выводим заголовоки таблицы
    print("Имя".ljust(15), "Фамилия".ljust(15), "Экзамены".ljust(35), "Оценки".ljust(15), "Средний балл".ljust(15))
    print("-" * 100) # Разделительная линия

    for student in students_list:
        marks = student["marks"] # Получаем оценки циклом
        average_mark = sum(marks) / len(marks)

        if average_mark > threshold_average:
            # Форматированный вывод данных
            print(
                student["name"].ljust(15),
                student["surname"].ljust(15),
                str(student["exams"]).ljust(35),
                str(student["marks"]).ljust(15),
                f"{average_mark:.2f}".ljust(15)
            )
    
    print("\n" + "-" * 100) # Разделительная линия

# Вызов функции
filter_and_print_students(groupmates)