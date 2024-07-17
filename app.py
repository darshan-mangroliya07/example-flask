from flask import Flask
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

app = Flask(__name__)

options=webdriver.EdgeOptions()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--disable-extensions")
options.add_argument("--no-sandbox")

driver=webdriver.Edge(options=options)


@app.route('/')
def hello_world():

    driver.get("https://www.google.com")
    return driver.title


if __name__ == "__main__":
    app.run()
