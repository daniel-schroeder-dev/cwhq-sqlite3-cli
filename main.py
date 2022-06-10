import sqlite3
from helper import print_table
from init_db import (
    populate_db,
    remove_db,
    connection,
    cursor,
)


def run_query(query, connection, cursor):
    result = cursor.execute(query)

    if query.lower().startswith("select"):
        print()
        print_table(result)
        print()

    connection.commit()


def display_tables(cursor):
    query = """
        SELECT name FROM sqlite_schema
        WHERE type='table'
        ORDER BY name;
    """
    result = cursor.execute(query)
    print("\n")
    for table in result.fetchall():
        table_name = table[0]
        if table_name == "sqlite_sequence":
            continue

        print(table_name)
    print("\n")


def display_table_schema(query, cursor):
    table_name = query.replace(DISPLAY_SCHEMA_COMMAND, "").strip()
    query = """
        SELECT sql FROM sqlite_master WHERE name = ?;
    """
    result = cursor.execute(query, [table_name])
    table_schema = result.fetchone()
    if table_schema is not None:
        print()
        print(table_schema[0])
        print()
    else:
        print("Invalid table name passed to `.schema`!")


def get_query():
    query = ""
    prompt = "sqlite> "
    while True:
        query += input(prompt)
        if query in command_list or query.strip().startswith(DISPLAY_SCHEMA_COMMAND):
            return query
        elif ";" in query:
            return query

        query += "\n"
        prompt = "   ...> "


welcome_message = """
           Welcome to the CWHQ SQLite3 CLI!

This app lets you run raw SQL commands against a SQLite database.
The database comes pre-populated with a few tables that are used
in the SQL section of the CWHQ documentation. You can also add
new tables if you wish.
"""


EXIT_COMMAND = ".exit"
DISPLAY_TABLES_COMMAND = ".tables"
DISPLAY_SCHEMA_COMMAND = ".schema"
HELP_COMMAND = ".help"

command_list = [
    EXIT_COMMAND,
    DISPLAY_TABLES_COMMAND,
    DISPLAY_SCHEMA_COMMAND,
    HELP_COMMAND,
]


sql_command_options = """
########################################################################################

                                SQLite3 CLI Options

    .exit                   -> Exits this app
    .tables                 -> Displays the tables in the DB
    .schema [table_name]    -> Displays the `CREATE TABLE` statement for this table
    .help                   -> Displays these options

########################################################################################
"""

if __name__ == "__main__":
    populate_db()
    print(welcome_message)
    print(sql_command_options)

    try:
        while True:
            query = get_query()

            if query == EXIT_COMMAND:
                print("Goodbye!")
                break
            elif query == DISPLAY_TABLES_COMMAND:
                display_tables(cursor)
            elif query.strip().startswith(DISPLAY_SCHEMA_COMMAND):
                display_table_schema(query, cursor)
            else:
                try:
                    run_query(query, connection, cursor)
                except sqlite3.Error as e:
                    print(f"Error: {str(e)}")
                except Exception as e:
                    print(e)

    except Exception as e:
        print("Fatal error:")
        print(e)
    finally:
        remove_db()
