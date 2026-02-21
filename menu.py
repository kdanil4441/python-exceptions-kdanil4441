from card import Card


class Menu:
    """Класс пользовательского меню."""

    def __init__(self) -> None:
        """Конструктор класса меню."""
        self.__product = Card()

    def print_info(self) -> None:
        print("Выберите действие: \n\n"
              "1) Указать название товара.\n"
              "2) Указать количество товара.\n"
              "3) Указать поставщика товара.\n"
              "4) Указать производителя товара.\n"
              "5) Указать цену товара.\n"
              "6) Указать местоположение товара.\n"
              "7) Указать категорию товара.\n"
              "8) Указать срок годности товара (мес).\n"
              "9) Указать номер товара.\n"
              "10) Указать массу товара.\n"
              "11) Поставить товар на учёт.\n"
              "12) Списать товар с учёта.\n"
              "13) Узнать название товара.\n"
              "14) Узнать количество товара.\n"
              "15) Узнать поставщика товара.\n"
              "16) Узнать производителя товара.\n"
              "17) Узнать цену товара.\n"
              "18) Узнать местоположение товара.\n"
              "19) Узнать категорию товара.\n"
              "20) Узнать срок годности товара (мес.).\n"
              "21) Узнать номер товара.\n"
              "22) Узнать статус товара.\n"
              "23) Узнать массу товара.\n"
              "24) Выход\n"
              )

    def choose(self, choose: str) -> None:
        try:
            choose = int(choose)
        except ValueError:
            print("Введите число")
        else:
            if 0 < choose < 25:
                match choose:
                    case 1:
                        self.__product.set_name(input("Укажите название: "))
                    case 2:
                        self.__product.set_quantity(input("Укажите количество товара: "))
                    case 3:
                        self.__product.set_provider(input("Укажите поставщика товара: "))
                    case 4:
                        self.__product.set_manufacturer(input("Укажите производителя товара: "))
                    case 5:
                        self.__product.set_price(input("Укажите цену товара: "))
                    case 6:
                        self.__product.set_location(input("Укажите местоположение товара: "))
                    case 7:
                        self.__product.set_category(input("Укажите категорию товара: "))
                    case 8:
                        self.__product.set_expiration(input("Укажите срок годности товара (месh   hbhhb): "))
                    case 9:
                        self.__product.set_number(input("Укажите номер товара: "))
                    case 10:
                        self.__product.set_weight(input("Укажите массу товара: "))
                    case 11:
                        self.__product.set_status("состоит на учёте")
                    case 12:
                        self.__product.set_status("списано")
                    case 13:
                        print(self.__product.get_name())
                    case 14:
                        print(self.__product.get_quantity())
                    case 15:
                        print(self.__product.get_provider())
                    case 16:
                        print(self.__product.get_manufacturer())
                    case 17:
                        print(self.__product.get_price())
                    case 18:
                        print(self.__product.get_location())
                    case 19:
                        print(self.__product.get_category())
                    case 20:
                        print(self.__product.get_expiration())
                    case 21:
                        print(self.__product.get_number())
                    case 22:
                        print(self.__product.get_status())
                    case 23:
                        print(self.__product.get_weight())
                    case 24:
                        pass

    def run(self) -> None:
        while True:
            self.print_info()
            choose = input("Ваш выбор: ")
            if choose.strip() == "24":
                print("Программа завершена")
                break
            self.choose(choose)


if __name__ == "__main__":
    menu = Menu()
    menu.run()