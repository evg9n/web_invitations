from django.db import models

from guests.validators import check_name


class BaseModel(models.Model):
    """
    Базовая модель
    """
    is_active = models.BooleanField(default=True, verbose_name='Показывать?')
    date_time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')

    class Meta:
        abstract = True  # не создавать таблицу в базе данных


class DrinkModel(BaseModel):
    """
    Модель напитков
    """
    name = models.CharField(max_length=128, verbose_name='Напиток')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'напиток'
        verbose_name_plural = 'напитки'


class CityModel(BaseModel):
    """
    Модель города откуда и куда заказывать трансфер
    """
    name = models.CharField(max_length=128, verbose_name='Город')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'город'
        verbose_name_plural = 'города'


class GuestModel(BaseModel):
    """
    Модели гостя
    """
    name = models.CharField(max_length=128, unique=True,
                            help_text='данное поле не будет использовано в приветствии гостя(ей), '
                                      'оно будет использовано в качестве имени карточки '
                                      'и для создании индивидуальной ссылки',
                            verbose_name='Название карточки')
    slug = models.SlugField(max_length=256, unique=True, blank=True, null=True, editable=False, verbose_name='slug')
    CHOICE_YES_OR_NO = (
        ('да', 'да'),
        ('нет', 'нет'),
    )
    name_first = models.CharField(max_length=128, validators=[check_name],
                                  help_text='Имя первого гостя. Будет отображаться в приветствии.'
                                            'Если будет более двух гостей, то нужно обощить их общей фамилией, '
                                            'если она общая, иначе нужно на каждого гостя сделать свою карточку',
                                  verbose_name='Имя(Фамилия) гостя(ей)')
    CHOICE_SEX = (
        ('она', 'она'),
        ('он', 'он'),
        ('они', 'они'),
    )
    sex = models.CharField(max_length=3, choices=CHOICE_SEX, verbose_name='Пол первого гостя',
                           help_text='Если их будет более одно, то установить нужно "они"')
    visit_first_guest = models.CharField(max_length=3, choices=CHOICE_YES_OR_NO, verbose_name='Придет?')

    name_second = models.CharField(max_length=128, null=True, blank=True, validators=[check_name],
                                   help_text="В этом поле ожидается парень/девушка/супруг/супруга первого гостя")
    visit_second_guest = models.CharField(max_length=3, choices=CHOICE_YES_OR_NO, verbose_name='Придет?')
    to_transfer = models.CharField(max_length=3, choices=CHOICE_YES_OR_NO,
                                   verbose_name='Нужен трансфер НА мероприятие?')
    from_city = models.ManyToManyField(CityModel, verbose_name='С какого города забрать на мероприятие?')
    from_transfer = models.CharField(max_length=3, choices=CHOICE_YES_OR_NO,
                                     verbose_name='Нужен трансфер С мероприятия?')
    to_city = models.ManyToManyField(CityModel, related_name='cites',
                                     verbose_name='В какой город отвезти после мероприятия?')
    drinks = models.ManyToManyField(DrinkModel, related_name='drinks', verbose_name='Какие напитки будут?')
    date_time_answer = models.DateTimeField(blank=True, null=True, editable=False, verbose_name='Дата и время ответа')
    date_time_answer_edit = models.DateTimeField(blank=True, null=True, editable=False,
                                                 verbose_name='Дата и время редактирования ответа')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'гость'
        verbose_name_plural = 'гости'
