from django.core.exceptions import ValidationError
from re import match


def check_name(name):
    """
    В имени только буквы и пробелы?
    """
    pattern = r'^[а-яА-Яa-zA-Z\s]+$'
    if match(pattern, name):
        raise ValidationError('В поле допустимы только буквы и пробелы')
