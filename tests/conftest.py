import pytest
import selenium.webdriver

@pytest.fixture
def browser():

    #Initialize the ChromeDriver Instance
    b = selenium.webdriver.Chrome()
    
    #Make its calls wait up to 10 seconds for elements to appear 
    b.implicitly_wait(10)
    
    # Return the WebDriver instance for the setup
    yield browser
    
    # Quit the WebDriver instance for the cleanup
    b.quit()