from utils.paterns import Singleton
from selenium import webdriver


class DriverManagerBase:
    DRIVERS = {
        "chrome": (webdriver.Chrome, r"C:\chromedriver\chromedriver.exe"),
        "firefox": (webdriver.Firefox, r"C:\path\to\geckodriver.exe")
    }
    WEB_DRIVERS = {}

    def webdriver(self, browser_type):
        if browser_type in self.DRIVERS.keys():
            if browser_type not in self.WEB_DRIVERS.keys():
                self.WEB_DRIVERS[browser_type] = self.DRIVERS[browser_type][0](
                    executable_path=self.DRIVERS[browser_type][1]
                )
            return self.WEB_DRIVERS[browser_type]

    def close(self, browser_type):
        self.WEB_DRIVERS[browser_type].close()
        self.WEB_DRIVERS.pop(browser_type)


class DriverManager(DriverManagerBase, metaclass=Singleton):
    pass
