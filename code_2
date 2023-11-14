def check_age():
    age = int(input("Введіть свій вік: "))
    if age < 18:
        print("Ви ще неповнолітній")
    else:
        print("Ви повнолітній")

def draw_pyramid():
    pyramid_height = int(input("Введіть висоту піраміди: "))
    for i in range(1, pyramid_height + 1):
        print(" " * (pyramid_height - i) + "*" * (2 * i - 1))

def reverse_sentence():
    sentence = input("Введіть речення: ")
    reversed_sentence = sentence[::-1]
    print("Реверс речення:", reversed_sentence)

def most_common_letter():
    word = input("Введіть слово: ")
    letter_count = {}
    for letter in word:
        letter_count[letter] = letter_count.get(letter, 0) + 1
    most_common = max(letter_count, key=letter_count.get)
    print(f"Найчастіше зустрічається буква '{most_common}' ({letter_count[most_common]} разів)")

def process_numbers():
    numbers_input = input("Введіть послідовність чисел, розділених комою: ")
    numbers_list = [float(num) for num in numbers_input.split(',')]
    numbers_tuple = tuple(numbers_list)
    total_sum = sum(numbers_list)
    average = total_sum / len(numbers_list)
    
    print("Список чисел:", numbers_list)
    print("Кортеж чисел:", numbers_tuple)
    print("Сума чисел:", total_sum)
    print("Середнє арифметичне:", average)

def generate_squares():
    n = int(input("Введіть число n: "))
    squares_list = [i**2 for i in range(1, n + 1)]
    print("Список квадратів чисел:", squares_list)

def student_grades():
    students = {}
    while True:
        name = input("Введіть ім'я студента (або 'stop' для завершення): ")
        if name.lower() == 'stop':
            break
        grades_input = input(f"Введіть оцінки для {name}, розділені комою: ")
        grades = [int(grade) for grade in grades_input.split(',')]
        students[name] = grades

    print("Імена студентів та їх оцінки:")
    for student, grades in students.items():
        print(f"{student}: {grades}")

def student_grades_multiple():
    students = {}
    while True:
        name = input("Введіть ім'я студента (або 'stop' для завершення): ")
        if name.lower() == 'stop':
            break
        grades_input = input(f"Введіть оцінки для {name}, розділені комою: ")
        grades = [int(grade) for grade in grades_input.split(',')]
        students[name] = grades

    print("Імена студентів та їх оцінки:")
    for student, grades in students.items():
        print(f"{student}: {grades}")

def main():
    check_age()
    draw_pyramid()
    reverse_sentence()
    most_common_letter()
    process_numbers()
    generate_squares()
    student_grades()
    student_grades_multiple()

if __name__ == "__main__":
    main()
