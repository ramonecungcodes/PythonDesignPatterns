"""Module providing an example of the Facade design pattern."""
# pylint: disable=locally-disabled, too-few-public-methods

class ExtractCsv():
    """Example of loading data of a specific type"""

    @staticmethod
    def load():
        """Provides ability to load data from a source"""

        print("Data loaded from CSV file.")


class ExtractExcel():
    """Example of loading data of a specific type"""

    @staticmethod
    def load():
        """Provides ability to load data from a source"""

        print("Data loaded from Excel file.")


class ExtractS3():
    """Example of loading data of a specific type"""

    @staticmethod
    def load():
        """Provides ability to load data from a source"""

        print("Data loaded from S3 bucket.")


class ExtractAzureBlobStorage():
    """Example of loading data of a specific type"""

    @staticmethod
    def load():
        """Provides ability to load data from a source"""

        print("Data loaded from Azure Blob.")


class TransformData():
    """Example of fransforming data"""

    @staticmethod
    def load():
        """Provides ability to transform data"""

        print(f"Data transformed.")


class LoadDataToDatabase():
    """Example of saving data to a target system"""

    @staticmethod
    def load():
        """Provides ability to load data to a database"""

        print("Data loaded to database table!")


class Etl:
    """Base class for ETLs of various types"""

    steps = []

    def execute_etl(self):
        """Provides ability to perform a series of steps"""

        for step in self.steps:
            step.load()


class EtlForSystem1(Etl):
    """Example of ETL that loads data for a specific system"""

    steps = [ExtractCsv, TransformData, LoadDataToDatabase]


class EtlForSystem2(Etl):
    """Example of ETL that loads data for a specific system"""

    steps = [ExtractExcel, TransformData, LoadDataToDatabase]


class EtlForSystem3(Etl):
    """Example of ETL that loads data for a specific system"""

    steps = [ExtractAzureBlobStorage, TransformData, LoadDataToDatabase]


class EtlForSystem4(Etl):
    """Example of ETL that loads data for a specific system"""

    steps = [ExtractS3, TransformData, LoadDataToDatabase]


class DataWarehouse():
    """Defines a logical data warehouse"""

    def load_system1(self):
        """Loads data from a specific system"""

        print("Now loading system 1 data")
        EtlForSystem1().execute_etl()

    def load_system2(self):
        """Loads data from a specific system"""

        print("Now loading system 2 data")
        EtlForSystem2().execute_etl()

    def load_system3(self):
        """Loads data from a specific system"""

        print("Now loading system 3 data")
        EtlForSystem3().execute_etl()

    def load_system4(self):
        """Loads data from a specific system"""

        print("Now loading system 4 data")
        EtlForSystem4().execute_etl()


class ClientSystem():
    """Used to demo a client system using a data warehouse object"""

    def __init__(self) -> None:
        self.shutdown_systems()
        self.perform_data_warehouse_activities()
        self.resume_systems()

    def shutdown_systems(self):
        """Simulates shutting down the system"""
        print("All systems have been shut down.")

    def resume_systems(self):
        """Simulates resuming the system"""
        print("All systems have resumed operations.")

    def perform_data_warehouse_activities(self):
        """Simulates executing ETLs to load data from various systems"""
        edw = DataWarehouse()
        edw.load_system1()
        edw.load_system2()
        edw.load_system3()
        edw.load_system4()


def demo_facade_pattern():
    """Demo the Facade design pattern as implemented using the classes above"""
    ClientSystem()


if __name__ == "__main__":
    demo_facade_pattern()
