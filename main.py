import re
import urllib.parse
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class TelephoneScraper:
    def __init__(self):
        self.url = "https://www.b144.co.il/%D7%90%D7%99%D7%A0%D7%A1%D7%98%D7%9C%D7%98%D7%95%D7%A8%D7%99%D7%9D/"
        self.init_driver()

    def init_driver(self):
        parsed_url = urllib.parse.unquote(self.url)
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get(parsed_url)
        all_whatsapp_links = self.driver.find_elements_by_xpath("//div[starts-with(@id,'whatsapp')]")
        for all_links in all_whatsapp_links:
            #Find the onclick attribute value
            attr_values = all_links.get_attribute("onclick")
            #Parsing strings and getting the number
            pre_regex = attr_values.split(";")[2].split(",")[-1]
            #Regex to parse on the numbers between "_" and ")"
            regex_expr = r'.*\_(.*)\)'
            post_regex_match = re.search(regex_expr,pre_regex)
            post_regex_str = post_regex_match.group(1)
            print(post_regex_str)
        print(len(all_whatsapp_links))
        


TelephoneScraper()