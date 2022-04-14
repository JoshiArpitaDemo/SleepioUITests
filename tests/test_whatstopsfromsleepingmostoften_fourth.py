"""
These tests cover the navigation from the "Which of the following stops you from sleeping most often?" Page to the next page "To what extent has sleep troubled you in general?"
Also, tests that only one checkbox can be selected at a time 
"""

from selenium.webdriver.support.ui import Select
import pytest
import time
from pages.sleepscoreinitialpage import SleepScoreHowWouldYouLikeToImproveYourSleepPage
from pages.getstarted import SleepioLandingPage
from pages.howlongproblemwithsleeppage import HowLongProblemWithSleepPage
from pages.sleepingmostoftenquestionpage import WhatStopsFromSleepingMostOftenPage

@pytest.mark.usefixtures("browser")
def test_navigation_from_whatstopsfromsleepingmostoften_page(browser):
     initial_page = SleepScoreHowWouldYouLikeToImproveYourSleepPage(browser)
     landing_page = SleepioLandingPage(browser)
     problemwithsleep_page = HowLongProblemWithSleepPage(browser)
     whatstopsfromsleeping_page = WhatStopsFromSleepingMostOftenPage(browser)

#Given the `Which of the following stops you from sleeping most often?` page
     initial_page.load_improvesleeppage()
     landing_page.click()
     initial_page.check_multiple_options()
     initial_page.click_continue()
     problemwithsleep_page.dropdown_selections()
     problemwithsleep_page.continue_click()


#When I select the first option
     whatstopsfromsleeping_page.select_first_radio_button()

#And I select the second option
     whatstopsfromsleeping_page.select_the_second_radio_button()

#Then the first option greys out
     whatstopsfromsleeping_page.the_first_option_greysout()


#And only the second option remains selected
     whatstopsfromsleeping_page.the_second_option_remains_selected()