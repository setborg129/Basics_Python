# 6. Продолжить работу над вторым заданием.
# Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

class Orgtech:
    def __init__(self, serial=None, name=None, model=None, price=None, count=None):
        self.serial = serial
        self.name = name
        self.model = model
        self.price = price
        self.count = count
        self.items = {}
        self.company = {}

    def get_info(self):
        return f"Name: {self.items.items()}"

    def add_item(self, serial, name, model, price):
        "'"
        global result
        "Передаем технику на склад"
        while True:
            try:
                result = int(input("Введите количество едениц техники: "))
                if type(result) != int and result <= 0:
                    print("Некорректное количество")
                    continue
                else:
                    break
            except TypeError:
                print("Введите количество едениц типа Int(число)")
                continue
            except ValueError:
                print("Введите количество едениц типа Int(число)")
                continue
        self.items[serial] = {
            'Name Printer:', name,
            'Model:', model,
            'Цена:', price,
            'Количество:', result,
        }

        print(f"Передали на склад: Серийный номер: {serial}, Имя: {name}, Модель:{model}, "
          f"Цена:{price}, Колличество: {result} \n")


    def get_items_count(self):
        "'"
        "Получаем полный список техники которая находится на складе"
        return f"На складе: {len(self.items)} ед. "


    def remove_item(self, serial_number: str):
        "'"
        "Удаляем технику со склада для передачи."
        try:
            for org in self.items:
                if (org == serial_number):
                    self.items.pop(serial_number)
                    print(f"удалили со склада технику с серийным номером:  {serial_number}")
            print(f'Нет техники на складе с серийным номером: {serial_number}')

        except RuntimeError as Ex:
            f'Ошибка = {Ex}'


    def to_company(self, serial_number, name_company):
        ''''''
        " Передаем технику компании "
        try:
            for to in self.items:
                if (to == serial_number):
                    self.items.pop(serial_number)

                    self.company[serial_number] = {
                        'Name Printer', self.name,
                        'Model', self.model,
                        'Цена', self.price,
                        'Количество', self.count,
                        'company', name_company
                    }
                    print(f'Передали компании "{name_company}" со склада технику с серийным номером: {serial_number}')
        except:
            pass


class Printer(Orgtech):
    def __init__(self, serial=None, name=None, model=None, price=None, printer_resolution=None):
        super().__init__(serial=None, name=None, model=None, price=None)
        self.printer_resolution = printer_resolution

    def get_info(self):
        return super().get_info() + f", Printing Resolution: {self.printer_resolution}"


class Scanner(Orgtech):
    def __init__(self, serial=None, name=None, model=None, price=None, scanning_resolution=None):
        super().__init__(serial, name, model, price)
        self.scanning_resolution = scanning_resolution

    def get_info(self):
        return super().get_info() + f", Scanning Resolution: {self.scanning_resolution}"


class Xerox(Orgtech):
    def __init__(self, serial=None, name=None, model=None, price=None, Xerox_resolution=None):
        super().__init__(serial=None, name=None, model=None, price=None)
        self.Xerox_resolution = Xerox_resolution

    def get_info(self):
        return super().get_info() + f", Xerox Resolution: {self.Xerox_resolution}"


organize_pri1 = Printer()

organize_pri1.add_item('75233412', 'Epson', 'ESP-100', '400 тыс.')
organize_pri1.add_item('55264152', 'HP', 'LJ', '50 тыс.')
organize_pri1.add_item('55264153', 'HP', 'LJ', '50 тыс.')
print(organize_pri1.get_items_count())
organize_pri1.remove_item('55264152')
print(organize_pri1.get_items_count())
organize_pri1.to_company('75233412', 'Газпром')
print(organize_pri1.get_items_count())
