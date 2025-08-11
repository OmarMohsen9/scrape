import functions
import config

if __name__ == "__main__":
    driver = functions.setup_and_launch_chrome(config.Implicit_wait)
    try:
        functions.web_goto(driver,config.baseurl)
        functions.verify_title(driver,config.Expected_HomePage_title)
        items = functions.scrape_list(driver,config.Expected_mobilePage_title)
        check_sort = sorted(items)
        if items == check_sort:
            print("Sorted")
        else:
            print("Not Sorted")
        functions.check_prices(driver)
    finally:
        driver.quit()