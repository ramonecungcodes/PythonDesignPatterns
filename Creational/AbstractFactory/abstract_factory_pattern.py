"""Module providing an example of the Abstract Factory design pattern."""

from abc import ABC, abstractmethod
from enum import Enum


class ComputerEquipmentInterface(ABC):
    """Interface that defines functionality for computers."""

    @property
    @abstractmethod
    def name(self) -> str:
        """Getter for the property 'name'"""

    @abstractmethod
    def turn_on(self):
        """Define functionality for turning on the instance of a computer."""

    @abstractmethod
    def turn_off(self):
        """Define functionality for turning of the instance of a computer."""


class MonitorEquipmentInterface(ABC):
    """Interface that defines functionality for monitors."""

    @property
    @abstractmethod
    def name(self) -> str:
        """Getter for the property 'name'"""

    @abstractmethod
    def turn_on(self):
        """Define functionality for turning on the instance of a monitor."""

    @abstractmethod
    def turn_off(self):
        """Define functionality for turning off the instance of a monitor."""


class WebcamEquipmentInterface(ABC):
    """Interface that defines functionality for webcames."""

    @property
    @abstractmethod
    def name(self) -> str:
        """Getter for the property 'name'"""

    @abstractmethod
    def turn_on(self):
        """Define functionality for turning on the instance of a webcam."""

    @abstractmethod
    def turn_off(self):
        """Define functionality for turning off the instance of a webcam."""


class MacMini(ComputerEquipmentInterface):
    """Concrete definition of a type of computer."""

    name = "Mac Mini"

    def turn_on(self):
        print(f"{self.name} has turned on!")

    def turn_off(self):
        print(f"{self.name} has turned off!")


class MacbookAir(ComputerEquipmentInterface):
    """Concrete definition of a type of computer."""

    name = "Macbook Air"

    def turn_on(self):
        print(f"{self.name} has turned on!")

    def turn_off(self):
        print(f"{self.name} has turned off!")


class MacbookPro(ComputerEquipmentInterface):
    """Concrete definition of a type of computer."""

    name = "Macbook Pro"

    def turn_on(self):
        print(f"{self.name} has turned on!")

    def turn_off(self):
        print(f"{self.name} has turned off!")


class Monitor4k(MonitorEquipmentInterface):
    """Concrete definition of a type of monitor."""

    name = "4k Monitor"

    def turn_on(self):
        print(f"{self.name} has turned on!")

    def turn_off(self):
        print(f"{self.name} has turned off!")


class DualMonitors(MonitorEquipmentInterface):
    """Concrete definition of a type of monitor."""

    name = "Dual 4k Monitors"

    def turn_on(self):
        print(f"{self.name} has turned on!")

    def turn_off(self):
        print(f"{self.name} has turned off!")


class Webcam1080p(WebcamEquipmentInterface):
    """Concrete definition of a type of webcam."""

    name = "1080p Webcam"

    def turn_on(self):
        print(f"{self.name} has turned on!")

    def turn_off(self):
        print(f"{self.name} has turned off!")


class Webcam4k(WebcamEquipmentInterface):
    """Concrete definition of a type of webcam."""

    name = "4k Webcam"

    def turn_on(self):
        print(f"{self.name} has turned on!")

    def turn_off(self):
        print(f"{self.name} has turned off!")


class EmployeeEquipmentType(Enum):
    """Defines the various classes of employee based on equipment."""

    REMOTE = 1
    ONSITE = 2
    EXECUTIVE = 3
    CONTRACTOR = 4


class EquipmentFactoryInterface(ABC):
    """ Abstract factory """

    @property
    @abstractmethod
    def employee_equipment_type(self):
        """A property that defines what class of equipment an employee can get."""

    @abstractmethod
    def define_monitor(self) -> MonitorEquipmentInterface:
        """Create an instance that represents a monitor."""

    @abstractmethod
    def define_webcam(self) -> WebcamEquipmentInterface:
        """Create an instance that represents a webcam."""

    @abstractmethod
    def define_computer(self) -> ComputerEquipmentInterface:
        """Create an instance that represents a computer."""


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
    """ Factory """

    employee_equipment_type = EmployeeEquipmentType.ONSITE

    def define_monitor(self):
        return DualMonitors()

    def define_computer(self):
        return MacMini()

    def define_webcam(self):
        return Webcam1080p()


class ExecutiveEquipmentFactory(EquipmentFactoryInterface):
    """ Factory """

    employee_equipment_type = EmployeeEquipmentType.EXECUTIVE

    def define_monitor(self):
        return DualMonitors()

    def define_computer(self):
        return MacMini()

    def define_webcam(self):
        return Webcam1080p()


class ContractorEquipmentFactory(EquipmentFactoryInterface):
    """ Factory """

    employee_equipment_type = EmployeeEquipmentType.CONTRACTOR

    def define_monitor(self):
        return Monitor4k()

    def define_computer(self):
        return MacMini()

    def define_webcam(self):
        return Webcam1080p()


def demo_abstract_factory():
    """Test out the functionality of the classes defined above."""

    new_employee_equipment = ExecutiveEquipmentFactory()

    computer = new_employee_equipment.define_computer()
    monitor = new_employee_equipment.define_monitor()
    webcam = new_employee_equipment.define_webcam()

    computer.turn_on()
    monitor.turn_on()
    webcam.turn_on()

if __name__ == "__main__":
    demo_abstract_factory()
