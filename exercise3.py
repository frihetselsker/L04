def average(numbers):
    """Average of a list. An empty list has average 0"""
    return sum(numbers) / len(numbers) if numbers else 0


def first_word(text):
    """The first word of the text, or "" if the text is empty"""
    words = text.split()
    return words[0] if words else ""


def percent(part, total):
    """part as a percentage of total. If total is 0, the result is 0"""
    return part / total * 100 if total != 0 else 0
