# utility.py
import datetime

def format_date(date):
    """Format a date as a string (e.g., 'YYYY-MM-DD')."""
    return date.strftime('%Y-%m-%d')

def parse_date(date_str):
    """Parse a date string (e.g., 'YYYY-MM-DD') into a datetime object."""
    return datetime.datetime.strptime(date_str, '%Y-%m-%d')

def calculate_square(number):
    """Calculate the square of a number."""
    return number ** 2

def sanitize_input(input_str):
    """Sanitize user input by removing leading and trailing whitespace."""
    return input_str.strip()
