import re

def create_file_TF22_1():
    with open('TF22_1.txt', 'w', encoding='utf-8') as file:
        file.write("Привіт, як справи?\n")
        file.write("Ця програма написана для пошуку найкращих слів.\n")
        file.write("Слова, які мають символ а, будуть відібрані.\n")

def print_file_TF22_1():
    """
    Читання і виведення вмісту файлу TF22_1.txt.
    """
    try:
        with open('TF22_1.txt', 'r', encoding='utf-8') as file:
            content = file.readlines()
            if content:
                print("Вміст файлу TF22_1:")
                for line in content:
                    print(line.strip())
            else:
                print("Файл TF22_1 порожній.")
    except FileNotFoundError:
        print("Файл TF22_1 не знайдено.")

def find_longest_words_with_a():
    try:
        with open('TF22_1.txt', 'r', encoding='utf-8') as file:
            content = file.read()

        words = re.findall(r'\b\w+\b', content)

        words_with_a = [word for word in words if 'а' in word]

        if not words_with_a:
            with open('TF22_2.txt', 'w', encoding='utf-8') as file:
                file.write("Немає слів, що містять символ 'а'.\n")
        else:
            max_length = max(len(word) for word in words_with_a)

            longest_words_with_a = [word for word in words_with_a if len(word) == max_length]

            with open('TF22_2.txt', 'w', encoding='utf-8') as file:
                for word in longest_words_with_a:
                    file.write(word + '\n')

    except FileNotFoundError:
        print("Файл TF22_1 не знайдено.")

def print_file_TF22_2():
    """
    Читання і виведення вмісту файлу TF22_2.txt.
    """
    try:
        with open('TF22_2.txt', 'r', encoding='utf-8') as file:
            content = file.readlines()
            if content:
                print("Вміст файлу TF22_2 (слова з літерою 'а' найбільшої довжини):")
                for line in content:
                    print(line.strip())
            else:
                print("Файл TF22_2 порожній.")
    except FileNotFoundError:
        print("Файл TF22_2 не знайдено.")

if __name__ == "__main__":
    create_file_TF22_1()

    print_file_TF22_1()

    find_longest_words_with_a()

    print_file_TF22_2()
