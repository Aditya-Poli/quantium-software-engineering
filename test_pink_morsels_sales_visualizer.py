from pink_morsels_sales_visualizer import app
from selenium import webdriver    
import chromedriver_autoinstaller
from selenium.webdriver.chrome.service import Service

chromedriver_autoinstaller.install()
driver = webdriver.Chrome(service=Service())

def test_header_exists(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#header", timeout=10)


def test_visualization_exists(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#visulaization", timeout=10)


def test_region_selector_exists(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#region_selector", timeout=10)