import booking.constants as const
from selenium import webdriver

class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r"C:\chromedriver\chromedriver.exe", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        super(Booking, self).__init__()

    def __exit__(self, ex_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()
    
    def land_first_page(self):
        self.get(const.BASE_URL)


