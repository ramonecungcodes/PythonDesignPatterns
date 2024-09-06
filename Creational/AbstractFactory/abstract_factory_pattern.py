from abc import ABC, abstractmethod
from enum import Enum


class ComputerEquipmentInterface(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


class MonitorEquipmentInterface(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


class WebcamEquipmentInterface(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


class MacMini(ComputerEquipmentInterface):
    name = "Mac Mini"

    def turn_on(self):
        print(f"{self.name} has turned on!")

    def turn_off(self):
        print(f"{self.name} has turned off!")


class MacbookAir(ComputerEquipmentInterface):
    name = "Macbook Air"

    def turn_on(self):
        print(f"{self.name} has turned on!")

    def turn_off(self):
        print(f"{self.name} has turned off!")


class MacbookPro(ComputerEquipmentInterface):
    name = "Macbook Pro"

    def turn_on(self):
        print(f"{self.name} has turned on!")

    def turn_off(self):
        print(f"{self.name} has turned off!")


class Monitor4k(MonitorEquipmentInterface):
    name = "4k Monitor"

    def turn_on(self):
        print(f"{self.name} has turned on!")

    def turn_off(self):
        print(f"{self.name} has turned off!")


class DualMonitors(MonitorEquipmentInterface):
    name = "Dual 4k Monitors"

    def turn_on(self):
        print(f"{self.name} has turned on!")

    def turn_off(self):
        print(f"{self.name} has turned off!")


class Webcam1080p(WebcamEquipmentInterface):
    name = "1080p Webcam"

    def turn_on(self):
        print(f"{self.name} has turned on!")

    def turn_off(self):
        print(f"{self.name} has turned off!")


class Webcam4k(WebcamEquipmentInterface):
    name = "4k Webcam"

    def turn_on(self):
        print(f"{self.name} has turned on!")

    def turn_off(self):
        print(f"{self.name} has turned off!")


class EmployeeEquipmentType(Enum):
    REMOTE = 1
    ONSITE = 2
    EXECUTIVE = 3
    CONTRACTOR = 4


class EquipmentFactoryInterface(ABC):
    """ Abstract factory """
    @property
    @abstractmethod
    def employee_equipment_type():
        pass

    @abstractmethod
    def define_monitor(self) -> MonitorEquipmentInterface:
        pass

    @abstractmethod
    def define_webcam(self) -> WebcamEquipmentInterface:
        pass

    @abstractmethod
    def define_computer(self) -> ComputerEquipmentInterface:
        pass


class RemoteEquipmentFactory(EquipmentFactoryInterface):
    """ Factory """
    employee_equipment_type = EmployeeEquipmentType.REMOTE

    def define_monitor(self):
        return Monitor4k()

    def define_computer(self):
        return MacbookAir()
    
    def define_webcam(self):
        return Webcam1080p()


class OnsiteEquipmentFactory(EquipmentFactoryInterface):
    employee_equipment_type = EmployeeEquipmentType.ONSITE

    def define_monitor(self):
        return DualMonitors()
    
    def define_computer(self):
        return MacMini()
    
    def define_webcam(self):
        return Webcam1080p()


class ExecutiveEquipmentFactory(EquipmentFactoryInterface):
    employee_equipment_type = EmployeeEquipmentType.EXECUTIVE

    def define_monitor(self):
        return DualMonitors()
    
    def define_computer(self):
        return MacMini()
    
    def define_webcam(self):
        return Webcam1080p()


class ContractorEquipmentFactory(EquipmentFactoryInterface):
    employee_equipment_type = EmployeeEquipmentType.CONTRACTOR

    def define_monitor(self):
        return Monitor4k()
    
    def define_computer(self):
        return MacMini()
    
    def define_webcam(self):
        return Webcam1080p()


def demo_abstract_factory():
    new_employee_equipment = ExecutiveEquipmentFactory()

    computer = new_employee_equipment.define_computer()
    monitor = new_employee_equipment.define_monitor()
    webcam = new_employee_equipment.define_webcam()

    computer.turn_on()
    monitor.turn_on()
    webcam.turn_on()

if __name__ == "__main__":
    demo_abstract_factory()
