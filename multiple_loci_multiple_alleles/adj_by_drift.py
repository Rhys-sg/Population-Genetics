import random

def adj_by_drift(genotype_counts, drift, pop_size, carrying_capacity):
    """
    Adjust genotype counts by a genetic drift.
    - Applied by multiplying each genotype frequency by a random number between 1-drift and 1+drift.
    - Rounds the rate of drift to the nearest whole number becuase you can't have a fraction of an genotype.
    - Scales the count of each genotype up or down by a random amount, relative to the original count.
    - adj_drift makes drift inversely relative to the population size with respect to carrying capacity.

    Args:
    - genotype_counts (dict): A dictionary of genotypes and their counts.
    - drift (float): The amount of genetic drift from 0 to 1.

    Returns:
    - dict: A dictionary of genotypes and their adjusted counts

    """

    adj_drift = drift / (pop_size / carrying_capacity)

    return {key: round(genotype_counts[key] * random.uniform(1-adj_drift, 1+adj_drift)) for key in genotype_counts}
