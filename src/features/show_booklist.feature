Feature: Visa boklista

  Scenario: Visa alla böcker i katalogen
    Given att jag är på startsidan
    Then ska jag se en lista över alla böcker
    And varje bok ska visa titel och författare