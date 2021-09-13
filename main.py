from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"C:\chromedriver\chromedriver.exe")

driver.get("https://www.seleniumeasy.com/test/jquery-download-progress-bar-demo.html")
driver.implicitly_wait(3)
my_element = driver.find_element_by_id("downloadButton")
my_element.click()

