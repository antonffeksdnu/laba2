import random
import math

# Функція, що обчислює значення заданої функції
def eval_func(x, y, z):
    result = 1 / (1 + (x - 2) ** 2 + (y + 1) ** 2 + (z - 1) ** 2)
    return result,

# Функція для створення початкової популяції
def create_population(size):
    population = []
    for _ in range(size):
        chromosome = [random.uniform(-18, 18) for _ in range(3)]  # Генеруємо хромосому з трьох випадкових чисел в діапазоні [-18, 18]
        population.append(chromosome)
    return population

# Функція для оцінки фітнес-функції для кожної хромосоми в популяції
def evaluate_population(population):
    evaluated_pop = []
    for chromosome in population:
        fitness = eval_func(*chromosome)
        evaluated_pop.append((chromosome, fitness))
    return evaluated_pop

# Функція для вибору батьків з популяції на основі турнірного відбору
def select_parents(evaluated_pop, num_parents):
    parents = []
    for _ in range(num_parents):
        tournament_size = min(3, len(evaluated_pop))  # Розмір турніру - 3 або кількість доступних хромосом
        tournament = random.sample(evaluated_pop, tournament_size)  # Випадково вибираємо хромосоми для турніру
        winner = max(tournament, key=lambda x: x[1])  # Обираємо хромосому з найкращим значенням фітнесу
        parents.append(winner[0])
    return parents

# Функція для розмноження (одноточковий кросовер)
def crossover(parents, num_offsprings):
    offsprings = []
    for _ in range(num_offsprings):
        parent1, parent2 = random.sample(parents, 2)  # Випадково вибираємо двох батьків
        crossover_point = random.randint(1, len(parent1) - 1)  # Випадково обираємо точку кросоверу
        offspring = parent1[:crossover_point] + parent2[crossover_point:]  # Об'єднуємо гени батьків
        offsprings.append(offspring)
    return offsprings

# Функція для мутації (заміна одного гена випадковим значенням)
def mutate(offsprings, mutation_rate):
    mutated_offsprings = []
    for offspring in offsprings:
        if random.random() < mutation_rate:
            gene_to_mutate = random.randint(0, len(offspring) - 1)  # Випадково вибираємо ген для мутації
            offspring[gene_to_mutate] = random.uniform(-4, 4)  # Замінюємо ген на нове випадкове значення
        mutated_offsprings.append(offspring)
    return mutated_offsprings

# Головна функція генетичного алгоритму
def genetic_algorithm(population_size, num_generations, num_parents, num_offsprings, mutation_rate):
    population = create_population(population_size)

    for _ in range(num_generations):
        evaluated_pop = evaluate_population(population)
        parents = select_parents(evaluated_pop, num_parents)
        offsprings = crossover(parents, num_offsprings)
        mutated_offsprings = mutate(offsprings, mutation_rate)
        population = parents + mutated_offsprings

    best_chromosome = max(evaluate_population(population), key=lambda x: x[1])[0]
    return best_chromosome

# Задання параметрів генетичного алгоритму
population_size = 25
num_generations = 20
num_parents = 9
num_offsprings = 8
mutation_rate = 0.09

# Запуск генетичного алгоритму
best_chromosome = genetic_algorithm(population_size, num_generations, num_parents, num_offsprings, mutation_rate)
best_fitness = eval_func(*best_chromosome)[0]

print("Найкраща хромосома:", best_chromosome)
print("Найкраще значення функції:", best_fitness)
