"""Module providing an example of the Prototype design pattern."""


from abc import ABC, abstractmethod


class PrototypeInterface(ABC):
    @abstractmethod
    def clone(self):
        pass

class DataLoadInterface(ABC):
    @abstractmethod
    def attempt_data_load(self):
        pass


class ExpensiveDatabaseDataLoad(DataLoadInterface, PrototypeInterface):
    def __init__(self, data_set: str) -> None:
        self.database_hostname = "MYHOST"
        self.database_port = 80
        self.data_set = data_set
    
    def perform_expensive_data_load():
        pass
    
    def attempt_data_load(self):
        self.perform_expensive_data_load()

    def clone(self):
        new_instance = ExpensiveDatabaseDataLoad(self.data_set)
        new_instance.database_hostname = self.database_hostname
        new_instance.database_port = self.database_port
        return new_instance
    

class ExpensiveNetworkFileLoad(DataLoadInterface, PrototypeInterface):
    def __init__(self):
        self.unc_path = "\\server\folder\file.txt"
        self.target_path = "/home/$user/folder"

    def load_huge_data_file():
        pass
    
    def attempt_data_load(self):
        self.load_huge_data_file()

    def clone(self):
        new_instance = ExpensiveNetworkFileLoad()
        new_instance.unc_path = self.unc_path
        new_instance.target_path = self.target_path
        return new_instance


def demo_prototype_pattern():
    original_object = ExpensiveDatabaseDataLoad("SALES_DATA")
    print(f"The original object's will connect to {original_object.database_hostname}:{original_object.database_port}")
    new_object = original_object.clone()
    print(f"The new object will connect to {new_object.database_hostname}:{new_object.database_port}")
    print(f"Is the new object the same instance of the original object? {original_object is new_object}")
    print(f"Is the original the same instance of the original object? {original_object is original_object}")
    


if __name__ == "__main__":
    demo_prototype_pattern()
