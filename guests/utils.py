from django.utils.text import slugify


def cyrillic_to_slug(text):
    """
    замена кириллические символы на ближайшие аналоги на латинице
    """
    cyrillic_letters = {
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd',
        'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i',
        'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n',
        'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
        'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch',
        'ш': 'sh', 'щ': 'shch', 'ъ': 'ie', 'ы': 'y', 'ь': '',
        'э': 'e', 'ю': 'yu', 'я': 'ya'
    }
    translit_text = ''.join(cyrillic_letters.get(char, char) for char in text.lower())
    return slugify(translit_text)


if __name__ == '__main__':
    print(cyrillic_to_slug('Check функции'))
