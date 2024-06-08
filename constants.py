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

        # База данных
        self.USERNAME_DB = environ.get('USERNAME_DB')
        self.NAME_DB = environ.get('NAME_DB')
        self.PASSWORD_DB = environ.get('PASSWORD_DB')
        self.HOST_DB = environ.get('HOST_DB')
        self.PORT_DB = environ.get('PORT_DB')

    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise AttributeError('Constants are not changeable!')
        else:
            super().__setattr__(name, value)
