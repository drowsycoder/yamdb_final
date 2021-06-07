from datetime import datetime as dt

from django.core.exceptions import ValidationError


def year_validator(year):
    """Проверяет значение года для произведения.

    Предполагается, что оно датировано с -1000 г. до н.э. по текущий год.
    """
    if year < -1000 or year > dt.now().year:
        raise ValidationError(f'{year} не является корректным значением года!',
                              params={'value': year}, )
