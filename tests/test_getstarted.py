"""
These tests cover the navigation from the Get Started Page.
"""

from pages.getstarted import SleepioLandingPage
from pages.sleepscoreinitialpage import SleepScoreHowWouldYouLikeToImproveYourSleepPage

def test_basic_navigation_from_landing_page(browser):
  landing_page = SleepioLandingPage(browser)
  result_page = SleepScoreHowWouldYouLikeToImproveYourSleepPage(browser)
  Expected_header = "YOUR SLEEP SCORE"

  # Given the Sleepio home page is displayed
  landing_page.load()

  # When the user clicks "Get Started"
  landing_page.click()

  # Then the page header contains "YOUR SLEEP SCORE"
  assert Expected_header in result_page.result_link_title()

  # And the page with the question "How would you like to improve your sleep?" appears
  assert "How would you like to improve your sleep?" in result_page.title()

  raise Exception("Incomplete Test")