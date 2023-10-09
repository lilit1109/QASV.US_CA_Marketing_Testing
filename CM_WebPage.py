from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://qasvus.wixsite.com/ca-marketing")
print(driver.title)
print(driver.current_url)
driver.quit()