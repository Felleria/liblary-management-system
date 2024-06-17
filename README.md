# Library Management System

## Overview

This is a simple command-line interface (CLI) application for managing a library's authors and books. The application uses SQLite as the database and is structured using Python's object-relational mapping (ORM) methods. It is built using the `click` library to handle the CLI operations.

## Features

- Create, read, update, and delete (CRUD) operations for authors and books.
- One-to-many relationship between authors and books.
- Property methods to add appropriate constraints to each model class.
- Validates user input and provides informative error messages.


- **Pipfile**: Manages project dependencies.
- **README.md**: This file.
- **lib/**: Directory containing the main application code.
  - **__init__.py**: Initializes the database connection.
  - **cli.py**: Contains the CLI commands and menus.
  - **debug.py**: For debugging purposes.
  - **models/**: Directory containing the ORM models.
    - **__init__.py**: Initializes the models.
    - **author.py**: Defines the `Author` model.
    - **book.py**: Defines the `Book` model.

## Setup

### Prerequisites

- Python 3.8+
- Pipenv

### Installation

1. Clone the repository:
    ```sh
    git clone <https://github.com/Felleria/liblary-management-system.git>
    cd library-management-system
    ```

2. Install the dependencies:
    ```sh
    pipenv install
    ```

3. Activate the Pipenv shell:
    ```sh
    pipenv shell
    ```

## Usage

### Initialize the Database

Before using the application, initialize the database:
```sh
python lib/cli.py initdb


