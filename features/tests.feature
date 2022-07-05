# Created by ivanc at 03.07.2022
Feature: Checking the functionality of exchange rates in the (chrome)

  Background:
    Given Open browser chrome on https://infinbank.com/ru/ and set current language RU

  Scenario:
    Then Check the texts of the functionality "currency rates" in the current language
    And Change language to UZ
    And Check the texts of the functionality "currency rates" in the current language
    And Change language to EN
    And Check the texts of the functionality "currency rates" in the current language

  Scenario:
    Then Check the correspondence of indicators to changes in exchange rates
    And Change language to UZ
    And Check the correspondence of indicators to changes in exchange rates
    And Change language to EN
    And Check the correspondence of indicators to changes in exchange rates