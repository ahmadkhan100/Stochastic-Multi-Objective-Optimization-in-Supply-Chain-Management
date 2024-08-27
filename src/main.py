from src.supply_chain import SupplyChainNetwork
from src.genetic_algorithm import GeneticAlgorithm

if __name__ == "__main__":
    # Parameters
    n_suppliers = 3
    n_manufacturers = 4
    n_warehouses = 3
    n_customers = 5
    n_routes = n_customers
    n_generations = 50
    pop_size = 20
    mutation_rate = 0.1

    # Initialize the supply chain network
    supply_chain = SupplyChainNetwork(n_suppliers, n_manufacturers, n_warehouses, n_customers)

    # Run the Genetic Algorithm
    ga = GeneticAlgorithm(supply_chain, n_generations, pop_size, mutation_rate)
    best_solution, best_evaluation = ga.run(n_routes)

    print(f"Best solution: {best_solution}")
    print(f"Best evaluation (Cost, Time, Service Level): {best_evaluation}")
