from abc import ABC, abstractmethod


class DiscountObserverInterface(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def discounts_have_started(self):
        pass

    @abstractmethod
    def discounts_have_ended(self):
        pass


class DiscountProducerInterface(ABC):
    def __init__(self):
        self._discount_observers = []

    @abstractmethod
    def request_notification(self, observer: DiscountObserverInterface):
        pass

    @abstractmethod
    def cancel_request(self, observer: DiscountObserverInterface):
        pass


class Customer(DiscountObserverInterface):
    def discounts_have_started(self):
        print(f"{self.name} is excited for discounts!")

    def discounts_have_ended(self):
        print(f"{self.name} is sad discounts are over.")
    

class Warehouse(DiscountObserverInterface):
    def discounts_have_started(self):
        print(f"{self.name} is preparing for more orders!")

    def discounts_have_ended(self):
        print(f"{self.name} is now preparing to receive inventory.")
    

class OrganizationalDepartment(DiscountObserverInterface):
    def discounts_have_started(self):
        print(f"{self.name} is ready to support Accounting's busy time!")

    def discounts_have_ended(self):
        print(f"{self.name} is back to regular operations")
    

class PricingOptimizer(DiscountProducerInterface):
    def request_notification(self, observer: DiscountObserverInterface):
        print(f"{observer.name} has requested notification.")
        self._discount_observers.append(observer)

    def cancel_request(self, observer: DiscountObserverInterface):
        print(f"{observer.name} has requested cancellation of notifications.")
        self._discount_observers.remove(observer)

    def notify_discount_start(self):
        print("Now notifying observers that discounts have started.")
        for observer in self._discount_observers:
            print(f"Notifying {observer.name} that discounts are starting.")
            observer.discounts_have_started()

    def notify_discount_end(self):
        print("Now notifying observers that discounts have ended.")
        for observer in self._discount_observers:
            print(f"Notifying {observer.name} that discounts are ending.")
            observer.discounts_have_ended()


def demo_observer_pattern():
    pricing_system = PricingOptimizer()

    sally = Customer("Sally")
    pat = Customer("Pat")
    bobby = Customer("Bobby")

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

