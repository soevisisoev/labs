
russian_alphabet = set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
text = "карочи этот текст для проверки на наличие букв в алфавите."
text = text.lower()
use = set()
for char in text:
    if char in russian_alphabet:
        use.add(char)
unuse = russian_alphabet - use
count_unused = len(unuse)
print("Количество букв русского алфавита, не встречающихся в тексте:", count_unused)
print("Неиспользованные буквы:", unuse)