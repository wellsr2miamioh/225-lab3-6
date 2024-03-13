'''
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class HtmlElementsTestCase(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--user-data-dir=/tmp/chrome_user_data")

        self.driver = webdriver.Chrome(options=options)

    def test_navigate_to_website(self):
        # Navigate to the website and then quit the browser.
        self.driver.get("http://10.48.10.170")

    def tearDown(self):
        # Quit the driver after test execution.
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
'''
