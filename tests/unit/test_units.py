import pytest
from Bookstore.book_store import BookStore, FavoriteBooks, Book
from Bookstore.book_list import funny_books


# --- FIXTURES ---

@pytest.fixture
# En ny bookstore skapas inför varje testfunktion och nollställer listan och sätter ID till 100
def store():
    return BookStore()


@pytest.fixture
def fav_manager():
    return FavoriteBooks()


@pytest.fixture
def sample_book():
    # Skapar ett bookobjekt baserat på första objektet i funny_books listan
    data = funny_books[0]
    return Book(data["id"], data["title"], data["author"])


# --- BOOKSTORE TESTER ---

@pytest.mark.unit
def test_add_book_from_list(store):
    # Testar att lägga till första boken i listan, 'Ormar på ett plan'
    book_data = funny_books[0]  # Ormar på ett plan
    book = store.add_book(book_data["author"], book_data["title"])

    assert book.id == 100                   # Assert på att första boken blir id 100
    assert book.title == book_data["title"] # Kontrollera att titeln sparats
    assert len(store.books) == 1            # Assert på att boken lagts till i listan

@pytest.mark.unit
def test_toggle_favorite_cycle(store):
    # Testar att det går att toggla favoritböcker (lägg till/ta bort)
    store.add_book(funny_books[0]["author"], funny_books[0]["title"])  # 100
    store.add_book(funny_books[1]["author"], funny_books[1]["title"])  # 101
    book_data = funny_books[5]  # Git Blame (vi simulerar att den blir nr 3 i kön)
    book = store.add_book(book_data["author"], book_data["title"])  # 102

    # Toggle PÅ
    assert store.toggle_favorite(102) is True
    assert store.favorite_manager.is_favorite(102) is True

    # Toggle AV
    assert store.toggle_favorite(102) is True
    assert store.favorite_manager.is_favorite(102) is False

@pytest.mark.unit
def test_toggle_non_existent_book(store):
    # Test att toggla en boks id som inte finns ännu
    # Stack Overflow-boken har ID 111 i listan, men
    result = store.toggle_favorite(111)
    assert result is False


# --- TESTER FÖR FAVORITEBOOKS (4 ST) ---
@pytest.mark.unit
def test_fav_add_book(fav_manager, sample_book):
    # Testar att lägga till en bok i favoriter
    fav_manager.add(sample_book)
    assert len(fav_manager.books) == 1
    assert fav_manager.is_favorite(sample_book.id)

@pytest.mark.unit
def test_fav_add_duplicate(fav_manager, sample_book):
    # Testar att lägga till samam bok två ggr
    fav_manager.add(sample_book)
    fav_manager.add(sample_book)  # Försöker lägga till samma bok igen
    assert len(fav_manager.books) == 1 # Assertar att det endast finns 1 bok

@pytest.mark.unit
def test_fav_remove_book(fav_manager, sample_book):
    # Testar att ta bort en bok som är satt som favorit
    fav_manager.add(sample_book)
    fav_manager.remove(sample_book)
    assert len(fav_manager.books) == 0
    assert not fav_manager.is_favorite(sample_book.id)