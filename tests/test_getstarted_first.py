"""
These tests cover the navigation from the Get Started Page.
"""
import pytest
from pytest_bdd import scenarios, scenario, given, when, then, parsers
from functools import partial
from pages.getstarted import SleepioLandingPage
from pages.sleepscoreinitialpage import SleepScoreHowWouldYouLikeToImproveYourSleepPage

#scenarios = partial(scenario, '../tests/features/getstarted.feature')

@scenario('../tests/features/getstarted.feature', 'Basic Sleepio Navigation From Landing Page')
def test_getstarted():
    pass

@pytest.mark.usefixtures("browser")
def test_navigation_from_landing_page(browser):
    landing_page = SleepioLandingPage(browser)
    result_page = SleepScoreHowWouldYouLikeToImproveYourSleepPage(browser)
    Expected_header = "YOUR SLEEP SCORE"
    return landing_page

# Given the Sleepio home page is displayed
@given("the Sleepio home page is displayed")
def test_given_on_landing_page(browser):
    landing_page = SleepioLandingPage(browser)
    landing_page.load()

# When the user clicks "Get Started"
@when('the user clicks "Get Started"')
def getstarted_click(browser):
    landing_page = SleepioLandingPage(browser)
    landing_page.click()

# Then the page header contains "YOUR SLEEP SCORE"
@then('the page header contains "YOUR SLEEP SCORE"')
def page_header_assertion(browser):
    Expected_header = "YOUR SLEEP SCORE"
    result_page = SleepScoreHowWouldYouLikeToImproveYourSleepPage(browser)
    assert Expected_header in result_page.result_header_value()

# And the page with the question "How would you like to improve your sleep?" appears
@then('the page with the question "How would you like to improve your sleep?" appears')
def page_assertion(browser):
    result_page = SleepScoreHowWouldYouLikeToImproveYourSleepPage(browser)
    assert "How would you like to improve your sleep?" in result_page.result_link_title()
