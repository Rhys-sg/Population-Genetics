def calc_genotype_freqs(genotype_counts, pop):
    """
    Calculate genotype frequencies from genotype counts.

    Args:
    - genotype_counts (dict): A dictionary of genotype counts.
    - pop (int): The population size.

    Returns:
    - dict: A dictionary of genotypes and their frequencies.
    
    """

    return {genotype: count / pop for genotype, count in genotype_counts.items()}
