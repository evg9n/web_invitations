from io import BytesIO

from xlsxwriter import Workbook
from xlsxwriter.format import Format

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
    return m.EventModel.objects.filter(is_active=True).order_by('date', 'time_event')


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
            if request_post.get(drink.name):
                guest.drinks.add(drink)
    elif attendance == 'no':
        guest.visit = 'нет'
    else:
        return False
    guest.date_time_answer = datetime.now()
    guest.save()
    return True


def get_style(wb: Workbook, **kwargs) -> Format:
    """
    Вспомогательная функция для получения форматирования ячейки
    """
    font_name = 'Times New Roman'
    kwargs['font_name'] = font_name
    return wb.add_format(kwargs)


def generate_excel(request) -> BytesIO:
    """
    Создаем файл Excel в памяти
    """

    output = BytesIO()
    wb = Workbook(output, {'in_memory': True})
    ws = wb.add_worksheet()

    # Данные для записи
    format_cell = get_style(wb, align='center', valign='vcenter', text_wrap=True, bold=True, border=1)

    ws.set_column(0, 4, 20)
    ws.set_column(5, 5, 1)
    ws.set_column(6, 7, 10)
    ws.set_column(8, 8, 1)
    ws.set_column(9, 10, 10)

    row = 0
    ws.merge_range(first_row=row, last_row=row, first_col=0, last_col=4,
                   data='Ответы гостей', cell_format=format_cell)

    ws.merge_range(first_row=row, last_row=row, first_col=6, last_col=7,
                   data='Итоги', cell_format=format_cell)

    ws.merge_range(first_row=row, last_row=row, first_col=9, last_col=10,
                   data='Итоги по напиткам', cell_format=format_cell)

    row += 1
    ws.write(row, 0, '№ п/п', format_cell)
    ws.write(row, 1, 'Имя', format_cell)
    ws.write(row, 2, 'Придет?', format_cell)
    ws.write(row, 3, 'Напитки', format_cell)
    ws.write(row, 4, 'Дата ответа', format_cell)

    ws.write(row, 6, 'Ответ', format_cell)
    ws.write(row, 7, 'Количество', format_cell)

    ws.write(row, 9, 'Напиток', format_cell)
    ws.write(row, 10, 'Количество', format_cell)

    row += 1
    ws.write(row, 0, '1', format_cell)
    ws.write(row, 1, '2', format_cell)
    ws.write(row, 2, '3', format_cell)
    ws.write(row, 3, '4', format_cell)

    format_cell = get_style(wb, align='center', valign='vcenter', text_wrap=True, border=1)

    guests = m.GuestModel.objects.all()
    dict_drink = dict()
    dict_guest = {
        'Придут': 0,
        'Не придут': 0,
        'Не ответили': 0,
    }
    row += 1
    number = 0
    for guest in guests:
        name = guest.name
        visit = guest.visit
        date_time_answer = guest.date_time_answer
        drinks = ''
        if guest.visit == 'да':
            dict_guest['Придут'] += 1
            for drink in guest.drinks.all():
                if dict_drink.get(drink):
                    dict_drink[drink] += 1
                else:
                    dict_drink[drink] = 1
                drinks += f'{drink} '
        elif guest.visit == 'нет':
            dict_guest['Не придут'] += 1
        else:
            dict_guest['Не ответили'] += 1
            visit = 'не ответили'
        number += 1
        ws.write(row, 0, number, format_cell)
        ws.write(row, 1, name, format_cell)
        ws.write(row, 2, visit, format_cell)
        ws.write(row, 3, drinks, format_cell)
        ws.write(row, 4, str(date_time_answer.strftime('%Y.%m.%d - %H:%M')) if date_time_answer else '', format_cell)

        row += 1

    row = 2
    for key, value in dict_guest.items():
        ws.write(row, 6, key, format_cell)
        ws.write(row, 7, value, format_cell)
        row += 1

    row = 2
    for key, value in dict_drink.items():
        ws.write(row, 9, key.name, format_cell)
        ws.write(row, 10, value, format_cell)
        row += 1

    wb.close()
    output.seek(0)
    return output
