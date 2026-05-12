import pytest
# Importerar klasserna och din specifika boklista
from Bookstore.book_store import BookStore, FavoriteBooks, Book
from Bookstore.book_list import funny_books


@pytest.fixture
def store():
    """Fixture som skapar en butik. Denna har redan en FavoriteBooks-instans inuti sig."""
    return BookStore()


# --- INTEGRATIONSTESTER ---

@pytest.mark.integration
def test_integration_add_and_toggle_favorite(store):
    """1. Testar hela kedjan: Lägg till bok i store -> Toggle till favorit."""
    book_data = funny_books[0]  # "Ormar på ett plan"
    store.add_book(book_data["author"], book_data["title"])  # Skapar bok med ID 100

    # Integration: BookStore anropar FavoriteBooks.add() internt
    store.toggle_favorite(100)

    # Vi kontrollerar att boken nu finns i favorit-managerns lista
    assert len(store.favorite_manager.books) == 1
    assert store.favorite_manager.books[0].title == book_data["title"]


@pytest.mark.integration
def test_integration_toggle_on_off(store):
    """2. Testar att 'toggle' faktiskt växlar tillståndet i FavoriteBooks-objektet."""
    store.add_book(funny_books[1]["author"], funny_books[1]["title"])  # ID 100

    store.toggle_favorite(100)  # Första anropet: Lägg till
    assert store.favorite_manager.is_favorite(100) is True

    store.toggle_favorite(100)  # Andra anropet: Ta bort
    assert store.favorite_manager.is_favorite(100) is False


@pytest.mark.integration
def test_integration_multiple_books_flow(store):
    """3. Testar att rätt bok hanteras när vi har flera böcker i systemet."""
    # Lägg till tre olika böcker
    store.add_book(funny_books[0]["author"], funny_books[0]["title"])  # 100
    store.add_book(funny_books[1]["author"], funny_books[1]["title"])  # 101
    store.add_book(funny_books[2]["author"], funny_books[2]["title"])  # 102

    # Toggle bara den mellersta boken
    store.toggle_favorite(101)

    assert len(store.favorite_manager.books) == 1
    assert store.favorite_manager.books[0].id == 101  # Kontrollera att rätt ID sparades


@pytest.mark.integration
def test_integration_prevent_duplicates_via_store(store):
    """4. Verifierar att FavoriteBooks logik förhindrar dubbletter även när anropet kommer från Store."""
    book = store.add_book(funny_books[3]["author"], funny_books[3]["title"])  # ID 100

    # Vi simulerar ett scenario där FavoriteBooks på något sätt redan har boken
    store.favorite_manager.add(book)

    # Om vi nu kör toggle_favorite(100) ska den hitta boken i favoriter och TA BORT den
    store.toggle_favorite(100)

    assert len(store.favorite_manager.books) == 0


@pytest.mark.integration
def test_integration_id_consistency(store):
    """5. Testar att ID:t som skapas av Store är det som FavoriteBooks använder för sökning."""
    book_data = funny_books[10]  # "My First Regex"
    new_book = store.add_book(book_data["author"], book_data["title"])  # Får ID 100

    store.toggle_favorite(100)

    # Kontrollera att is_favorite faktiskt hittar det ID som Store genererade
    assert store.favorite_manager.is_favorite(new_book.id) is True


@pytest.mark.integration
def test_integration_remove_unrelated_book(store):
    """6. Testar att borttagning av en favorit inte påverkar butikens huvudlista."""
    store.add_book(funny_books[0]["author"], funny_books[0]["title"])  # 100
    store.toggle_favorite(100)  # Lägg till i favoriter

    # Ta bort från favoriter
    store.toggle_favorite(100)

    # Boken ska vara borta från favoriter men finnas kvar i butikens lager
    assert len(store.favorite_manager.books) == 0
    assert len(store.books) == 1


@pytest.mark.integration
def test_integration_fail_gracefully(store):
    """7. Testar att ett misslyckat anrop (fel ID) inte korrumperar favoritlistan."""
    store.add_book(funny_books[0]["author"], funny_books[0]["title"])  # ID 100

    # Försök toggla ett ID som inte finns
    store.toggle_favorite(999)

    # Favoritlistan ska fortfarande vara helt opåverkad och tom
    assert len(store.favorite_manager.books) == 0