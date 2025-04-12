class Book:
    material = 'Бумага'
    existing_text = True

    def __init__(self, book_name, book_avtor, page_count, isbn, reserved=False):
        self.book_name = book_name
        self.book_avtor = book_avtor
        self.page_count = page_count
        self.isbn = isbn
        self.reserved = reserved

    def __str__(self):
        reserved_status = 'зарезервировано' if self.reserved else ''
        return (
            f'Название: {self.book_name}, Автор: {self.book_avtor}, '
            f'Страницы: {self.page_count}, ISBN: {self.isbn}'
            + (f', {reserved_status}' if reserved_status else '')
        )


book_one = Book('Идиот', 'Достоевский', 500, '7320-1162', reserved=True)
book_two = Book('Капитанская дочка', 'Пушкин', 161, '2133-2210')
book_three = Book('Война и Мир', 'Толстой', 707, '712837218930')
book_four = Book('Муму', 'Тургенев', 180, '28128-1221')
book_five = Book('Ионыч', ' Чехов', 300, '213123-1232-222111-3123')

books = [book_one, book_two, book_three, book_four, book_five]

for book in books:
    print(book)


class School_book(Book):

    def __init__(self, book_name, book_avtor, page_count, isbn, subject, class_number, exercise, reserved=False):
        super().__init__(book_name, book_avtor, page_count, isbn, reserved)
        self.subject = subject
        self.class_number = class_number
        self.exercise = exercise

    def __str__(self):
        reserved_status = 'зарезервировано' if self.reserved else ''
        return (
            f'Название книги: {self.book_name}, Автор: {self.book_avtor}, Количество страниц: {self.page_count},'
            f'ISBN: {self.isbn} Предмет: {self.subject}, Номер класса: {self.class_number},'
            f' Упражнения: {self.exercise}' + (f', {reserved_status}' if reserved_status else '')
        )


p_one = School_book('Алгебра', 'Малявкин', 123, '123123-123-33',
                    "Математика", 5, True, reserved=True)
p_two = School_book("Биохимия", 'Иванов', 332, '123-223', 'Химия',
                    7, True, reserved=True)
p_three = School_book('Классическая музыка', 'Бах', 254, '1323-8580',
                      "Музыка", 6, False, reserved=False)
p_four = School_book('Родная речь', 'Малыхин', 233, '123-9595-433',
                     "Русский язык", 9, True, reserved=True)
p_five = School_book('На все руки мастер', 'Сильвесторов', 300, '1344-3863-3',
                     "Технология", 8, False, reserved=True)

sch_books = [p_one, p_two, p_three, p_four, p_five]

for sch_book in sch_books:
    print(sch_book)
