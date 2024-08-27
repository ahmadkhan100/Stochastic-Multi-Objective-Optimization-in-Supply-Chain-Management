import unittest
from src.supply_chain import SupplyChainNetwork
from src.genetic_algorithm import GeneticAlgorithm

class TestGeneticAlgorithm(unittest.TestCase):
    def setUp(self):
        self.network = SupplyChainNetwork(3, 4, 3, 5)
        self.ga = GeneticAlgorithm(self.network, 10, 10, 0.1)

    def test_initialize_population(self):
        population = self.ga.initialize_population(5)
        self.assertEqual(len(population), 10)

    def test_evaluate_population(self):
        population = self.ga.initialize_population(5)
        evaluations = self.ga.evaluate_population(population)
        self.assertEqual(len(evaluations), 10)
        for eval in evaluations:
            self.assertTrue(len(eval) == 3)

if __name__ == '__main__':
    unittest.main()
