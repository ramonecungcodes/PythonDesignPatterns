import unittest
import Behavioral.Observer.observer_pattern as o

class Test_DiscountObserverInterface(unittest.TestCase):
    def test_DiscountObserverInterface_is_abstract_base_class(self):
        self.assertRaises(TypeError, o.DiscountObserverInterface, "test name")

    def test_DiscountProducerInterface_is_abstract_base_class(self):
        self.assertRaises(TypeError, o.DiscountProducerInterface)

    def test_PricingOptimizer_can_add_requests(self):
        object_to_notify = o.Customer("object")
        pricing_optimizer = o.PricingOptimizer()
        self.assertEqual(len(pricing_optimizer._discount_observers), 0)
        pricing_optimizer.request_notification(object_to_notify)
        self.assertEqual(len(pricing_optimizer._discount_observers), 1)

    def test_PricingOptimizer_can_remove_requests(self):
        object_to_notify = o.Customer("object")
        pricing_optimizer = o.PricingOptimizer()
        self.assertEqual(len(pricing_optimizer._discount_observers), 0)
        pricing_optimizer.request_notification(object_to_notify)
        self.assertEqual(len(pricing_optimizer._discount_observers), 1)
        pricing_optimizer.cancel_request(object_to_notify)
        self.assertEqual(len(pricing_optimizer._discount_observers), 0)


if __name__ == '__main__':
    unittest.main()
    