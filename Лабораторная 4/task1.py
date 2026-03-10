"""
Модуль реализации иерархии музыкальных инструментов.
Демонстрирует принципы ООП: наследование, инкапсуляция, полиморфизм.
"""

from typing import Optional, List
from abc import ABC, abstractmethod


class MusicalInstrument(ABC):
    """
    Базовый абстрактный класс для всех музыкальных инструментов.

    Определяет общий интерфейс и базовую функциональность для всех
    музыкальных инструментов независимо от их типа.

    Attributes:
        name (str): Название инструмента
        manufacturer (str): Производитель инструмента
        year_made (int): Год изготовления
        _condition (str): Состояние инструмента (инкапсулировано для
            контроля валидности значений через сеттер)
        _is_tuned (bool): Флаг настройки инструмента (инкапсулировано,
            так как изменяется только через метод tune())
    """

    # Допустимые значения состояния инструмента
    VALID_CONDITIONS = ["новый", "отличное", "хорошее", "удовлетворительное", "плохое"]

    def __init__(
            self,
            name: str,
            manufacturer: str,
            year_made: int,
            condition: str = "новый"
    ) -> None:
        """
        Инициализирует музыкальный инструмент.

        Args:
            name: Название инструмента
            manufacturer: Производитель
            year_made: Год изготовления (должен быть положительным)
            condition: Состояние инструмента из VALID_CONDITIONS

        Raises:
            ValueError: Если год отрицательный или состояние недопустимо
        """
        self.name: str = name
        self.manufacturer: str = manufacturer

        if year_made <= 0:
            raise ValueError("Год изготовления должен быть положительным числом")
        self.year_made: int = year_made

        # Инкапсуляция: контроль валидности через сеттер
        self._condition: str = ""
        self.condition = condition  # Используем сеттер для валидации

        # Инкапсуляция: состояние настройки изменяется только через метод tune()
        self._is_tuned: bool = False

    @property
    def condition(self) -> str:
        """Возвращает текущее состояние инструмента."""
        return self._condition

    @condition.setter
    def condition(self, value: str) -> None:
        """
        Устанавливает состояние инструмента с валидацией.

        Args:
            value: Новое состояние из списка VALID_CONDITIONS

        Raises:
            ValueError: Если значение не входит в допустимые
        """
        if value not in self.VALID_CONDITIONS:
            raise ValueError(
                f"Недопустимое состояние '{value}'. "
                f"Допустимые: {', '.join(self.VALID_CONDITIONS)}"
            )
        self._condition = value

    @property
    def is_tuned(self) -> bool:
        """Возвращает True, если инструмент настроен."""
        return self._is_tuned

    def tune(self) -> None:
        """
        Настраивает инструмент.

        Устанавливает флаг _is_tuned в True. Этот метод единственный
        способ изменить состояние настройки (инкапсуляция).
        """
        self._is_tuned = True
        print(f"{self.name} настроен и готов к игре.")

    @abstractmethod
    def play(self) -> str:
        """
        Абстрактный метод воспроизведения звука.

        Должен быть реализован в дочерних классах для специфичного
        звучания каждого типа инструмента.

        Returns:
            str: Описание звука или нотация
        """
        pass

    def get_info(self) -> str:
        """
        Возвращает общую информацию об инструменте.

        Returns:
            str: Форматированная строка с характеристиками
        """
        tune_status = "настроен" if self._is_tuned else "требует настройки"
        return (
            f"{self.name} ({self.manufacturer}, {self.year_made}) - "
            f"состояние: {self._condition}, {tune_status}"
        )

    def __str__(self) -> str:
        """Строковое представление для пользователя."""
        return f"{self.name} от {self.manufacturer} ({self.year_made})"

    def __repr__(self) -> str:
        """Официальное представление для разработчика."""
        return (
            f"{self.__class__.__name__}("
            f"name='{self.name}', "
            f"manufacturer='{self.manufacturer}', "
            f"year_made={self.year_made}, "
            f"condition='{self._condition}')"
        )


class StringInstrument(MusicalInstrument):
    """
    Дочерний класс струнных инструментов.

    Расширяет базовый класс специфичными для струнных инструментов
    атрибутами и методами.

    Attributes:
        number_of_strings (int): Количество струн
        string_material (str): Материал струн
        _current_notes (List[str]): Текущие ноты настройки (инкапсулировано,
            так как изменяется только через методы настройки)
    """

    def __init__(
            self,
            name: str,
            manufacturer: str,
            year_made: int,
            number_of_strings: int,
            string_material: str = "нейлон",
            condition: str = "новый"
    ) -> None:
        """
        Расширяет конструктор базового класса параметрами струнных инструментов.

        Args:
            name: Название инструмента
            manufacturer: Производитель
            year_made: Год изготовления
            number_of_strings: Количество струн (должно быть положительным)
            string_material: Материал струн (по умолчанию "нейлон")
            condition: Состояние инструмента

        Raises:
            ValueError: Если количество струн не положительное
        """
        # Вызываем конструктор родительского класса
        super().__init__(name, manufacturer, year_made, condition)

        if number_of_strings <= 0:
            raise ValueError("Количество струн должно быть положительным числом")
        self.number_of_strings: int = number_of_strings
        self.string_material: str = string_material

        # Инкапсуляция: ноты настройки управляются только через методы класса
        self._current_notes: List[str] = []

    def play(self) -> str:
        """
        Реализация абстрактного метода для струнного инструмента.

        Returns:
            str: Описание звучания струн
        """
        if not self.is_tuned:
            return "Инструмент расстроен! Требуется настройка."
        return f"Звучат {self.number_of_strings} струн из {self.string_material}..."

    def tune(self, notes: Optional[List[str]] = None) -> None:
        """
        Перегружает метод tune() базового класса.

        Причина перегрузки: струнные инструменты требуют специфичной
        настройки по нотам, в отличие от базового флага _is_tuned.
        Сохраняем вызов super() для установки базового флага.

        Args:
            notes: Список нот для настройки каждой струны.
                   Если None, используется стандартный строй.

        Raises:
            ValueError: Если количество нот не совпадает с количеством струн
        """
        # Сначала вызываем базовый метод для установки флага
        super().tune()

        if notes is None:
            # Стандартный строй для большинства струнных
            notes = ["E", "A", "D", "G", "B", "E"][:self.number_of_strings]

        if len(notes) != self.number_of_strings:
            raise ValueError(
                f"Количество нот ({len(notes)}) должно совпадать "
                f"с количеством струн ({self.number_of_strings})"
            )

        self._current_notes = notes
        print(f"Настройка завершена: {', '.join(notes)}")

    def change_strings(self, new_material: str) -> None:
        """
        Меняет струны на новые.

        Args:
            new_material: Материал новых струн

        Side Effects:
            Сбрасывает настройку (устанавливает _is_tuned в False)
        """
        self.string_material = new_material
        self._is_tuned = False  # Сброс флага настройки
        self._current_notes = []
        print(f"Струны заменены на {new_material}. Требуется настройка.")

    # Унаследованный метод get_info() используется без изменений

    def __str__(self) -> str:
        """Расширяет строковое представление данными о струнах."""
        base = super().__str__()
        return f"{base}, {self.number_of_strings}-струнный"

    def __repr__(self) -> str:
        """Расширяет repr данными о струнах."""
        base_repr = super().__repr__().rstrip(")")
        return (
            f"{base_repr}, "
            f"number_of_strings={self.number_of_strings}, "
            f"string_material='{self.string_material}')"
        )


class KeyboardInstrument(MusicalInstrument):
    """
    Дочерний класс клавишных инструментов.

    Расширяет базовый класс специфичными для клавишных инструментов
    атрибутами и методами.

    Attributes:
        number_of_keys (int): Количество клавиш
        has_pedals (bool): Наличие педалей
        _volume_level (int): Уровень громкости 0-100 (инкапсулировано
            для контроля диапазона значений)
    """

    MAX_VOLUME = 100
    MIN_VOLUME = 0

    def __init__(
            self,
            name: str,
            manufacturer: str,
            year_made: int,
            number_of_keys: int,
            has_pedals: bool = True,
            condition: str = "новый"
    ) -> None:
        """
        Расширяет конструктор базового класса параметрами клавишных инструментов.

        Args:
            name: Название инструмента
            manufacturer: Производитель
            year_made: Год изготовления
            number_of_keys: Количество клавиш (обычно 61, 76 или 88)
            has_pedals: Наличие педалей sustain/soft
            condition: Состояние инструмента
        """
        super().__init__(name, manufacturer, year_made, condition)
        self.number_of_keys: int = number_of_keys
        self.has_pedals: bool = has_pedals

        # Инкапсуляция: контроль диапазона через property
        self._volume_level: int = 50  # Средняя громкость по умолчанию

    @property
    def volume_level(self) -> int:
        """Возвращает текущий уровень громкости."""
        return self._volume_level

    @volume_level.setter
    def volume_level(self, value: int) -> None:
        """
        Устанавливает уровень громкости с ограничением диапазона.

        Args:
            value: Желаемый уровень громкости (0-100)
        """
        self._volume_level = max(self.MIN_VOLUME, min(self.MAX_VOLUME, value))

    def play(self) -> str:
        """
        Реализация абстрактного метода для клавишного инструмента.

        Returns:
            str: Описание звучания клавиш
        """
        if not self.is_tuned:
            return "Инструмент не откалиброван!"

        pedal_info = "с педалями" if self.has_pedals else "без педалей"
        return (
            f"Звучат {self.number_of_keys} клавиш {pedal_info} "
            f"(громкость: {self._volume_level}%)..."
        )

    def tune(self) -> None:
        """
        Перегружает метод tune() базового класса.

        Причина перегрузки: клавишные инструменты требуют калибровки
        механизма (фортепиано) или электроники (синтезатор), а не
        настройки в классическом смысле. Сохраняем базовое поведение
        через super(), но добавляем специфичную логику.
        """
        super().tune()

        # Специфичная для клавишных логика калибровки
        if "фортепиано" in self.name.lower() or "пианино" in self.name.lower():
            print("Калибровка молоточкового механизма выполнена.")
        else:
            print("Электронная калибровка завершена.")

    def adjust_volume(self, delta: int) -> None:
        """
        Изменяет громкость на указанную величину.

        Args:
            delta: Изменение громкости (может быть отрицательным)
        """
        self.volume_level += delta  # Используем сеттер с валидацией

    # Унаследованный метод get_info() используется без изменений

    def __str__(self) -> str:
        """Расширяет строковое представление данными о клавишах."""
        base = super().__str__()
        pedal_str = "с педалями" if self.has_pedals else "без педалей"
        return f"{base}, {self.number_of_keys} клавиш {pedal_str}"

    def __repr__(self) -> str:
        """Расширяет repr данными о клавишах."""
        base_repr = super().__repr__().rstrip(")")
        return (
            f"{base_repr}, "
            f"number_of_keys={self.number_of_keys}, "
            f"has_pedals={self.has_pedals})"
        )


# ============== ДЕМОНСТРАЦИЯ РАБОТЫ ==============

if __name__ == "__main__":
    # Создаем экземпляры
    guitar = StringInstrument(
        name="Fender Stratocaster",
        manufacturer="Fender",
        year_made=2020,
        number_of_strings=6,
        string_material="сталь"
    )

    piano = KeyboardInstrument(
        name="Yamaha Grand Piano",
        manufacturer="Yamaha",
        year_made=2019,
        number_of_keys=88,
        has_pedals=True
    )

    # Демонстрация __str__
    print(f"Струнный: {guitar}")
    print(f"Клавишный: {piano}")
    print()

    # Демонстрация __repr__
    print(f"Repr guitar: {repr(guitar)}")
    print(f"Repr piano: {repr(piano)}")
    print()

    # Демонстрация унаследованного метода get_info()
    print("=== Унаследованный метод get_info() ===")
    print(guitar.get_info())
    print(piano.get_info())
    print()

    # Демонстрация перегруженного метода tune()
    print("=== Перегруженный метод tune() ===")
    guitar.tune(["E", "A", "D", "G", "B", "E"])  # С нотами
    piano.tune()  # Без параметров (калибровка)
    print()

    # Демонстрация play()
    print("=== Метод play() ===")
    print(guitar.play())
    print(piano.play())
    print()

    # Демонстрация инкапсуляции
    print("=== Инкапсуляция ===")
    print(f"Состояние гитары: {guitar.condition}")
    try:
        guitar.condition = "сломанный"  # Вызовет ошибку
    except ValueError as e:
        print(f"Ошибка валидации: {e}")

    # Изменение громкости пианино
    print(f"Громкость пианино: {piano.volume_level}")
    piano.adjust_volume(30)
    print(f"После увеличения: {piano.volume_level}")
    piano.adjust_volume(50)  # Попытка превысить 100
    print(f"После попытки превысить максимум: {piano.volume_level}")