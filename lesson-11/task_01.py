# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен извлекать
# число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить
# валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры
# на реальных данных.
from typing import Any, Generator


class Number(int):
    def __str__(self):
        return f'{self:02}'


class Data:
    def __init__(self, date: str, /):
        fragments = date.split('-')
        self.day, self.month, self.year = self.Number_data(fragments)
        if self.validate_day(self.day) and self.validate_month(self.month) and self.validate_year(self.year):
            print(f"Дата {date} валинда")
        else:
            print(f"Дата {date} не валинда")

    @classmethod
    def Number_data(cls, date: list[str]) -> Generator[int, Any, None]:
        return (int(i) for i in date)

    @staticmethod
    def validate_day(day):
        if 1 <= day <= 31:
            return True
        else:
            return False


    @staticmethod
    def validate_month(mouth):
        if 1 <= mouth <= 12:
            return True
        else:
            return False

    @staticmethod
    def validate_year(year):
        if 1900 <= year <= 2023:
            return True
        else:
            return False


if __name__ == '__main__':
    for data in ('01-11-2023', '02-01-1421', '01-11-2022'):
        try:
            Data(data)
        except TypeError as e:
            print(f'Ошибка = {e}')
