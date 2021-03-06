#!/usr/bin/env python
# coding: utf-8

## This is assignment 1 part 2 that includes simple classes.

class Book(object):
    """A print book."""

    author = " "
    title = " "

    def __init__(self, author, title):
        """Constructor for the Book() class.
       
        Args:
            author (str): The author of the book.
            title (str): The title of the book.
        
        Attributes:
            author (str): The author of the book.
            title (str): The title of the book.
        """
        self.author = author
        self.title = title

    def display(self):
        """Displays the book title and author."""

        bookinfo = '"{}, written by {}"'.format(self.title, self.author)
        print bookinfo

BOOK1 = Book('John Steinbeck', 'Of Mice and Men')
BOOK2 = Book('Harper Lee', 'To Kill a Mockingbird')

BOOK1.display()
BOOK2.display()

