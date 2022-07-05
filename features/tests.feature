# Created by ivanc at 03.07.2022
Feature: Checking the functionality of exchange rates in the (chrome)


  Scenario Outline:
    Given Open browser chrome on https://infinbank.com/lang/ and set current language <lang>
    Then Check "currency rates" title text in current language
    Then Check all rates button text in current language
    Then Check exchange offices link text in current language
    Then Check the correspondence of indicators to changes in exchange rates
    Examples:
      | lang |
      | RU   |
      | UZ   |
      | EN   |

  Scenario Outline:
    Given Open browser chrome on https://infinbank.com/lang/ and set current language <lang>
    When Click all rates button
    Then Check url Check the url on the "all rates" page
    Examples:
      | lang |
      | RU   |
      | UZ   |
      | EN   |

  Scenario Outline:
    Given Open browser chrome on https://infinbank.com/lang/ and set current language <lang>
    When Click exchange offices link
    Then Check url Check the url on the "currency exchange offices" page
    Examples:
      | lang |
      | RU   |
      | UZ   |
      | EN   |

