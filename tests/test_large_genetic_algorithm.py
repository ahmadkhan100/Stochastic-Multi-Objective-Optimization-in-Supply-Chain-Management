import unittest
import pandas as pd
import numpy as np
from src.supply_chain import SupplyChainNetwork
from src.genetic_algorithm import GeneticAlgorithm

class TestLargeGeneticAlgorithm(unittest.TestCase):
    def setUp(self):
        # Load the large dataset
        self.df = pd.read_csv('data/large_supply_chain_data.csv')

        # Initialize the SupplyChainNetwork with realistic numbers
        n_suppliers = 10
        n_manufacturers = 15
        n_warehouses = 10
        n_customers = 20

        self.network = SupplyChainNetwork(n_suppliers, n_manufacturers, n_warehouses, n_customers)

        # Parse the CSV to extract costs, times, and service levels
        self.network.costs = {
            'supplier_manufacturer': self.df[(self.df['Entity Type'] == 'Supplier') & (self.df['To'].str.contains('MAN'))]
                                      .pivot(index='From', columns='To', values='Cost').fillna(0).to_numpy(),
            'manufacturer_warehouse': self.df[(self.df['Entity Type'] == 'Manufacturer') & (self.df['To'].str.contains('WH'))]
                                      .pivot(index='From', columns='To', values='Cost').fillna(0).to_numpy(),
            'warehouse_customer': self.df[(self.df['Entity Type'] == 'Warehouse') & (self.df['To'].str.contains('CUS'))]
                                      .pivot(index='From', columns='To', values='Cost').fillna(0).to_numpy()
        }
        self.network.times = {
            'supplier_manufacturer': self.df[(self.df['Entity Type'] == 'Supplier') & (self.df['To'].str.contains('MAN'))]
                                      .pivot(index='From', columns='To', values='Time').fillna(0).to_numpy(),
            'manufacturer_warehouse': self.df[(self.df['Entity Type'] == 'Manufacturer') & (self.df['To'].str.contains('WH'))]
                                      .pivot(index='From', columns='To', values='Time').fillna(0).to_numpy(),
            'warehouse_customer': self.df[(self.df['Entity Type'] == 'Warehouse') & (self.df['To'].str.contains('CUS'))]
                                      .pivot(index='From', columns='To', values='Time').fillna(0).to_numpy()
        }
        self.network.service_levels = {
            'supplier_manufacturer': self.df[(self.df['Entity Type'] == 'Supplier') & (self.df['To'].str.contains('MAN'))]
                                      .pivot(index='From', columns='To', values='Service Level').fillna(0).to_numpy(),
            'manufacturer_warehouse': self.df[(self.df['Entity Type'] == 'Manufacturer') & (self.df['To'].str.contains('WH'))]
                                      .pivot(index='From', columns='To', values='Service Level').fillna(0).to_numpy(),
            'warehouse_customer': self.df[(self.df['Entity Type'] == 'Warehouse') & (self.df['To'].str.contains('CUS'))]
                                      .pivot(index='From', columns='To', values='Service Level').fillna(0).to_numpy()
        }

        # Initialize the GeneticAlgorithm with realistic parameters
        self.ga = GeneticAlgorithm(self.network, n_generations=10, pop_size=20, mutation_rate=0.1)

    def test_genetic_algorithm_large_data(self):
        n_routes = 20  # Example: one route per customer
        best_solution, best_evaluation = self.ga.run(n_routes)
        
        # We expect the algorithm to return a valid solution
        self.assertIsInstance(best_solution, list)
        self.assertTrue(len(best_solution) > 0)
        self.assertTrue(best_evaluation[0] > 0)  # cost
        self.assertTrue(best_evaluation[1] > 0)  # time
        self.assertTrue(0 <= best_evaluation[2] <= 1)  # service level

if __name__ == '__main__':
    unittest.main()
