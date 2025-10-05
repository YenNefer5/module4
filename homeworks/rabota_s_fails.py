f = open("hello.txt", "w", encoding="utf-8")  # открываем файл на дозапись

sequence = ["Замученный дорогой,\n", "Я выбился из сил.\n", "И в доме лесника я\n", "Ночлега попросил.\n", "С улыбкой добродушной\n", "Старик меня пустил.\n", "И жестом дружелюбным\n", "На ужин пригласил!"]

f.writelines(sequence) # берет строки из sequence и записывает в файл (без переносов)

f.close()

import string
from collections import Counter

def get_words(filename):
    with open(filename, "r", encoding="utf8") as f:
        text = f.read()
    text = text.replace("\n", " ")
    translator = str.maketrans('',"", string.punctuation)
    text = text.translate(translator)
    words = [i for i in text.lower().split() if i]
    return words


def get_words_dict(words):
    words_dict = Counter(words)
    return words_dict


def main():
    filename = input("Введите название файла: ").strip()
    words = get_words(filename)
    words_dict = get_words_dict(words)
    total_words = len(words)
    unique_words = len(words_dict)
    print(f"Кол-во слов: {total_words}")
    print(f"Кол-во уникальных слов: {unique_words}")
    print("Все использованные слова:")
    for word, count in sorted(words_dict.items()):
        print(f"{word} {count}")

if __name__ == "__main__":
     main()