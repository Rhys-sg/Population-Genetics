def adj_by_fitness(genotype_counts, genotype_fitness):
    """
    Adjust genotype counts by fitness.
    
    Args:
    - genotype_counts (dict): A dictionary of genotypes and their counts.
    - genotype_fitness (dict): A dictionary of genotypes and their fitnesses.

    Returns:
    - dict: A dictionary of genotypes and their adjusted counts

    """
    
    return {key: genotype_counts[key] * genotype_fitness[key] for key in genotype_counts}
