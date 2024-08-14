from calc_N import calc_N

def calc_avg_fitness(genotype_data):
    """
    Calculate the average fitness of a population.

    """

    avg_fitness = 0
    for data in genotype_data.values():
        avg_fitness += (data['Nm'] + data['Nf']) * data['fitness']

    N  = calc_N(genotype_data)
    return avg_fitness / N