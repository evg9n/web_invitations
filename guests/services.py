from constants import Constants
from datetime import datetime
from calendar import month_name
from locale import setlocale, LC_ALL

from . import models as m

c = Constants()


def get_drinks():
    """
    получаем напитки
    """
    return m.DrinkModel.objects.filter(is_active=True)


def get_cities():
    """
    получаем города
    """
    return m.CityModel.objects.filter(is_active=True)


def get_events():
    """
    получаем события
    """
    return m.EventModel.objects.filter(is_active=True).order_by('time_event')


def get_guest(slug: str):
    """
    Получаем информацию о госте
    """
    try:
        return m.GuestModel.objects.get(slug=slug)
    except m.GuestModel.DoesNotExist:
        return None


MONTHS = dict(
    января="January", февраля="February", марта="March", апреля="April",
    мая="May", июня="June", июля="July", августа="August",
    сентября="September", октября="October", ноября="November", декабря="December"
)


def get_context() -> dict:
    date = datetime(year=c.YEAR, month=c.MONTH, day=c.DAY, hour=c.HOUR, minute=c.MINUTES)
    # date_js = date.strftime(' %d, %Y %H:%M:%S')
    date_js = date.strftime('%Y-%m-%d %H:%M:%S')
    # date_js = 'July 24, 2024 13:00:00'
    full_date = date.strftime('%d.%m.%Y')
    setlocale(LC_ALL, 'ru_RU.UTF-8')
    name_month = month_name[date.month]
    # date_js = f"{MONTHS.get(name_month)}" + str(date_js)
    name_week_day = date.strftime('%A')
    context = dict(
        drinks=get_drinks(),
        events=get_events(),
        cities=get_cities(),
        bride=c.NAME_BRIDE.capitalize(),
        groom=c.NAME_GROOM.capitalize(),
        date_js=date_js,
        name_week_day=name_week_day,
        name_month=name_month,
        day=c.DAY,
        time=f'{c.HOUR if c.HOUR > 9 else "0" + str(c.HOUR)}:{c.MINUTES if c.MINUTES > 9 else "0" + str(c.MINUTES)}',
        full_date=full_date,
        place=c.PLACE,
        width=c.WIDTH,
        longitude=c.LONGITUDE,
        name_label=c.NAME_LABEL,
    )

    return context


def answers_guest(guest: m.GuestModel, request_post) -> bool:
    attendance = request_post.get('attendance')
    if attendance == 'yes':
        drinks = m.DrinkModel.objects.filter(is_active=True)
        guest.visit = 'да'
        for drink in drinks:
            if request_post.get(drink):
                guest.drinks.add(drink)
    elif attendance == 'no':
        guest.visit = 'нет'
    else:
        return False
    guest.date_time_answer = datetime.now()
    guest.save()
    return True
