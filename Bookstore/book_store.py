class Book:
    def __init__(self, book_id, title, author):
        self.id = book_id
        self.title = title
        self.author = author

class BookStore:
    def __init__(self):
        self.books = []
        self.favorite_manager = FavoriteBooks()
        self._next_id = 100

    def add_book(self, author, title):
        new_book = Book(self._next_id, title, author)
        self.books.append(new_book)
        self._next_id += 1
        return new_book

    def toggle_favorite(self, book_id):
        book = next((b for b in self.books if b.id == book_id), None)
        if not book:
            return False

        if self.favorite_manager.is_favorite(book_id):
            self.favorite_manager.remove(book)
        else:
            self.favorite_manager.add(book)
        return True


class FavoriteBooks:
    def __init__(self):
        self.books = []

    def add(self, book):
        if book not in self.books:
            self.books.append(book)

    def remove(self, book):
        if book in self.books:
            self.books.remove(book)

    def is_favorite(self, book_id):
        # Hjälpmetod för att kolla om ett ID finns i favoritlistan
        return any(b.id == book_id for b in self.books)

