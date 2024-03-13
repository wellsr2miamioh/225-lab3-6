from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import unittest

class TestH5Tag(unittest.TestCase):
    def setUp(self):
        # Setup Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Ensures the browser window does not open
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        
        # Set path to chromedriver as per your configuration
        # Optional for dockerized Selenium
        self.driver = webdriver.Chrome(options=chrome_options)

    def test_h5_tag_content(self):
        driver = self.driver
        driver.get("http://10.48.10.170")  # Replace with your target website
        
        # Locate the <h5> tag and get its text
        h5_text = driver.find_element(By.TAG_NAME, "h5").text
        
        # Assert that the text of the <h5> tag is "Lab 3-6 Works!"
        self.assertEqual("Lab 3-6 Works!", h5_text, "The <h5> tag does not contain the text 'lab'")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
