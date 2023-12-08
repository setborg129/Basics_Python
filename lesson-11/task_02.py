# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем. При вводе нуля в
# качестве делителя программа должна корректно обработать эту ситуацию и не
# завершиться с ошибкой.


class exceptions:
    def __init__(self, first_num=10, second_num=0):
        self.first_num = first_num
        self.second_num = second_num

    def divisions(self):
        try:
            print(f"Результат деления: {int(self.first_num / self.second_num)}")
        except ZeroDivisionError as ex:
            print(f"Ошибка - {ex}, Деление на ноль недопустимо")


num_first = int(input("Введите делимое число: "))
num_second = int(input("Введите делитель: "))
div = exceptions(num_first, num_second)
div.divisions()
