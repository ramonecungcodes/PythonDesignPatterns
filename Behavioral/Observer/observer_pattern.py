"""Module providing an example of the Observer design pattern."""

from abc import ABC, abstractmethod


class DiscountObserverInterface(ABC):
    """Provides an interface for discount notifications"""
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def discounts_have_started(self):
        """Allows concrete class to accept incoming notifications"""

    @abstractmethod
    def discounts_have_ended(self):
        """Allows concrete class to accept incoming notifications"""


class DiscountProducerInterface(ABC):
    """Example of a class that will notify clients of discounts"""
    def __init__(self):
        self._discount_observers = []

    @abstractmethod
    def request_notification(self, observer: DiscountObserverInterface):
        """Allows concrete class to request notifications"""

    @abstractmethod
    def cancel_request(self, observer: DiscountObserverInterface):
        """Allows concrete class to cancel notifications"""


class Customer(DiscountObserverInterface):
    """Concrete class representing a specific customer that can request discount notifications"""
    def discounts_have_started(self):
        print(f"{self.name} is excited for discounts!")

    def discounts_have_ended(self):
        print(f"{self.name} is sad discounts are over.")


class Warehouse(DiscountObserverInterface):
    """Concrete class representing a specific warehouse that can request discount notifications"""
    def discounts_have_started(self):
        print(f"{self.name} is preparing for more orders!")

    def discounts_have_ended(self):
        print(f"{self.name} is now preparing to receive inventory.")


class OrganizationalDepartment(DiscountObserverInterface):
    """Concrete class representing an internal department that can request discount notifications"""
    def discounts_have_started(self):
        print(f"{self.name} is ready to support Accounting's busy time!")

    def discounts_have_ended(self):
        print(f"{self.name} is back to regular operations")


class PricingOptimizer(DiscountProducerInterface):
    """Example of a concrete class that will notify observers that have requested notifications"""
    def request_notification(self, observer: DiscountObserverInterface):
        print(f"{observer.name} has requested notification.")
        self._discount_observers.append(observer)

    def cancel_request(self, observer: DiscountObserverInterface):
        print(f"{observer.name} has requested cancellation of notifications.")
        self._discount_observers.remove(observer)

    def notify_discount_start(self):
        """Allows the instance to nofity discounts have started"""
        print("Now notifying observers that discounts have started.")
        for observer in self._discount_observers:
            print(f"Notifying {observer.name} that discounts are starting.")
            observer.discounts_have_started()

    def notify_discount_end(self):
        """Allows instance to notify discounts have ended"""
        print("Now notifying observers that discounts have ended.")
        for observer in self._discount_observers:
            print(f"Notifying {observer.name} that discounts are ending.")
            observer.discounts_have_ended()


def demo_observer_pattern():
    """Demo the Observer design pattern as implemented using the classes above"""

    pricing_system = PricingOptimizer()

    sally = Customer("Sally")
    pat = Customer("Pat")
    # pylint: disable=locally-disabled, unused-variable
    bobby = Customer("Bobby")   # not used on purpose to show notifications don't go to all

    accounting = OrganizationalDepartment("Accounting")
    tech = OrganizationalDepartment("Information Technology")
    retail = OrganizationalDepartment("Retail")

    austin_warehouse = Warehouse("Austin Facility")
    boston_warehouse = Warehouse("Boston Facility")

    pricing_system.request_notification(sally)
    pricing_system.request_notification(pat)
    print("")
    pricing_system.request_notification(accounting)
    pricing_system.request_notification(tech)
    pricing_system.request_notification(retail)
    print("")
    pricing_system.request_notification(austin_warehouse)
    pricing_system.request_notification(boston_warehouse)
    print("")
    pricing_system.notify_discount_start()
    print("")
    pricing_system.notify_discount_end()

if __name__ == "__main__":
    demo_observer_pattern()
