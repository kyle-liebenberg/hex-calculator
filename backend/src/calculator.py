def _validate_input(val):
    """Helper function to validate the 2-digit hex input constraint."""
    if len(val) > 2:
        raise ValueError("Inputs must be a maximum of 2 digits.")
    try:
        # Convert the hex string to a base 10 integer
        return int(val, 16)
    except ValueError:
        raise ValueError("Input must be a valid hexadecimal string.")

def _format_output(val_int):
    """Helper function to validate output constraints and format to hex."""
    if val_int < 0:
        raise ValueError("Calculator cannot return negative answers.")
        
    # Convert integer to hex, remove '0x' prefix, and uppercase
    hex_str = hex(val_int)[2:].upper()
    
    if len(hex_str) > 4:
        raise ValueError("Answers cannot exceed 4 digits.")
        
    return hex_str

def add_hex(val1, val2):
    i1 = _validate_input(val1)
    i2 = _validate_input(val2)
    return _format_output(i1 + i2)

def sub_hex(val1, val2):
    i1 = _validate_input(val1)
    i2 = _validate_input(val2)
    # The _format_output function will catch the negative result, but we can explicitly check it here as well.
    if i1 < i2:
         raise ValueError("Calculator cannot return negative answers.")
    return _format_output(i1 - i2)

def mul_hex(val1, val2):
    i1 = _validate_input(val1)
    i2 = _validate_input(val2)
    return _format_output(i1 * i2)

def div_hex(val1, val2):
    i1 = _validate_input(val1)
    i2 = _validate_input(val2)
    
    if i2 == 0:
        raise ValueError("Calculator cannot divide by zero.")
        
    if i1 % i2 != 0:
        raise ValueError("Calculator cannot return answers with decimal places.")
        
    # Using integer division (//) since we already verified there are no remainders
    return _format_output(i1 // i2)