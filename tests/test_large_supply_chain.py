import unittest
import pandas as pd
import numpy as np
from src.supply_chain import SupplyChainNetwork

class TestLargeSupplyChain(unittest.TestCase):
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

    def test_calculate_objectives_large_data(self):
        # Example of a possible route assignment (simplified for demonstration)
        routes = [
            ('SUP_1', 'MAN_1', 'WH_1', 'CUS_1'),
            ('SUP_2', 'MAN_2', 'WH_2', 'CUS_2'),
            ('SUP_3', 'MAN_3', 'WH_3', 'CUS_3'),
            ('SUP_4', 'MAN_4', 'WH_4', 'CUS_4')
        ]
        cost, time, service = self.network.calculate_objectives(routes)
        # We expect these values to be positive and realistic
        self.assertTrue(cost > 0)
        self.assertTrue(time > 0)
        self.assertTrue(0 <= service <= 1)

if __name__ == '__main__':
    unittest.main()
