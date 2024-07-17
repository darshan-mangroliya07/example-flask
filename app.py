from flask import Flask
from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Open a website
    page.goto('http://google.com')


    # Get the title of the page
    title = page.title()
    print(title)

    # Close the browser
    browser.close()

with sync_playwright() as playwright:
    run(playwright)



app = Flask(__name__)



@app.route('/')
def hello_world():
    run()
    return "Hello"


if __name__ == "__main__":
    app.run()
