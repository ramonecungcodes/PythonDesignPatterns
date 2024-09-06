"""Module providing an example of the Facade design pattern."""

class ExtractCsv():
    def load(self):
        print(f"Data loaded from CSV file.")


class ExtractExcel():
    def load(self):
        print(f"Data loaded from Excel file.")


class ExtractS3():
    def load(self):
        print(f"Data loaded from S3 bucket.")


class ExtractAzureBlobStorage():
    def load(self):
        print(f"Data loaded from Azure Blob.")


class TransformData():
    def load(self):
        print(f"Data transformed.")


class LoadDataToDatabase():
    def load(self):
        print(f"Data loaded to database table!")


class Etl:
    def execute_etl(self):
        for step in self.steps:
            step.load()


class EtlForSystem1(Etl):
    steps = [ExtractCsv, TransformData, LoadDataToDatabase]


class EtlForSystem2(Etl):
    steps = [ExtractExcel, TransformData, LoadDataToDatabase]


class EtlForSystem3(Etl):
    steps = [ExtractAzureBlobStorage, TransformData, LoadDataToDatabase]


class EtlForSystem4(Etl):
    steps = [ExtractS3, TransformData, LoadDataToDatabase]


class DataWarehouse():
    def load_system1(self):
        print("Now loading system 1 data")
        EtlForSystem1().execute_etl()

    def load_system2(self):
        print("Now loading system 2 data")
        EtlForSystem2().execute_etl()

    def load_system3(self):
        print("Now loading system 3 data")
        EtlForSystem3().execute_etl()

    def load_system4(self):
        print("Now loading system 4 data")
        EtlForSystem4().execute_etl()


class ClientSystem():
    def __init__(self) -> None:
        self.shutdown_systems()
        self.perform_data_warehouse_activities()
        self.resume_systems()

    def shutdown_systems(self):
        print("All systems have been shut down.")

    def resume_systems(self):
        print("All systems have resumed operations.")

    def perform_data_warehouse_activities(self):
        edw = DataWarehouse()
        edw.load_system1()
        edw.load_system2()
        edw.load_system3()
        edw.load_system4()


def demo_facade_pattern():
    ClientSystem()


if __name__ == "__main__":
    demo_facade_pattern()
