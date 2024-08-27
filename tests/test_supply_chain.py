import unittest
from src.supply_chain import SupplyChainNetwork

class TestSupplyChain(unittest.TestCase):
    def setUp(self):
        self.network = SupplyChainNetwork(3, 4, 3, 5)

    def test_calculate_objectives(self):
        routes = [(0, 0, 0, 0), (1, 1, 1, 1), (2, 2, 2, 2)]
        cost, time, service = self.network.calculate_objectives(routes)
        self.assertTrue(cost > 0)
        self.assertTrue(time > 0)
        self.assertTrue(0 <= service <= 1)

if __name__ == '__main__':
    unittest.main()
