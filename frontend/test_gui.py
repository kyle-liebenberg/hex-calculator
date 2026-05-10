import os
import pytest
from playwright.sync_api import Page, expect

@pytest.fixture
def calc_url():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return f"file://{os.path.join(current_dir, 'index.html')}"

# --- CORE ARITHMETIC TESTS ---

def test_addition_gui(page: Page, calc_url):
    page.goto(calc_url)
    page.locator('button.btn-num', has_text="1").click()
    page.locator('button.btn-hex', has_text="A").click()
    page.locator('button.btn-op', has_text="+").click()
    page.locator('button.btn-num', has_text="2").click()
    page.locator('button.btn-hex', has_text="F").click()
    page.locator('button#btn-equal').click()
    
    expect(page.locator('#main-display')).to_have_text("49")

def test_subtraction_gui(page: Page, calc_url):
    page.goto(calc_url)
    page.locator('button.btn-hex', has_text="F").click()
    page.locator('button.btn-num', has_text="4").click()
    page.locator('button.btn-op', has_text="-").click()
    page.locator('button.btn-num', has_text="8").click()
    page.locator('button.btn-hex', has_text="A").click()
    page.locator('button#btn-equal').click()
    
    expect(page.locator('#main-display')).to_have_text("6A")

def test_multiplication_gui(page: Page, calc_url):
    page.goto(calc_url)
    page.locator('button.btn-num', has_text="2").click()
    page.locator('button.btn-hex', has_text="F").click()
    page.locator('button.btn-op', has_text="*").click()
    page.locator('button.btn-num', has_text="0").first.click()
    page.locator('button.btn-num', has_text="2").click()
    page.locator('button#btn-equal').click()
    
    expect(page.locator('#main-display')).to_have_text("5E")

def test_division_gui(page: Page, calc_url):
    page.goto(calc_url)
    page.locator('button.btn-num', has_text="8").click()
    page.locator('button.btn-hex', has_text="C").click()
    page.locator('button.btn-op', has_text="/").click()
    page.locator('button.btn-num', has_text="0").first.click()
    page.locator('button.btn-num', has_text="4").click()
    page.locator('button#btn-equal').click()
    
    expect(page.locator('#main-display')).to_have_text("23")


# --- USABILITY AND CONSTRAINT TESTS ---

def test_clear_button(page: Page, calc_url):
    page.goto(calc_url)
    # Type some numbers
    page.locator('button.btn-num', has_text="7").click()
    page.locator('button.btn-num', has_text="8").click()
    
    # Hit clear
    page.locator('button#btn-clear').click()
    
    # Assert display resets to 0 and equation clears
    expect(page.locator('#main-display')).to_have_text("0")
    expect(page.locator('#equation-display')).to_have_text("")

def test_frontend_input_limit(page: Page, calc_url):
    page.goto(calc_url)
    # Attempt to type three characters: "1", "2", "3"
    page.locator('button.btn-num', has_text="1").click()
    page.locator('button.btn-num', has_text="2").click()
    page.locator('button.btn-num', has_text="3").click()
    
    # The frontend JavaScript should prevent the "3" from registering
    expect(page.locator('#main-display')).to_have_text("12")

def test_backend_error_negative_alert(page: Page, calc_url):
    page.goto(calc_url)
    
    # Playwright automatically dismisses alerts. We need to set up a listener 
    # to catch the alert message and accept it.
    dialog_messages = []
    page.on("dialog", lambda dialog: (dialog_messages.append(dialog.message), dialog.accept()))
    
    # Input 05 - 0A
    page.locator('button.btn-num', has_text="0").first.click()
    page.locator('button.btn-num', has_text="5").click()
    page.locator('button.btn-op', has_text="-").click()
    page.locator('button.btn-num', has_text="0").first.click()
    page.locator('button.btn-hex', has_text="A").click()
    page.locator('button#btn-equal').click()
    
    # Assert the screen says "Error"
    expect(page.locator('#main-display')).to_have_text("Error")
    
    # Assert the backend specifically sent back our negative answer constraint message
    assert "negative answers" in dialog_messages[0]