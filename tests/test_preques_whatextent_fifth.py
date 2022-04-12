"""
These tests cover the navigation from the "To what extent has sleep troubled you in general?" Page
Also, tests that a selection has to be made before continuing 
"""

import pytest
import time
from pages.sleepscoreinitialpage import SleepScoreHowWouldYouLikeToImproveYourSleepPage
from pages.getstarted import SleepioLandingPage
from pages.howlongproblemwithsleeppage import HowLongProblemWithSleepPage
from pages.sleepingmostoftenquestionpage import WhatStopsFromSleepingMostOftenPage
from pages.prequeswhatextentpage import WhatExtentPastMonthPage

@pytest.mark.usefixtures("browser")
def test_navigation_from_whatextent_page(browser):
     initial_page = SleepScoreHowWouldYouLikeToImproveYourSleepPage(browser)
     landing_page = SleepioLandingPage(browser)
     problemwithsleep_page = HowLongProblemWithSleepPage(browser)
     whatstopsfromsleeping_page = WhatStopsFromSleepingMostOftenPage(browser)
     whatextent_page = WhatExtentPastMonthPage(browser)

#Given the `To what extent has sleep troubled you in general?` page     
     initial_page.load_improvesleeppage()
     landing_page.click()
     initial_page.check_multiple_options()
     initial_page.click_continue()
     problemwithsleep_page.dropdown_selections()
     problemwithsleep_page.continue_click()
     whatstopsfromsleeping_page.select_first_radio_button()
     whatstopsfromsleeping_page.click_continue()

#When I try to navigate further without selecting any options from dropdown
     whatextent_page.click_button_wrapper()


#Then I get the message `Please answer all the questions before continuing` 
     whatextent_page.error_message_shown()