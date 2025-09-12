"""
Library Management System
Lab 9 – Task 2
This module provides basic functions to manage books in a library system.
"""

def add_book(title, author, year):
    """
    Add a new book to the library.

    Args:
        title (str): The title of the book.
        author (str): The author of the book.
        year (int): The year the book was published.

    Returns:
        dict: A dictionary containing the details of the added book.

    Example:
        >>> add_book("1984", "George Orwell", 1949)
        {'title': '1984', 'author': 'George Orwell', 'year': 1949}
    """
    # For demonstration, we just return a dictionary
    return {"title": title, "author": author, "year": year}


def issue_book(book_id, user_id):
    """
    Issue a book from the library to a user.

    Args:
        book_id (int): The unique ID of the book to issue.
        user_id (int): The unique ID of the user borrowing the book.

    Returns:
        str: A confirmation message with book_id and user_id.

    Example:
        >>> issue_book(101, 2001)
        'Book 101 has been issued to user 2001.'
    """
    # For demonstration, just return a message
    return f"Book {book_id} has been issued to user {user_id}."


# ---------------------------------------------------
# Test the functions
# ---------------------------------------------------
if __name__ == "__main__":
    print(add_book("The Hobbit", "J.R.R. Tolkien", 1937))
    print(issue_book(101, 2001))