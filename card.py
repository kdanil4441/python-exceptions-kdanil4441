class Card:
    """Класс карточек."""

    def __init__(self) -> None:
        """Конструктор класса Card."""
        self.__name = None
        self.__quantity = None
        self.__status = "в обработке"
        self.__provider = None
        self.__manufacturer = None
        self.__price = None
        self.__location = None
        self.__category = None
        self.__weight = None
        self.__expiration = None
        self.__number = None

    def set_name(self, name: str) -> None:
        """Сеттер названия товара.

        Args:
            name: Название товара.
        """
        self.__name = name
        print("Название успешно указано\n")

    def set_quantity(self, quantity: str) -> None:
        """Сеттер количества товара.

        Args:
            quantity: Количество товара.
        """
        try:
            if int(quantity) >= 0:
                self.__quantity = quantity
                print("Количество успешно указано\n")
            else:
                print("Введено некорректное значение\n")
        except ValueError:
            print("Введите целое число\n")

    def set_status(self, status: str) -> None:
        """Сеттер состояния товара.

        Args:
            status: Состояние товара.
        """
        if status == "списано":
            if self.__status == "состоит на учёте":
                self.__status = status
                print("Успешно списано\n")
            else:
                print("Товар не числится на учёте\n")
        else:
            self.__status = status
            print("Статус успешно изменён\n")

    def set_provider(self, provider: str) -> None:
        """Сеттер поставщика товара.

        Args:
            provider: Поставщик товара.
        """
        self.__provider = provider
        print("Поставщик успешно указан\n")

    def set_manufacturer(self, manufacturer: str) -> None:
        """Сеттер производителя товара.

        Args:
            manufacturer: Производитель товара.
        """
        self.__manufacturer = manufacturer
        print("Производитель успешно указан\n")

    def set_price(self, price: str) -> None:
        """Сеттер цены товара.

        Args:
            price: Цена товара.
        """
        try:
            if int(price) > 0:
                self.__price = price
                print("Цена успешно указана\n")
            else:
                print("Введено некорректное значение\n")
        except ValueError:
            print("Введите целое число\n")

    def set_location(self, location: str) -> None:
        """Сеттер местоположения товара.

        Args:
            location: Местоположение товара.
        """
        self.__location = location
        print("Местоположение успешно указано\n")

    def set_category(self, category: str) -> None:
        """Сеттер категории товара.

        Args:
            category: Категория товара.
        """
        self.__category = category
        print("Категория успешно указана\n")

    def set_weight(self, weight: str) -> None:
        """Сеттер массы товара.

        Args:
            weight: Масса товара.
        """
        try:
            if int(weight) > 0:
                self.__weight = weight
                print("Вес успешно указан\n")
            else:
                print("Введено некорректное значение\n")
        except ValueError:
            print("Введите целое число\n")

    def set_expiration(self, expiration: str) -> None:
        """Сеттер срока годности товара.

        Args:
            expiration: Срок годности товара (в месяцах).
        """
        try:
            if int(expiration) > 0:
                self.__expiration = expiration
                print("Срок годности успешно указан\n")
            else:
                print("Введено некорректное значение\n")
        except ValueError:
            print("Введите целое число\n")

    def set_number(self, number: str) -> None:
        """Сеттер номера товара.

        Args:
            number: Номер товара.
        """
        self.__number = number
        print("Номер успешно указан\n")

    def get_name(self) -> str:
        """Геттер названия товара.

        Returns:
            name: Название товара.
        """
        return self.__name

    def get_quantity(self) -> int:
        """Геттер количества товара.

        Returns:
            quantity: Количество товара.
        """
        return self.__quantity

    def get_status(self) -> str:
        """Геттер состояния товара.

        Returns:
            status: Состояние товара.
        """
        return self.__status

    def get_provider(self) -> str:
        """Геттер поставщика товара.

        Returns:
            provider: Поставщик товара.
        """
        return self.__provider

    def get_manufacturer(self) -> str:
        """Геттер производителя товара.

        Returns:
            manufacturer: Производитель товара.
        """
        return self.__manufacturer

    def get_price(self) -> int:
        """Геттер цены товара.

        Returns:
            price: Цена товара.
        """
        return self.__price

    def get_location(self) -> str:
        """Геттер местоположения товара.

        Returns:
            location: Местоположение товара.
        """
        return self.__location

    def get_category(self) -> str:
        """Геттер категории товара.

        Returns:
            category: Категория товара.
        """
        return self.__category

    def get_weight(self) -> int:
        """Геттер массы товара.

        Returns:
            weight: Масса товара.
        """
        return self.__weight

    def get_expiration(self) -> int:
        """Геттер срока годности товара.

        Returns:
            expiration: Срок годности товара (в месяцах).
        """
        return self.__expiration

    def get_number(self) -> int:
        """Геттер номера товара.

        Returns:
            number: Номер товара.
        """
        return self.__number