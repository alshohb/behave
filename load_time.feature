Feature: Page Load Speed
    As a website user
    I want the website to load quickly
    So that I can have a good user experience

Scenario: Load Time Within Acceptable Limit
    Given I navigate to the website
    When the page has finished loading
    Then the page load time should be less than 3 seconds
