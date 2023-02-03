import time
import os
import requests
from selenium import webdriver
from tools import mkdir_recursive

def manage_scrape_banners(config):
    stores_config = config.get("stores")
    if stores_config:
        for store_config in config.get("stores"):
            cb = ScrapeBanners(store_config)
            banners_urls = cb.get_banners_urls_from_page_source()
            cb.save_banners_to_local_disc(banners_urls)


class ScrapeBanners:
    def __init__(self, store_config):
        self.config = store_config
        self.banner_prefix = self.config.get("banner_prefix")
        self.time_sleep = self.config.get("time_sleep")
        self.store_url = self.config.get("store_url")
        self.banners_output = self.config.get("banners_output")

    def get_banners_urls_from_page_source(self):
        driver = webdriver.Chrome()
        driver.get(self.store_url)
        banners_url = []
        for jia in range(10):
            page_source = driver.page_source
            temp = page_source.split('"')
            for i in temp:
                if self.banner_prefix in i and i not in banners_url:
                    banners_url.append(i)
            time.sleep(self.time_sleep)
        return banners_url

    def save_banners_to_local_disc(self, banners_url):
        for url in banners_url:
            response = requests.get(url)
            name = url.replace(self.banner_prefix, "")
            mkdir_recursive(self.banners_output)
            open(os.path.join(self.banners_output, name), "wb").write(response.content)
