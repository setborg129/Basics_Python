class Orgtech:
    def __init__(self, name, model, price):
        self.name = name
        self.model = model
        self.price = price

    def get_info(self):
        return f"Name: {self.name}, {self.model}, {self.price}"


class Printer(Orgtech):
    def __init__(self, name, model, price, printer_resolution):
        super().__init__(name, model, price)
        self.printer_resolution = printer_resolution

    def get_info(self):
        return super().get_info() + f", Printing Resolution: {self.printer_resolution}"


class Scanner(Orgtech):
    def __init__(self, name, model, price, scanning_resolution):
        super().__init__(name, model, price)
        self.scanning_resolution = scanning_resolution

    def get_info(self):
        return super().get_info() + f", Scanning Resolution: {self.scanning_resolution}"


class Xerox(Orgtech):
    def __init__(self, name, model, price, Xerox_resolution):
        super().__init__(name, model, price)
        self.Xerox_resolution = Xerox_resolution

    def get_info(self):
        return super().get_info() + f", Xerox Resolution: {self.Xerox_resolution}"


organize_pri = Printer('Epson', 'ESP-100', '400 тыс.', '550dp')
print(organize_pri.get_info())

organize_sca = Scanner('ER', 'pole', '200 тыс.', '1dp')
print(organize_sca.get_info())

organize_xer = Xerox('HP', 'LaserJet', '100 тыс.', '110es')
print(organize_xer.get_info())
