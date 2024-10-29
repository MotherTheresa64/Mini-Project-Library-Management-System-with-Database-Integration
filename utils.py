def get_input(prompt):
    """Get user input and return it."""
    return input(prompt)

def validate_integer(value):
    """Validate if the value is an integer."""
    try:
        return int(value)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return None

def validate_date(date_str):
    """Validate date format YYYY-MM-DD."""
    import datetime
    try:
        datetime.datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        print("Invalid date format. Please enter date as YYYY-MM-DD.")
        return False
