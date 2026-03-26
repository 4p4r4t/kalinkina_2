import doctest


class BankAccount:
    def __init__(self, account_number: str, owner_name: str, initial_balance: float = 0.0):
        """
        Создание и подготовка к работе объекта "Банковский счет".

        :param account_number: Уникальный номер счета (идентификатор)
        :param owner_name: ФИО владельца счета
        :param initial_balance: Начальный баланс счета (по умолчанию 0.0)

        Примеры:
        >>> account = BankAccount("40817810000001234567", "Иванов Петр Сергеевич", 1500.50)
        """
        if not isinstance(account_number, str):
            raise TypeError("Номер счета должен быть типа str")
        if not account_number.strip():
            raise ValueError("Номер счета не может быть пустым")
        self.account_number = account_number

        if not isinstance(owner_name, str):
            raise TypeError("Имя владельца должно быть типа str")
        if not owner_name.strip():
            raise ValueError("Имя владельца не может быть пустым")
        self.owner_name = owner_name

        if not isinstance(initial_balance, (int, float)):
            raise TypeError("Начальный баланс должен быть типа int или float")
        if initial_balance < 0:
            raise ValueError("Начальный баланс не может быть отрицательным числом")
        self.balance = float(initial_balance)

    def deposit(self, amount: float) -> None:
        """
        Внесение денежных средств на счет.

        :param amount: Сумма для внесения
        :raise TypeError: Если сумма не является числом
        :raise ValueError: Если сумма отрицательная или равна нулю

        Примеры:
        >>> account = BankAccount("40817810000001234567", "Иванов Петр", 1000.0)
        >>> account.deposit(500.0)
        """
        if not isinstance(amount, (int, float)):
            raise TypeError("Сумма внесения должна быть типа int или float")
        if amount <= 0:
            raise ValueError("Сумма внесения должна быть положительным числом")
        ...

    def withdraw(self, amount: float) -> bool:
        """
        Снятие денежных средств со счета.

        :param amount: Сумма для снятия
        :return: True, если операция выполнена успешно; False, если недостаточно средств
        :raise TypeError: Если сумма не является числом
        :raise ValueError: Если сумма отрицательная или равна нулю

        Примеры:
        >>> account = BankAccount("40817810000001234567", "Иванов Петр", 1000.0)
        >>> account.withdraw(300.0)
        True
        """
        if not isinstance(amount, (int, float)):
            raise TypeError("Сумма снятия должна быть типа int или float")
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть положительным числом")
        return True

    def get_balance(self) -> float:
        """
        Получение текущего баланса счета.

        :return: Текущий баланс в виде числа с плавающей точкой

        Примеры:
        >>> account = BankAccount("40817810000001234567", "Иванов Петр", 5000.0)
        >>> account.get_balance()
        5000.0
        """
        return self.balance


class Book:
    def __init__(self, title: str, author: str, total_pages: int):
        """
        Создание и подготовка к работе объекта "Книга".

        :param title: Название книги
        :param author: Автор книги
        :param total_pages: Общее количество страниц в книге

        Примеры:
        >>> book = Book("Война и мир", "Лев Толстой", 1225)
        """
        if not isinstance(title, str):
            raise TypeError("Название книги должно быть типа str")
        if not title.strip():
            raise ValueError("Название книги не может быть пустым")
        self.title = title

        if not isinstance(author, str):
            raise TypeError("Имя автора должно быть типа str")
        if not author.strip():
            raise ValueError("Имя автора не может быть пустым")
        self.author = author

        if not isinstance(total_pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if total_pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self.total_pages = total_pages
        self.current_page = 0

    def read(self, pages: int) -> None:
        """
        Прочитать указанное количество страниц.

        :param pages: Количество страниц для чтения
        :raise TypeError: Если pages не является целым числом
        :raise ValueError: Если pages отрицательное, равно нулю или превышает оставшееся количество страниц

        Примеры:
        >>> book = Book("1984", "Джордж Оруэлл", 328)
        >>> book.read(50)
        """
        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if pages <= 0:
            raise ValueError("Количество страниц для чтения должно быть положительным числом")
        ...

    def bookmark(self, page: int) -> None:
        """
        Установить закладку на указанной странице.

        :param page: Номер страницы для установки закладки
        :raise TypeError: Если page не является целым числом
        :raise ValueError: Если page вне диапазона от 1 до total_pages

        Примеры:
        >>> book = Book("Мастер и Маргарита", "Михаил Булгаков", 480)
        >>> book.bookmark(156)
        """
        if not isinstance(page, int):
            raise TypeError("Номер страницы должен быть типа int")
        if page < 1 or page > self.total_pages:
            raise ValueError(f"Номер страницы должен быть от 1 до {self.total_pages}")
        ...

    def get_progress(self) -> float:
        """
        Рассчитать процент прочитанного содержимого книги.

        :return: Процент прочитанных страниц (от 0.0 до 100.0)

        Примеры:
        >>> book = Book("Преступление и наказание", "Федор Достоевский", 600)
        >>> book.get_progress()
        0.0
        """
        return 0.0


class SmartLight:
    def __init__(self, brightness: int = 50, color_temperature: int = 4000):
        """
        Создание и подготовка к работе объекта "Умная лампа".

        :param brightness: Уровень яркости (0-100%, по умолчанию 50)
        :param color_temperature: Цветовая температура в Кельвинах (2700-6500K, по умолчанию 4000)

        Примеры:
        >>> lamp = SmartLight(brightness=80, color_temperature=3000)
        """
        if not isinstance(brightness, int):
            raise TypeError("Яркость должна быть типа int")
        if not 0 <= brightness <= 100:
            raise ValueError("Яркость должна быть в диапазоне от 0 до 100")
        self.brightness = brightness

        if not isinstance(color_temperature, int):
            raise TypeError("Цветовая температура должна быть типа int")
        if not 2700 <= color_temperature <= 6500:
            raise ValueError("Цветовая температура должна быть в диапазоне от 2700 до 6500 Кельвинов")
        self.color_temperature = color_temperature
        self.is_on = False

    def set_brightness(self, level: int) -> None:
        """
        Установить уровень яркости освещения.

        :param level: Уровень яркости (0-100)
        :raise TypeError: Если level не является целым числом
        :raise ValueError: Если level вне диапазона 0-100

        Примеры:
        >>> lamp = SmartLight()
        >>> lamp.set_brightness(75)
        """
        if not isinstance(level, int):
            raise TypeError("Уровень яркости должен быть типа int")
        if not 0 <= level <= 100:
            raise ValueError("Уровень яркости должен быть в диапазоне от 0 до 100")
        ...

    def turn_on(self) -> None:
        """
        Включить умную лампу с текущими настройками яркости и температуры.

        Примеры:
        >>> lamp = SmartLight(brightness=60)
        >>> lamp.turn_on()
        """
        ...

    def get_status(self) -> dict:
        """
        Получить текущий статус лампы в виде словаря.

        :return: Словарь с ключами 'is_on', 'brightness', 'color_temperature'

        Примеры:
        >>> lamp = SmartLight(brightness=40, color_temperature=5000)
        >>> lamp.get_status()
        {'is_on': False, 'brightness': 40, 'color_temperature': 5000}
        """
        return {
            'is_on': self.is_on,
            'brightness': self.brightness,
            'color_temperature': self.color_temperature
        }


if __name__ == "__main__":
    doctest.testmod(verbose=True)  # Покажет все проверки