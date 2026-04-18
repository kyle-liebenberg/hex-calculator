import pytest
from src.calculator import add_hex, sub_hex, mul_hex, div_hex

# --- ADDITION TESTS ---
def test_add_hex():
    assert add_hex("1A", "2F") == "49"

def test_add_hex_input_limit():
    with pytest.raises(ValueError, match="maximum of 2 digits"):
        add_hex("FFF", "1")

# --- SUBTRACTION TESTS ---
def test_sub_hex():
    assert sub_hex("F4", "8A") == "6A"

def test_sub_hex_negative():
    # Attempting 05 - 0A (5 - 10) should raise an error
    with pytest.raises(ValueError, match="negative"):
        sub_hex("05", "0A")

# --- MULTIPLICATION TESTS ---
def test_mul_hex():
    assert mul_hex("2F", "02") == "5E"

def test_mul_max_output():
    # The highest possible valid input is FF * FF (255 * 255 = 65025). 
    # Hex representation is FE01, which is exactly 4 digits.
    assert mul_hex("FF", "FF") == "FE01"

# --- DIVISION TESTS ---
def test_div_hex():
    assert div_hex("8C", "04") == "23"

def test_div_hex_decimal():
    # Attempting 05 / 02 (5 / 2 = 2.5) should raise an error
    with pytest.raises(ValueError, match="decimal places"):
        div_hex("05", "02")

def test_div_zero():
    # Attempting to divide by zero
    with pytest.raises(ValueError, match="divide by zero"):
        div_hex("8C", "00")

# --- GENERAL INPUT VALIDATION ---
def test_invalid_hex_characters():
    # Attempting to input a character outside of 0-9 and A-F
    with pytest.raises(ValueError, match="valid hexadecimal"):
        add_hex("GZ", "01")