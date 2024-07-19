def adj_by_fitness(genotype_freqs, genotype_fitness):
    """
    Adjust genotype frequencies by fitness.
    
    Args:
        genotype_freqs (dict): A dictionary of genotypes and their frequencies.
        genotype_fitness (dict): A dictionary of genotypes and their fitnesses.


    """
    
    return {key: genotype_freqs[key] * genotype_fitness[key] for key in genotype_freqs}
