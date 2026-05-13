Feature: Favoritmarkera en bok

  Scenario: Klickar jag på hjärtat på en titel skall den läggas till som favorit
    Given att jag är på sidan katalog
    When jag klickar på hjärt-ikonen på en bok
    Then vill jag att boken sparas som favorit och hamnar under "Mina böcker"


  Scenario:  Favoritmarkerade böcker ska öka räknaren på sidan "Statistik"
    Given att jag är på sidan katalog
    When jag klickar på hjärt-ikonen på en bok
    Then ska siffran för favoritmarkerade böcker öka med 1 på sidan "Statistik"