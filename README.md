# qa_python
В настоящем проекте были проведены следующие проверки методов:
    add_new_book
        - книги с названием от 1 до 40 символов добавляются
        - книга с названием в 41 и 42 символа не добавляется
        - без названия книга не добавляется
    set_book_genre
        - книге устанавливается жанр из списка
        - книге не устанавливается жанр не из списка
    get_book_genre
        - на верное получение жанра по имени книги
    get_books_with_specific_genre
        - книги с определенным жанром добавились в список
    get_books_genre
        - на верное получение текущего словаря books_genre
    get_books_for_children
        - книги с возрастным рейтингом не добавляются в список книг для детей
    add_book_in_favorites
        - одну книгу нельзя дважды добавить в Избранное
    delete_book_from_favorites
        - книга удаляется из Избранного
    get_list_of_favorites_books
        - на верное получение текущего списка Избранных книг

=============================================================================== test session starts ===============================================================================
platform win32 -- Python 3.13.3, pytest-8.3.5, pluggy-1.5.0 -- C:\Users\drovi\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\drovi\qa_python
plugins: cov-6.1.1
collected 22 items                                                                                                                                                                 

tests.py::TestBooksCollector::test_add_new_book_add_two_books PASSED                                                                                                         [  4%]
tests.py::TestBooksCollector::test_add_new_book_len_name_between_0_and_41_added[1] PASSED                                                                                    [  9%]
tests.py::TestBooksCollector::test_add_new_book_len_name_between_0_and_41_added[12] PASSED                                                                                   [ 13%]
tests.py::TestBooksCollector::test_add_new_book_len_name_between_0_and_41_added[123456789012345678901234567890123456789] PASSED                                              [ 18%] 
tests.py::TestBooksCollector::test_add_new_book_len_name_between_0_and_41_added[1234567890123456789012345678901234567890] PASSED                                             [ 22%]
tests.py::TestBooksCollector::test_add_new_book_len_name_more_then_40_not_added[12345678901234567890123456789012345678901] PASSED                                            [ 27%] 
tests.py::TestBooksCollector::test_add_new_book_len_name_more_then_40_not_added[123456789012345678901234567890123456789012] PASSED                                           [ 31%] 
tests.py::TestBooksCollector::test_add_new_book_name_empty_not_added PASSED                                                                                                  [ 36%] 
tests.py::TestBooksCollector::test_set_book_genre_when_genre_in_list_added[\u0424\u0430\u043d\u0442\u0430\u0441\u0442\u0438\u043a\u0430] PASSED                              [ 40%] 
tests.py::TestBooksCollector::test_set_book_genre_when_genre_in_list_added[\u0423\u0436\u0430\u0441\u044b] PASSED                                                            [ 45%] 
tests.py::TestBooksCollector::test_set_book_genre_when_genre_in_list_added[\u0414\u0435\u0442\u0435\u043a\u0442\u0438\u0432\u044b] PASSED                                    [ 50%] 
tests.py::TestBooksCollector::test_set_book_genre_when_genre_in_list_added[\u041c\u0443\u043b\u044c\u0442\u0444\u0438\u043b\u044c\u043c\u044b] PASSED                        [ 54%] 
tests.py::TestBooksCollector::test_set_book_genre_when_genre_in_list_added[\u041a\u043e\u043c\u0435\u0434\u0438\u0438] PASSED                                                [ 59%] 
tests.py::TestBooksCollector::test_set_book_genre_when_genre_not_in_list_not_added PASSED                                                                                    [ 63%] 
tests.py::TestBooksCollector::test_get_book_genre_name_true PASSED                                                                                                           [ 68%] 
tests.py::TestBooksCollector::test_get_books_with_specific_genre_when_genre_added PASSED                                                                                     [ 72%] 
tests.py::TestBooksCollector::test_get_books_genre_true PASSED                                                                                                               [ 77%]
tests.py::TestBooksCollector::test_get_books_for_children_genre_age_rating_not_added[\u0423\u0436\u0430\u0441\u044b] PASSED                                                  [ 81%] 
tests.py::TestBooksCollector::test_get_books_for_children_genre_age_rating_not_added[\u0414\u0435\u0442\u0435\u043a\u0442\u0438\u0432\u044b] PASSED                          [ 86%] 
tests.py::TestBooksCollector::test_add_book_in_favorites_one_name_not_add_twice PASSED                                                                                       [ 90%] 
tests.py::TestBooksCollector::test_delete_book_from_favorites_name_removed PASSED                                                                                            [ 95%] 
tests.py::TestBooksCollector::test_get_list_of_favorites_books_true PASSED                                                                                                   [100%] 

=============================================================================== 22 passed in 0.06s ================================================================================ 
