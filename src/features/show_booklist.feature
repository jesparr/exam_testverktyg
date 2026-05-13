Feature: Visa boklista

  Scenario: Visa alla böcker i katalogen
    Given att jag står på startsidan
    When katalogen har laddats
    Then ska jag se en lista över alla böcker
