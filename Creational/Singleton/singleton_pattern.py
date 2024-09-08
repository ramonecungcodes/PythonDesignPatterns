"""Module providing an example of the Singleton design pattern."""

# pylint: disable=locally-disabled, too-few-public-methods, unused-private-member
class DatabaseConnection():
    """ Demonstrates a class that will only ever instantiate one object. """

    def __new__(cls):
        if not hasattr(cls, "__singleton"):
            cls.__singleton = super(DatabaseConnection, cls).__new__(cls)
        return cls


def demo_singleton_pattern():
    """Demo the Singleton design pattern as implemented using the classes above"""

    first_database_connection = DatabaseConnection()
    second_database_connection = DatabaseConnection()

    print("Is the first database connection the same instance as the second? "\
          f"{first_database_connection is second_database_connection}")
    print(f"The internal ID of the first database connection is {id(first_database_connection)} "\
          f"and the ID of the second is {id(second_database_connection)}")


if __name__ == "__main__":
    demo_singleton_pattern()
