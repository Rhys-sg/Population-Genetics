def calc_avg_fitness(genotype_freqs, genotype_fitness):
    """
    Calculate the average fitness of a population.

    Parameters
    - genotype_freqs: dict, the frequencies of each genotype in the population
    - genotype_fitness: dict, the fitness of each genotype

    Returns
    - avg_fitness: float, the average fitness of the population

    """

    avg_fitness = 0
    for genotype, freq in genotype_freqs.items():
        avg_fitness += freq * genotype_fitness[genotype]

    return avg_fitness