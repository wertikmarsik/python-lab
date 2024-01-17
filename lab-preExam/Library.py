
import csv

class Book:
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published

    def display_info(self):
        print(f"Титулка: {self.title}, Автор: {self.author}, Рік видання: {self.year_published}")

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_book(self, keyword, search_by='title'):
        found_books = []
        for book in self.books:
            if search_by == 'title' and keyword.lower() in book.title.lower():
                found_books.append(book)
            elif search_by == 'author' and keyword.lower() in book.author.lower():
                found_books.append(book)
        return found_books

    def display_all_books(self):
        for book in self.books:
            book.display_info()

    def import_books_from_csv(self, filename):
        try:
            with open(filename, 'r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) == 3:
                        title, author, year_published = row
                        book = Book(title, author, year_published)
                        self.add_book(book)
        except FileNotFoundError:
            print(f"Помилка '{filename}' не найдено.")
        except Exception as e:
            print(f"Помилка імпортації книжки: {e}")

    def export_books_to_csv(self, filename='library.csv'):
        try:
            with open(filename, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                for book in self.books:
                    writer.writerow([book.title, book.author, book.year_published])
            print(f"Інформацію бібліотеки додано {filename} успішно.")
        except Exception as e:
            print(f"Помилка експорту книги: {e}")

library = Library()

book1 = Book("Курс пайтона", "Семен Оскерко", 2023)
book2 = Book("КК України", "Україна", 1998)
library.add_book(book1)
library.add_book(book2)

library.import_books_from_csv('books.csv')


library.display_all_books()

found_books = library.find_book('Семен Оскерко', search_by='author')
print("\nКнигу Семена Оскерка найдено:")
for book in found_books:
    book.display_info()

library.export_books_to_csv()

