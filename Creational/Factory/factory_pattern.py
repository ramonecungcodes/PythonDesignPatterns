"""Module providing an example of the Factory design pattern."""

from abc import ABC, abstractmethod
from enum import Enum


class DeliveryInterface(ABC):
    """ Abstract class/interface to provide package transportation services. """

    @abstractmethod
    def get_package(self) -> None:
        pass

    @abstractmethod
    def dropoff_package(self) -> None:
        pass


class UpsDelivery(DeliveryInterface):
    """ Concrete implementation of the delivery interface """

    def get_package(self) -> None:
        print("UPS now has the package!")

    def dropoff_package(self) -> None:
        print("UPS has delivered the package!")


class FedExDelivery(DeliveryInterface):
    """ Concrete implementation of the delivery interface """

    def get_package() -> None:
        print("FedEx now has the package!")

    def dropoff_package() -> None:
        print("FedEx has delivered the package!")


class InHouseDelivery(DeliveryInterface):
    """ Concrete implementation of the delivery interface """

    def get_package(self) -> None:
        print("Pat now has the package!")

    def dropoff_package(self) -> None:
        print("Pat has delivered the package!")


class DeliveryType(Enum):
    DOMESTIC = 1
    INTERNATIONAL = 2
    LOCAL = 3


class DeliveryFactory():
    """ Class that provides factory functionality. It creates instances of DeliveryInterface subclasses. """

    @staticmethod
    def create_delivery_service(delivery_type: DeliveryType) -> DeliveryInterface:
        match delivery_type:
            case DeliveryType.DOMESTIC:
                return UpsDelivery()
            case DeliveryType.INTERNATIONAL:
                return FedExDelivery()
            case DeliveryType.LOCAL:
                return InHouseDelivery()


def demo_factory() -> None:
    """ 
    Imagine there was code that received a package from the warehouse, determined the 
    DeliveryType based on the address and now we need to ship it off...
    """

    package_delivery_service = DeliveryFactory.create_delivery_service(DeliveryType.DOMESTIC)
    package_delivery_service.get_package()
    package_delivery_service.dropoff_package()


if __name__ == "__main__":
    demo_factory()
