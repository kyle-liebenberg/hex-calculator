import os
import pytest
from playwright.sync_api import Page, expect

# We use a pytest fixture to easily get the URL for our index.html file in every test
@pytest.fixture
def calc_url():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return f"file://{os.path.join(current_dir, 'index.html')}"

# --- Core Arithmetic Tests ----

def test_addition_gui(page: Page, calc_url):
    # Navigate to the calculator applciation's frontend
    page.goto(calc_url)

    # Simulate a user clicking the buttons: 1A + 2F = 
    page.locator('button.btn-num', has_text="1").click()
    page.locator('button.btn-hex', has_text="A").click()
    page.locator('button.btn-op', has_text="+").click()
    page.locator('button.btn-num', has_text="2").click()
    page.locator('button.btn-hex', has_text="F").click()
    page.locator('button.btn-equal').click()

    # Grab the main display and assert it shows the correct answer
    display = page.locator('#main-display')

    # Playwright will automatically wait and retry until "49" appears or it times out. 
    expect(display).to_have_text("49")

# --- Usability and constraints tests ---

def test_clear_button(page: Page, calc_url):
    page.goto(calc_url)

    # Type some numbers
    page.locator('button.btn-num', has_text="1").click()
    page.locator('button.btn-num', has_text="8").click()

    # Hit clear
    page.locator('button.btn-clear').click()

    # Assert display resets to 0 and equation clears
    expect(page.locator('#main-display')).to_have_text("0")
    expect(page.locator('#equation-display')).to_have_text("")

