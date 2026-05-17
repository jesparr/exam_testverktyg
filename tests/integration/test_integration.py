import pytest
from Bookstore.book_store import BookStore, FavoriteBooks, Book
from Bookstore.book_list import funny_books


@pytest.fixture
def store():
    # Fixture som skapar en butik
    return BookStore()


# --- INTEGRATIONSTESTER ---

@pytest.mark.integration
def test_integration_add_and_toggle_favorite(store):
    # Testar hela flödet, lägg till bok i store -> Toggla som favorrit
    book_data = funny_books[0]  # "Ormar på ett plan"
    store.add_book(book_data["author"], book_data["title"])  # Skapar bok med ID 100

    # Integration: BookStore anropar FavoriteBooks.add() internt
    store.toggle_favorite(100)

    # Kontrollera att boken nu finns i favorit-managerns lista
    assert len(store.favorite_manager.books) == 1
    assert store.favorite_manager.books[0].title == book_data["title"]


@pytest.mark.integration
def test_integration_toggle_on_off(store):
    # Testar att toggle ändrar i favoritebooks
    store.add_book(funny_books[1]["author"], funny_books[1]["title"])  # ID 100

    store.toggle_favorite(100)  # Första anropet: Lägg till
    assert store.favorite_manager.is_favorite(100) is True

    store.toggle_favorite(100)  # Andra anropet: Ta bort
    assert store.favorite_manager.is_favorite(100) is False


@pytest.mark.integration
def test_integration_multiple_books_flow(store):
    # Lägg till tre olika böcker
    store.add_book(funny_books[0]["author"], funny_books[0]["title"])  # 100
    store.add_book(funny_books[1]["author"], funny_books[1]["title"])  # 101
    store.add_book(funny_books[2]["author"], funny_books[2]["title"])  # 102

    # Toggle bara den mellersta boken
    store.toggle_favorite(101)

    assert len(store.favorite_manager.books) == 1
    assert store.favorite_manager.books[0].id == 101  # Kontrollera att rätt ID sparades


@pytest.mark.integration
def test_integration_prevent_duplicates(store):
    # Verifierar hantering av dubletter
    book = store.add_book(funny_books[3]["author"], funny_books[3]["title"])  # ID 100

    # Lägger till boken två gånger
    store.favorite_manager.add(book)
    store.favorite_manager.add(book)

    # Listan ska innehålla ett exemplar
    assert len(store.favorite_manager.books) == 1



@pytest.mark.integration
def test_integration_remain_in_store_after_removing_from_favorites(store):
    # Testar att boken inte försvinner från katalogen när den tas bort som favorit
    store.add_book(funny_books[0]["author"], funny_books[0]["title"])  # 100
    store.toggle_favorite(100)  # Lägg till i favoriter

    # Ta bort från favoriter
    store.toggle_favorite(100)

    # Boken ska vara borta från favoriter finns kvar i katalogen
    assert len(store.favorite_manager.books) == 0
    assert len(store.books) == 1


@pytest.mark.integration
def test_integration_fail_gracefully(store):
    # Testar att inget konstigt händer när man försöker favoritmarkera en bok som inte finns
    store.add_book(funny_books[0]["author"], funny_books[0]["title"])  # ID 100

    # Försök toggla ett ID som inte finns
    store.toggle_favorite(999)

    # Favoritlistan ska fortfarande vara helt opåverkad och tom
    assert len(store.favorite_manager.books) == 0