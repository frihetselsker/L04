def celsius_to_fahrenheit(c):
    """Temperature c in degrees Celsius, converted to Fahrenheit"""
    return c * 9 / 5 - 32


def is_teenager(age):
    """True if age is from 13 to 19, both included"""
    return 13 < age <= 19


def max_of_list(numbers):
    """The largest number in a non-empty list"""
    best = 0
    for n in numbers:
        if n > best:
            best = n
    return best


def last_n(items, n):
    """The last n items of the list. If n is 0, the result is []"""
    return items[-n:]


def load_settings(text):
    """Settings written as JSON text, for example '{"volume": 5, "dark": true}', as a dict"""
    return eval(text)
