import numpy as np

class SupplyChainNetwork:
    def __init__(self, n_suppliers, n_manufacturers, n_warehouses, n_customers):
        np.random.seed(42)
        self.n_suppliers = n_suppliers
        self.n_manufacturers = n_manufacturers
        self.n_warehouses = n_warehouses
        self.n_customers = n_customers
        
        # Generate costs, times, and service levels
        self.costs = {
            'supplier_manufacturer': np.random.randint(1, 100, (n_suppliers, n_manufacturers)),
            'manufacturer_warehouse': np.random.randint(1, 100, (n_manufacturers, n_warehouses)),
            'warehouse_customer': np.random.randint(1, 100, (n_warehouses, n_customers))
        }
        
        self.times = {
            'supplier_manufacturer': np.random.randint(1, 10, (n_suppliers, n_manufacturers)),
            'manufacturer_warehouse': np.random.randint(1, 10, (n_manufacturers, n_warehouses)),
            'warehouse_customer': np.random.randint(1, 10, (n_warehouses, n_customers))
        }
        
        self.service_levels = {
            'supplier_manufacturer': np.random.rand(n_suppliers, n_manufacturers),
            'manufacturer_warehouse': np.random.rand(n_manufacturers, n_warehouses),
            'warehouse_customer': np.random.rand(n_warehouses, n_customers)
        }
        
        # Customer demand
        self.customer_demand = np.random.randint(50, 150, n_customers)

    def calculate_objectives(self, routes):
        total_cost = 0
        total_time = 0
        total_service = 0
        
        for i, route in enumerate(routes):
            supplier, manufacturer, warehouse, customer = route
            
            total_cost += self.costs['supplier_manufacturer'][supplier, manufacturer] + \
                          self.costs['manufacturer_warehouse'][manufacturer, warehouse] + \
                          self.costs['warehouse_customer'][warehouse, customer]
            
            total_time += self.times['supplier_manufacturer'][supplier, manufacturer] + \
                          self.times['manufacturer_warehouse'][manufacturer, warehouse] + \
                          self.times['warehouse_customer'][warehouse, customer]
            
            total_service += self.service_levels['supplier_manufacturer'][supplier, manufacturer] * \
                             self.service_levels['manufacturer_warehouse'][manufacturer, warehouse] * \
                             self.service_levels['warehouse_customer'][warehouse, customer]
        
        avg_service_level = total_service / len(routes)
        
        return total_cost, total_time, avg_service_level
