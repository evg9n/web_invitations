from os import environ, path, listdir, getenv
from dotenv import load_dotenv


class Constants:
    """
    Класс с неизменяемыми константами из вирутальных переменных
    """
    def __init__(self):
        path_dir_env = path.abspath('env')
        try:
            for env in listdir(path_dir_env):
                if env.endswith('.env'):
                    load_dotenv(path.join(path_dir_env, env))
        except FileNotFoundError:
            pass

        # Django settings
        self.SECRET_KEY_DJANGO = environ.get('SECRET_KEY_DJANGO')
        assert self.SECRET_KEY_DJANGO, "Отсутствует SECRET_KEY_DJANGO"

        self.LANGUAGE_CODE_DJANGO = getenv('LANGUAGE_CODE_DJANGO', default='ru')
        self.TIME_ZONE_DJANGO = getenv('TIME_ZONE_DJANGO', default='Europe/Moscow')
        self.DEBUG_DJANGO = getenv('DEBUG_DJANGO', default='False') == 'True'
        self.ALLOWED_HOSTS = getenv('ALLOWED_HOSTS', default='127.0.0.1').split(' ')
        self.CSRF_TRUSTED_ORIGINS_DJANGO = getenv('CSRF_TRUSTED_ORIGINS_DJANGO',
                                                  default='https://*.127.0.0.1').split(' ')
        if not self.DEBUG_DJANGO:
            self.CSRF_COOKIE_DOMAIN_DJANGO = getenv('CSRF_COOKIE_DOMAIN_DJANGO')
            assert self.CSRF_COOKIE_DOMAIN_DJANGO, 'Не укказан CSRF_COOKIE_DOMAIN_DJANGO'

        self.NAME_GROOM = getenv('NAME_GROOM')
        assert self.NAME_GROOM, 'Не укказан NAME_GROOM'

        self.NAME_BRIDE = getenv('NAME_BRIDE')
        assert self.NAME_BRIDE, 'Не укказан NAME_BRIDE'

        self.MONTH = int(getenv('MONTH', default=0))
        assert self.MONTH != 0, 'Не укказан MONTH или установлено значение 0'
        assert 0 < self.MONTH < 13, 'MONTH - должен быть целочисленным числом в диапазоне от 1 до 12'

        self.DAY = int(getenv('DAY', default=0))
        assert self.DAY != 0, 'Не укказан DAY или установлено значение 0'
        assert 0 < self.DAY < 32, 'DAY - должен быть целочисленным числом в диапазоне от 1 до 31'

        self.YEAR = int(getenv('YEAR', default=0))
        assert self.YEAR != 0, 'Не укказан YEAR или установлено значение 0'
        assert 2024 <= self.YEAR, 'YEAR - должен быть целочисленным числом больше либо равно 2024'

        self.HOUR = int(getenv('HOUR', default=-1))
        assert self.HOUR >= 0, 'Не укказан HOUR или установлено значение отрицательное'
        assert 0 <= self.HOUR <= 24, 'HOUR - должен быть целочисленным числом в диапазоне от 0 до 24'

        self.MINUTES = int(getenv('MINUTES', default=0))
        assert self.MINUTES >= 0, 'Не укказан MINUTES или установлено значение отрицательное'
        assert 0 <= self.MINUTES <= 60, 'MINUTES - должен быть целочисленным числом в диапазоне от 1 до 31'

        self.PLACE = getenv('PLACE')
        assert self.PLACE, 'Не укказан PLACE'

        # База данных
        self.USERNAME_DB = environ.get('USERNAME_DB')
        self.NAME_DB = environ.get('NAME_DB')
        self.PASSWORD_DB = environ.get('PASSWORD_DB')
        self.HOST_DB = environ.get('HOST_DB')
        self.PORT_DB = environ.get('PORT_DB')

        self.WIDTH = float(getenv('WIDTH', default=0))
        assert self.WIDTH >= 0, 'Не укказан WIDTH или установлено значение отрицательное'

        self.LONGITUDE = float(getenv('LONGITUDE', default=0))
        assert self.LONGITUDE >= 0, 'Не укказан LONGITUDE или установлено значение отрицательное'

        self.NAME_LABEL = getenv('NAME_LABEL')
        assert self.NAME_LABEL, 'Не укказан NAME_LABEL'

    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise AttributeError('Constants are not changeable!')
        else:
            super().__setattr__(name, value)
