Feature: Formulärvalidering

  Scenario: Båda fälten måste vara ifyllda för att kunna lägga till en ny bok
    Given att jag är på sidan "Lägg till bok"
    When jag inte har fyllt i alla fält
    Then vill jag att knappen "Lägg till ny bok" endast skall vara aktiv när alla fält är ifyllda