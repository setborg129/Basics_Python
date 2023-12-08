# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Запрашивать у пользователя данные и заполнять список необходимо
# только числами. Класс-исключение должен контролировать типы данных элементов списка.

class exception:
    def control_type(self):
        number_list = []
        while True:
            try:
                data_list = input('Введите число (для выходна введите stop):')
                if data_list.lower() == 'stop':
                    break
                number_list.append(int(data_list))
            except:
                print('Ошибка, введите только числа !')
        print(number_list)

int_list = exception()
int_list.control_type()
