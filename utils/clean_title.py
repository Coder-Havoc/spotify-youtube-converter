# utils/clean_title.py

import re

def clean_title(title):
    """
    Removes special characters, excessive spaces, and content within parentheses/brackets.
    Useful for getting cleaner search queries for YouTube.
    """
    # Remove text in parentheses or brackets
    title = re.sub(r"\([^)]*\)", "", title)
    title = re.sub(r"\[[^]]*\]", "", title)

    # Remove special characters and multiple spaces
    title = re.sub(r"[^\w\s\-]", "", title)
    title = re.sub(r"\s+", " ", title)

    return title.strip()
