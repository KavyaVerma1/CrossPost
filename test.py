from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_homepage():
    # Initialize the browser (Chrome in this case)
    driver = webdriver.Chrome()
    
    # Navigate to the homepage
    driver.get("https://cross-post-three.vercel.app/")  # Update the URL if needed
    
    time.sleep(3)  # Allow some time for the page to load
    
    try:
        # Verify the heading
        title = driver.find_element(By.TAG_NAME, "h1")
        assert "Your feed" in title.text, "Title does not match expected value"
        
        
        # Verify subreddit info box
        home_section = driver.find_element(By.XPATH, "//p[contains(text(), 'Home')]")
        assert home_section is not None, "Home section is missing"
        
        # Check the 'Create Community' button
        create_button = driver.find_element(By.LINK_TEXT, "Create Community")
        assert create_button is not None, "Create Community button is missing"
        
        print("All tests passed successfully.")
    
    except AssertionError as e:
        print(f"Test failed: {e}")
    
    finally:
        # Close the browser
        driver.quit()

# Run the test
test_homepage()
