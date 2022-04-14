@sleepiolanding
Feature: Sleepio browsing from landing page

  Scenario: Basic Sleepio Navigation From Landing Page
    Given the Sleepio home page is displayed
    When the user clicks "Get Started"
    Then the page header contains "YOUR SLEEP SCORE"
    And the page with the question "How would you like to improve your sleep?" appears

