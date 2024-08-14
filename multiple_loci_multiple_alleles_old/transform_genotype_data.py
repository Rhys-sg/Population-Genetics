def transform_genotype_data(genotype_data):
    """
    Transform genotype data from one dictionary to separate dictionaries

    Args:
    - genotypes: A dictionary with genotype data for each genotype.

    Returns:
    - genotype_m: The males in the population with each genotype
    - genotype_f: The females in the population with each genotype
    - genotype_fitness: The fitness of each genotype

    """
    genotype_m = {}
    genotype_f = {}
    genotype_fitness = {}

    for genotype, data in genotype_data.items():
        genotype_m[genotype] = data['male']
        genotype_f[genotype] = data['female']
        genotype_fitness[genotype] = data['fitness']
    
    return genotype_m, genotype_f, genotype_fitness


def calc_genotype_counts_from_mf(genotype_m, genotype_f):
    """
    Calculate the total number of individuals with each genotype.

    Args:
    - genotype_m: The number of males in the population with each genotype
    - genotype_f: The number of females in the population with each genotype

    Returns:
    - genotype_counts: The total number of individuals with each genotype

    """

    genotype_counts = {}
    for genotype in genotype_m.keys():
        genotype_counts[genotype] = genotype_m[genotype] + genotype_f[genotype]

    return genotype_counts


def calc_sex_counts(genotype_m, genotype_f):
    """
    Calculate the total number males and females in the population.
    Args:
    - genotype_m: The number of males in the population with each genotype
    - genotype_f: The number of females in the population with each genotype

    Returns
    - Nm: The total number males
    - Nf: The total number females

    """

    Nm = sum(genotype_m.values())
    Nf = sum(genotype_f.values())

    return Nm, Nf