import pandas as pd
import strawberry


class Library:
    """Represents a connection to the Library DF."""

    def __init__(self) -> None:
        self.df = pd.read_csv("./toys/code_python/library.csv")

    def get_author_for_book(self, root: "Book") -> "Author":
        """Return author for a given book."""
        # Return the first one?  There's gott'a be a better
        # way to do this.
        return [
            Author(name=name)
            for name in self.df["author"][self.df["title"] == root.title]
        ][0]

    def get_books_for_author(self, root: "Author") -> list["Book"]:
        """Return books for a given author."""
        return [
            Book(title=title)
            for title in self.df["title"][self.df["author"] == root.name]
        ]

    def get_authors(self) -> list["Author"]:
        """Return all authors."""
        return list(Author(name=author) for author in self.df["author"])

    def get_books(self) -> list["Book"]:
        """Return all books."""
        return list(Book(title=title) for title in self.df["title"])


library = Library()


@strawberry.type
class Book:
    """Represents a book object."""

    title: str
    author: "Author" = strawberry.field(resolver=library.get_author_for_book)


@strawberry.type
class Author:
    """Represents an Author object."""

    name: str
    books: list["Book"] = strawberry.field(resolver=library.get_books_for_author)


@strawberry.type
class Query:
    """Represents a query object."""

    books: list[Book] = strawberry.field(resolver=library.get_books)
    authors: list[Author] = strawberry.field(resolver=library.get_authors)


schema = strawberry.Schema(query=Query)
