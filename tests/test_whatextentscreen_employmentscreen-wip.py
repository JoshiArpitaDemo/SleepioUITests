"""
These tests cover the navigation from the "How many nights a week have you had a problem with your sleep?" through 
to the "What is your employment status?" Page
"""

import pytest
import time
from pages.sleepscoreinitialpage import SleepScoreHowWouldYouLikeToImproveYourSleepPage
from pages.getstarted import SleepioLandingPage
from pages.howlongproblemwithsleeppage import HowLongProblemWithSleepPage
from pages.sleepingmostoftenquestionpage import WhatStopsFromSleepingMostOftenPage
from pages.prequeswhatextentpage import WhatExtentPastMonthPage

@pytest.mark.usefixtures("browser")
def test_navigation_from_whatextentscreen_to_employmentscreen(browser):
     initial_page = SleepScoreHowWouldYouLikeToImproveYourSleepPage(browser)
     landing_page = SleepioLandingPage(browser)
     problemwithsleep_page = HowLongProblemWithSleepPage(browser)
     whatstopsfromsleeping_page = WhatStopsFromSleepingMostOftenPage(browser)
     whatextent_page = WhatExtentPastMonthPage(browser)

#Given the `How many nights a week have you had a problem with your sleep?` page
     initial_page.load_improvesleeppage()
     landing_page.click()
     initial_page.check_multiple_options()
     initial_page.click_continue()
     problemwithsleep_page.dropdown_selections()
     problemwithsleep_page.continue_click()
     whatstopsfromsleeping_page.select_first_radio_button()
     whatstopsfromsleeping_page.click_continue()
     whatextent_page.dropdown_selections()
     time.sleep(5)
     problemwithsleep_page.continue_click()
     time.sleep(10)

#When I select the option from the dropdown and navigate further to reach the DOB page


#Then I see the compliance message with the link to Privacy Policy
