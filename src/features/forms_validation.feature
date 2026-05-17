Feature: Formulärvalidering

  Scenario: Knappen ska vara inaktiv om fält lämnas tomma
    Given att jag är på sidan "Lägg till bok"
    When jag inte har fyllt i alla fält
    Then vill jag att knappen "Lägg till ny bok" endast skall vara aktiv när alla fält är ifyllda