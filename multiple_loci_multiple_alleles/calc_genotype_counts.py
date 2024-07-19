def calc_genotype_counts(genotype_freq, pop, growth_rate):
    """
    Calculate genotype counts from genotype frequencies.

    Args:
    - genotype_freq (dict): A dictionary of genotype frequencies.
    - pop (int): The population size.
    - growth_rate (int): The growth rate of the population.

    Returns:
    - dict: A dictionary of genotypes and their counts.
    
    """

    return {genotype: int(freq * pop * growth_rate) for genotype, freq in genotype_freq.items()}