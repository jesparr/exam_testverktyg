Feature: Lägga till ny bok

  Scenario: Lägga till ny bok med titel och författare
    Given att jag är på sidan för att lägga till böcker
    When jag fyller i titel och författare och klickar på spara
    Then vill jag att boken skall läggas till under "Mina böcker"