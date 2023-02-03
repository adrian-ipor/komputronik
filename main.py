from configuration.config_parser import ConfigurationParser
from scrape_banners import manage_scrape_banners
from scrape_new_products import manage_scrape_new_products

def main():
    cp = ConfigurationParser()
    config = cp.get_config()
    manage_scrape_banners(config)
    manage_scrape_new_products(config)

main()

