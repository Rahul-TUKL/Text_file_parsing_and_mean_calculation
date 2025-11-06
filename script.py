import ast # https://docs.python.org/3/library/ast.html
import math # https://docs.python.org/3/library/math.html
import sys  # https://docs.python.org/3/library/sys.html

def parse_value(value):
    """Convert a single value into a float if possible, applying all rules."""
    # Handle nested structures recursively as we can have multiple lists or tuples inside a List etc.
    if isinstance(value, (list, tuple)):
        return calculate_mean(value)
    
    # NoneType → ignore
    if value is None:
        return None

    # Strings → clean and interpret
    if isinstance(value, str):
        #print(f"Not Stripped value is: {value}")
        value = value.strip().replace(',', '.') # Strip the value and replace , with . 
        #print(f"Stripped value is: {value}")
        if value.lower() in ('nan', 'none', ''): # Making it case insensitive
            return None
        elif value.lower() == 'inf':
            return float('inf') # converting string to the float
        elif value.lower() == '-inf':
            return float('-inf')
        try:
            return float(value) # converting string to the float
        except ValueError:
            return None

    # Numeric values → cast to float
    if isinstance(value, (int, float)):
        if math.isnan(value): # Using math module to check if the value is nan.
            return None
        return float(value)

    # Unknown types then ignore
    return None


def calculate_mean(sequence):
    """Compute mean of valid values in a list/tuple, recursively handling nesting."""
    valid_values = []
    for item in sequence: # for every item in the line 
        val = parse_value(item) # Returned value from the parsing function
        if isinstance(val, (int, float)) and not math.isnan(val): # again math.isnan(val) checks if the value is none or not.
            valid_values.append(val)

    if not valid_values:
        return None

    # If infinite values exist → handle as per math rules
    if any(math.isinf(v) for v in valid_values):
        # If both +inf and -inf → result NaN
        if any(v == float('inf') for v in valid_values) and any(v == float('-inf') for v in valid_values):
            return float('nan')
        # Only +inf or -inf present → return that
        for v in valid_values:
            if math.isinf(v):
                return v

    # Calculate mean
    return sum(valid_values) / len(valid_values)


def main(input_file):
    with open(input_file, 'r', encoding='utf-8') as file: # For different File Modes refer: https://www.geeksforgeeks.org/python/file-mode-in-python/
        for line in file: # for a single line 
            line = line.strip() #https://docs.python.org/3.4/library/stdtypes.html
            if not line:
                continue
            try:
                # Safely interpret the line as a Python literal (list/tuple) without executing code.
                # Note: literal_eval expects properly quoted strings (e.g., "inf"), so unquoted values may require preprocessing (e.g., regex).
                sequence = ast.literal_eval(line) # Reference: https://stackoverflow.com/questions/15197673/using-pythons-eval-vs-ast-literal-eval
                print(sequence)
                result = calculate_mean(sequence)
                print(result)
            except Exception as e:
                print(f"Error parsing line: {line!r} → {e}", file=sys.stderr) # unterminated string literal (detected at line {No.}) (<unknown>, line {No.})


if __name__ == "__main__":
    # Example usage: python mean_parser.py input.txt
    if len(sys.argv) != 2:
        print("Usage on command prompt:  python script.py <input_file>")
        sys.exit(1)
    main(sys.argv[1])
