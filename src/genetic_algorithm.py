import numpy as np
from src.supply_chain import SupplyChainNetwork

class GeneticAlgorithm:
    def __init__(self, supply_chain_network, n_generations, pop_size, mutation_rate):
        self.network = supply_chain_network
        self.n_generations = n_generations
        self.pop_size = pop_size
        self.mutation_rate = mutation_rate

    def initialize_population(self, n_routes):
        population = []
        for _ in range(self.pop_size):
            individual = [
                (
                    np.random.randint(0, self.network.n_suppliers),
                    np.random.randint(0, self.network.n_manufacturers),
                    np.random.randint(0, self.network.n_warehouses),
                    np.random.randint(0, self.network.n_customers)
                ) for _ in range(n_routes)
            ]
            population.append(individual)
        return population

    def evaluate_population(self, population):
        return [self.network.calculate_objectives(individual) for individual in population]

    def select_parents(self, population, evaluations):
        selected = []
        for _ in range(len(population)):
            participants = np.random.choice(len(population), 3)
            best_idx = participants[np.argmin([evaluations[i][0] for i in participants])]
            selected.append(population[best_idx])
        return selected

    def crossover(self, parent1, parent2):
        point = np.random.randint(1, len(parent1) - 1)
        child1 = parent1[:point] + parent2[point:]
        child2 = parent2[:point] + parent1[point:]
        return child1, child2

    def mutate(self, individual):
        if np.random.rand() < self.mutation_rate:
            route_idx = np.random.randint(len(individual))
            individual[route_idx] = (
                np.random.randint(0, self.network.n_suppliers),
                np.random.randint(0, self.network.n_manufacturers),
                np.random.randint(0, self.network.n_warehouses),
                np.random.randint(0, self.network.n_customers)
            )
        return individual

    def run(self, n_routes):
        population = self.initialize_population(n_routes)
        
        for generation in range(self.n_generations):
            evaluations = self.evaluate_population(population)
            parents = self.select_parents(population, evaluations)
            
            new_population = []
            for i in range(0, len(parents), 2):
                parent1 = parents[i]
                parent2 = parents[i + 1 if i + 1 < len(parents) else 0]
                child1, child2 = self.crossover(parent1, parent2)
                new_population.append(self.mutate(child1))
                new_population.append(self.mutate(child2))
            
            population = new_population

        final_evaluations = self.evaluate_population(population)
        best_idx = np.argmin([eval[0] for eval in final_evaluations])
        return population[best_idx], final_evaluations[best_idx]
