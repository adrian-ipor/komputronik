
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from tools import mkdir_recursive


def manage_scrape_new_products(config):
    stores_config = config.get("stores")
    if stores_config:
        for store_config in config.get("stores"):
            cb = ScrapeNewProducts(store_config)
            cb.get_banners_urls_from_page_source()


class ScrapeNewProducts:
    def __init__(self, store_config):
        self.config = store_config
        self.time_sleep = self.config.get("time_sleep")
        self.store_url = self.config.get("store_url")
        self.css_selector = self.config.get("css_selector")
        self.cookies_except_id = self.config.get("cookies_except_id")
        self.set_window_size = self.config.get("set_window_size", {})
        self.product_tiles_output = self.config.get("product_tiles_output")

    def get_banners_urls_from_page_source(self):
        options = webdriver.ChromeOptions()
        options.headless = True
        driver = webdriver.Chrome()
        driver.get(self.store_url)
        driver.set_window_size(width=self.set_window_size["width"],
                               height=self.set_window_size["height"])  # May need manual adjustment
        page_source = driver.page_source
        driver.find_element(By.ID, self.cookies_except_id).click()
        count_of_css_selectors = page_source.count(self.css_selector)
        mkdir_recursive(self.product_tiles_output)
        for index in range(count_of_css_selectors):
            driver.find_element(By.CSS_SELECTOR, f"div[class='{self.css_selector}{index}']").screenshot(os.path.join(
                self.product_tiles_output, f'web_screenshot{index}.png'))
        driver.quit()
