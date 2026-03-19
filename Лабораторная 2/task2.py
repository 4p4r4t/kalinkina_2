class Book:
    def __init__(self, id_: int, name: str, pages: int):
        """
        Инициализация книги.
        
        :param id_: Идентификатор книги (используется id_ во избежание конфликта со встроенной функцией id)
        :param name: Название книги
        :param pages: Количество страниц
        """
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        """Возвращает строковое представление для пользователя."""
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        """Возвращает валидную Python-строку для создания экземпляра."""
        return f"Book(id_={self.id}, name={repr(self.name)}, pages={self.pages})"


class Library:
    def __init__(self, books: list[Book] = None):
        """
        Инициализация библиотеки.
        
        :param books: Список книг (по умолчанию None, инициализируется пустым списком)
        """
        # Используем аргумент по умолчанию None для избежания изменяемого дефолта
        if books is None:
            self.books = []
        else:
            self.books = books

    def get_next_book_id(self) -> int:
        """
        Возвращает id для следующей книги.
        Если книг нет — возвращает 1, иначе id последней книги + 1.
        """
        if not self.books:
            return 1
        return self.books[-1].id + 1

    def get_index_by_book_id(self, book_id: int) -> int:
        """
        Возвращает индекс книги в списке по её id.
        
        :param book_id: Идентификатор книги для поиска
        :return: Индекс книги в списке
        :raise ValueError: Если книга с таким id не найдена
        """
        # Используем enumerate для получения пар (индекс, значение)
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")


# Примеры использования:
if __name__ == "__main__":
    # Создаем книги
    book1 = Book(id_=1, name="test_name_1", pages=200)
    book2 = Book(id_=2, name="test_name_2", pages=150)
    
    print(f"Строковое представление: {book1}")  # Книга "test_name_1"
    print(f"Repr: {repr(book1)}")  # Book(id_=1, name='test_name_1', pages=200)
    
    # Создаем библиотеку
    library = Library([book1, book2])
    
    # Получаем следующий id
    print(f"Следующий id: {library.get_next_book_id()}")  # 3
    
    # Получаем индекс по id
    print(f"Индекс книги с id=2: {library.get_index_by_book_id(2)}")  # 1
    
    # Проверяем ошибку
    try:
        library.get_index_by_book_id(999)
    except ValueError as e:
        print(f"Ошибка: {e}")  # Книги с запрашиваемым id не существует
    
    # Пустая библиотека
    empty_library = Library()
    print(f"Следующий id в пустой библиотеке: {empty_library.get_next_book_id()}")  # 1