Feature: Ta bort favoritmarkering

  Scenario: Ta bort favoritmarkering
    Given att jag är på sidan "Katalog"
    And det finns böcker som är favoritmarkerade
    When jag klickar på hjärtat på en redan favoritmarkerad bok
    Then ska boken försvinna från listan på "Mina böcker"
