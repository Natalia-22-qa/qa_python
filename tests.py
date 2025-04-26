import pytest


from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()



    # переменная со списком доступных жанров
    genre = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
    # переменная со списком книг с возрастным рейтингом
    genre_age_rating = ['Ужасы', 'Детективы']

    # проверка add_new_book, что книги с названием от 1 до 40 символов добавляются
    @pytest.mark.parametrize('book_name', ['1',
                                           '12',
                                           '123456789012345678901234567890123456789',
                                           '1234567890123456789012345678901234567890'])
    def test_add_new_book_len_name_between_0_and_41_added(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert book_name in collector.books_genre

    # проверка add_new_book, что книга с названием в 41 и 42 символа не добавляется
    @pytest.mark.parametrize('book_name', ['12345678901234567890123456789012345678901',
                                           '123456789012345678901234567890123456789012'])
    def test_add_new_book_len_name_more_then_40_not_added(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert len(collector.get_books_genre()) == 0

    # проверка add_new_book, что без названия книга не добавляется
    def test_add_new_book_name_empty_not_added(self):
        collector = BooksCollector()
        collector.add_new_book('')
        assert len(collector.get_books_genre()) == 0

    # проверка set_book_genre, что книге устанавливается жанр из списка
    @pytest.mark.parametrize('book_genre', genre)
    def test_set_book_genre_when_genre_in_list_added(self, book_genre):
        collector = BooksCollector()
        collector.books_genre = {'Название книги': ''}
        collector.set_book_genre('Название книги', book_genre)
        assert collector.books_genre['Название книги'] == book_genre

    # проверка set_book_genre, что книге не устанавливается жанр не из списка
    def test_set_book_genre_when_genre_not_in_list_not_added(self):
        collector = BooksCollector()
        collector.books_genre = {'Эрагон': ''}
        collector.set_book_genre('Эрагон', 'Фэнтези')
        assert collector.books_genre['Эрагон'] == ''

    # проверка get_book_genre на верное получение жанра по имени книги
    def test_get_book_genre_name_true(self):
        collector = BooksCollector()
        collector.add_new_book('Мгла')
        collector.set_book_genre('Мгла', 'Ужасы')
        assert collector.get_book_genre('Мгла') == 'Ужасы'

    # проверка get_books_with_specific_genre, что книги с определенным жанром добавились в список
    def test_get_books_with_specific_genre_when_genre_added(self):
        collector = BooksCollector()
        collector.books_genre = {'Мгла': 'Ужасы',
                                 'Маугли': 'Мультфильмы',
                                 'Чужой': 'Ужасы',
                                 'Граф Аверин': 'Детективы',
                                 'Оно': 'Ужасы'}
        assert len(collector.get_books_with_specific_genre('Ужасы')) == 3

    # проверка get_books_genre на верное получение текущего словаря books_genre
    def test_get_books_genre_true(self):
        collector = BooksCollector()
        collector.books_genre = {'Мгла': 'Ужасы',
                                 'Маугли': 'Мультфильмы',
                                 'Граф Аверин': 'Детективы'}
        assert list(collector.get_books_genre()) == list(collector.books_genre)

    # проверка get_books_for_children, что книги с возрастным рейтингом не добавляются в список книг для детей
    @pytest.mark.parametrize('genre', genre_age_rating)
    def test_get_books_for_children_genre_age_rating_not_added(self, genre):
        collector = BooksCollector()
        collector.books_genre = {'Название книги': ''}
        collector.set_book_genre('Название книги', genre)
        assert len(collector.get_books_for_children()) == 0

    # проверка add_book_in_favorites, что одну книгу нельзя дважды добавить в Избранное
    def test_add_book_in_favorites_one_name_not_add_twice(self):
        collector = BooksCollector()
        collector.books_genre = {'Мгла': 'Ужасы',
                                 'Маугли': 'Мультфильмы',
                                 'Граф Аверин': 'Детективы'}
        collector.add_book_in_favorites('Граф Аверин')
        collector.add_book_in_favorites('Граф Аверин')
        assert len(collector.favorites) == 1

    # проверка delete_book_from_favorites, что книга удаляется из Избранного
    def test_delete_book_from_favorites_name_removed(self):
        collector = BooksCollector()
        collector.books_genre = {'Мгла': 'Ужасы',
                                 'Маугли': 'Мультфильмы',
                                 'Граф Аверин': 'Детективы'}
        collector.favorites = ['Мгла', 'Граф Аверин', 'Оно']
        collector.delete_book_from_favorites('Граф Аверин')
        assert 'Граф Аверин' not in collector.favorites and len(collector.favorites) == 2

    # проверка get_list_of_favorites_books на верное получение текущего списка Избранных книг
    def test_get_list_of_favorites_books_true(self):
        collector = BooksCollector()
        collector.favorites = ['Мгла', 'Граф Аверин', 'Оно']
        assert list(collector.get_list_of_favorites_books()) == collector.favorites