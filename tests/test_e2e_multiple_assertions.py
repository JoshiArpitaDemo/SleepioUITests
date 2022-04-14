"""
These tests cover the entire AUT from landing page to getting a sleep score Page with multiple assertions in between
"""

import pytest
import time
from pages.sleepscoreinitialpage import SleepScoreHowWouldYouLikeToImproveYourSleepPage
from pages.getstarted import SleepioLandingPage
from pages.howlongproblemwithsleeppage import HowLongProblemWithSleepPage
from pages.sleepingmostoftenquestionpage import WhatStopsFromSleepingMostOftenPage
from pages.prequeswhatextentpage import WhatExtentPastMonthPage
from pages.e2enavigationpage import MultipleScreenPages

@pytest.mark.usefixtures("browser")
def test_e2e(browser):
     initial_page = SleepScoreHowWouldYouLikeToImproveYourSleepPage(browser)
     landing_page = SleepioLandingPage(browser)
     problemwithsleep_page = HowLongProblemWithSleepPage(browser)
     whatstopsfromsleeping_page = WhatStopsFromSleepingMostOftenPage(browser)
     whatextent_page = WhatExtentPastMonthPage(browser)
     multiple_pages = MultipleScreenPages(browser)


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
     problemwithsleep_page.continue_click()

#And I select the option from the dropdown and navigate further to reach the employment screen
     multiple_pages.dropdown_selections()
     multiple_pages.click_continue()

     multiple_pages.dropdown_selections_control()
     multiple_pages.click_continue()

     multiple_pages.dropdown_selections_strugglepage()
     multiple_pages.click_continue()
     #Gender
     multiple_pages.select_the_second_radio_button()
     multiple_pages.click_continue()
     #DOB
     multiple_pages.dob_inputs()
     multiple_pages.click_continue()

#When I select employment status as 'Employed full-time' I get questions related to productivity
     multiple_pages.dropdown_employment()
     multiple_pages.click_continue()
     multiple_pages.dropdown_productivity_first()
     multiple_pages.click_continue()
     multiple_pages.dropdown_productivity_second()
     multiple_pages.click_continue()
     #Assert that I reach guide_page
     multiple_pages.assert_guide_page()

     multiple_pages.select_the_second_radio_button()
     multiple_pages.click_continue()
     multiple_pages.sign_up_details()
     #Final sleep score assertion!
     multiple_pages.assert_final_page()
