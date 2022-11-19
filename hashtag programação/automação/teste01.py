from playwright.sync_api import sync_playwright
import time
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://github.com/davileal7")
    time.sleep(5)
    page.screenshot(path="example01.png")
    print(page.title())

