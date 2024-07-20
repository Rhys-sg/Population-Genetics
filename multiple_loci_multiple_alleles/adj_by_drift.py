import random

def adj_by_drift(genotype_counts, drift, pop_size, carrying_capacity):
    """
    Adjust genotype counts by a genetic drift.
    - Applied by multiplying each genotype frequency by a random number between 1-drift and 1+drift.
    - Rounds the rate of drift to the nearest whole number because you can't have a fraction of a genotype.
    - Scales the count of each genotype up or down by a random amount, relative to the original count.
    - adj_drift makes drift inversely relative to the population size with respect to carrying capacity.

    Args:
    - genotype_counts (dict): A dictionary of genotypes and their counts.
    - drift (float): The amount of genetic drift from 0 to 1.
    - pop_size (int): The size of the population.
    - carrying_capacity (int): The maximum size of the population.

    Returns:
    - dict: A dictionary of genotypes and their adjusted counts
    """

    norm_adj_drift = normalize_adj_drift(drift, pop_size, carrying_capacity)

    return {key: round(genotype_counts[key] * random.uniform(1-norm_adj_drift, 1+norm_adj_drift)) for key in genotype_counts}

def normalize_adj_drift(drift, pop_size, carrying_capacity):
    """
    Helper function to normalize the drift based on the population size and carrying capacity.
    - Drift is inversely proportional to the population size with respect to the carrying capacity.
    - The maximum drift occurs when the population size is 1.
    - The minimum drift occurs when the population is at carrying capacity.

    Args:
    - drift (float): The amount of genetic drift from 0 to 1.
    - pop_size (int): The size of the population.
    - carrying_capacity (int): The maximum size of the population.

    Returns:
    - float: The normalized drift from 0 to 1.
    """
    if carrying_capacity == 0:
        raise ValueError("Carrying capacity cannot be zero")

    if pop_size == 0:
        raise ValueError("Population size cannot be zero")

    max_adj_drift = drift
    min_adj_drift = 0

    adj_drift = drift * (1 - (pop_size / carrying_capacity))
    
    normalized_adj_drift = (adj_drift - min_adj_drift) / (max_adj_drift - min_adj_drift)
    normalized_adj_drift = max(0, min(1, normalized_adj_drift))
    
    return normalized_adj_drift
