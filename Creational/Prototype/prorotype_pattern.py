"""Module providing an example of the Prototype design pattern."""


from abc import ABC, abstractmethod

# pylint: disable=locally-disabled, too-few-public-methods
class PrototypeInterface(ABC):
    """Defines interface for cloning an object"""
    @abstractmethod
    def clone(self):
        """Abstract method that provides ability to clone the concrete implementation of"""

# pylint: disable=locally-disabled, too-few-public-methods
class DataLoadInterface(ABC):
    """Provides interface for loading data into an object"""
    @abstractmethod
    def attempt_data_load(self):
        """Provides functionality to load data"""


class ExpensiveDatabaseDataLoad(DataLoadInterface, PrototypeInterface):
    """Simulates loading data from a database"""

    def __init__(self, data_set: str) -> None:
        self.database_hostname = "MYHOST"
        self.database_port = 80
        self.data_set = data_set

    def perform_expensive_data_load(self):
        """Simulates performing the data load"""

    def attempt_data_load(self):
        self.perform_expensive_data_load()

    def clone(self):
        new_instance = ExpensiveDatabaseDataLoad(self.data_set)
        new_instance.database_hostname = self.database_hostname
        new_instance.database_port = self.database_port
        return new_instance


class ExpensiveNetworkFileLoad(DataLoadInterface, PrototypeInterface):
    """Simulates loading data from across a network"""

    def __init__(self):
        self.unc_path = "\\server\folder\file.txt"
        self.target_path = "/home/$user/folder"

    def load_huge_data_file(self):
        """Simulates performing the data load"""

    def attempt_data_load(self):
        self.load_huge_data_file()

    def clone(self):
        new_instance = ExpensiveNetworkFileLoad()
        new_instance.unc_path = self.unc_path
        new_instance.target_path = self.target_path
        return new_instance


def demo_prototype_pattern():
    """Demo the Prototype design pattern as implemented using the classes above"""

    original_object = ExpensiveDatabaseDataLoad("SALES_DATA")
    print("The original object's will connect to "\
          f"{original_object.database_hostname}:{original_object.database_port}")
    new_object = original_object.clone()
    print("The new object will connect to "\
          f"{new_object.database_hostname}:{new_object.database_port}")
    print("Is the new object the same instance of the original object? "\
          f"{original_object is new_object}")
    # pylint: disable=locally-disabled, comparison-with-itself
    print(f"Is the original the same instance of the original object? "\
          f"{original_object is original_object}")



if __name__ == "__main__":
    demo_prototype_pattern()
