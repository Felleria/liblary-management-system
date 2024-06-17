import click
from lib.models.author import Author
from lib.models.book import Book

@click.group()
def cli():
    pass

@click.command()
def initdb():
    """Initialize the database."""
    Author.create_table()
    Book.create_table()
    click.echo('Initialized the database.')

@click.command()
def menu():
    """Display the main menu."""
    while True:
        click.echo("\nLibrary Management System")
        click.echo("1. Add Author")
        click.echo("2. Add Book")
        click.echo("3. List Authors")
        click.echo("4. List Books")
        click.echo("5. Delete Author")
        click.echo("6. Delete Book")
        click.echo("7. Find Author by ID")
        click.echo("8. Find Book by ID")
        click.echo("9. View Books by Author")
        click.echo("0. Exit")
        
        choice = click.prompt("Enter your choice", type=int)
        if choice == 1:
            add_author()
        elif choice == 2:
            add_book()
        elif choice == 3:
            list_authors()
        elif choice == 4:
            list_books()
        elif choice == 5:
            delete_author()
        elif choice == 6:
            delete_book()
        elif choice == 7:
            find_author_by_id()
        elif choice == 8:
            find_book_by_id()
        elif choice == 9:
            view_books_by_author()
        elif choice == 0:
            click.echo("Exiting...")
            break
        else:
            click.echo("Invalid choice. Please try again.")

def add_author():
    name = click.prompt("Enter author name")
    author = Author(name=name)
    author.save()
    click.echo(f"Author '{name}' added successfully.")

def add_book():
    title = click.prompt("Enter book title")
    author_id = click.prompt("Enter author ID")
    book = Book(title=title, author_id=author_id)
    book.save()
    click.echo(f"Book '{title}' added successfully.")

def list_authors():
    authors = Author.get_all()
    if authors:
        for author in authors:
            click.echo(f"{author.id}: {author.name}")
    else:
        click.echo("No authors found.")

def list_books():
    books = Book.get_all()
    if books:
        for book in books:
            click.echo(f"{book.id}: {book.title} (Author ID: {book.author_id})")
    else:
        click.echo("No books found.")

def delete_author():
    author_id = click.prompt("Enter author ID to delete", type=int)
    author = Author.find_by_id(author_id)
    if author:
        Author.delete(author_id)
        click.echo(f"Author '{author.name}' deleted successfully.")
    else:
        click.echo("Author not found.")

def delete_book():
    book_id = click.prompt("Enter book ID to delete", type=int)
    book = Book.find_by_id(book_id)
    if book:
        Book.delete(book_id)
        click.echo(f"Book '{book.title}' deleted successfully.")
    else:
        click.echo("Book not found.")

def find_author_by_id():
    author_id = click.prompt("Enter author ID to find", type=int)
    author = Author.find_by_id(author_id)
    if author:
        click.echo(f"{author.id}: {author.name}")
    else:
        click.echo("Author not found.")

def find_book_by_id():
    book_id = click.prompt("Enter book ID to find", type=int)
    book = Book.find_by_id(book_id)
    if book:
        click.echo(f"{book.id}: {book.title} (Author ID: {book.author_id})")
    else:
        click.echo("Book not found.")

def view_books_by_author():
    author_id = click.prompt("Enter author ID to view books", type=int)
    books = Book.find_by_author_id(author_id)
    if books:
        for book in books:
            click.echo(f"{book.id}: {book.title}")
    else:
        click.echo("No books found for this author.")

cli.add_command(initdb)
cli.add_command(menu)

if __name__ == "__main__":
    cli()
