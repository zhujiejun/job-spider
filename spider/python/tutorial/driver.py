from selenium import webdriver

CHROME_BINARY_LOCATION = '/opt/module/others/chrome-linux/chrome'
CHROME_DRIVER_LOCATION = '/opt/module/others/chrome-driver/chromedriver'
URL = 'https://www.zhipin.com/job_detail/?city=101280600&query=Java'
AGENT = 'user-agent="Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1 Edg/87.0.4280.88"'
COOKIE = 'cookie="lastCity=101280600; __g=-; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1609996748; t=XGDMvtVUuhnQkVTh; wt2=RPURQQrqGhnQkVTh; _bl_uid=5zkz5je1mjIe8bia44ay428ahekg; __l=l=%2Fwww.zhipin.com%2Fjob_detail%2F%3Fcity%3D101280600%26query%3DJava&r=&g=&s=3&friend_source=0&s=3&friend_source=0; __c=1609996748; __a=60541390.1609996748..1609996748.10.1.10.10; __zp_stoken__=7d39bC3xeB1VGOW1kEB08CEAjM1VvdBEYWipnOBV2ZWd3axNLd3Q7BHp0a193Um4SD2QSZhggZBdNJmECGy4Hbn0EIDMEUWQadQlUbUtrSRovPBQrBBlfFCkdGwshL0J7CTUYdVxfYGxPBTZhHQ%3D%3D; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1609998619"'


class tool:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-dev-shm-usage')
        # chrome_options.add_argument(settings.AGENT)
        chrome_options.add_argument(AGENT)
        chrome_options.add_argument(COOKIE)
        chrome_options.binary_location = CHROME_BINARY_LOCATION
        # chrome_options.add_argument('--proxy-server=http://223.242.225.113:9999')
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_LOCATION, options=chrome_options)


if __name__ == '__main__':
    driver = tool().driver
    driver.get(URL)
    cookie = driver.get_cookies()
    f = open('/home/cat/Downloads/common/zhipin', mode='w')
    f.write(str(cookie))
    print(f'{cookie}')
