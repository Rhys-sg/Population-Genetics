import itertools
from collections import defaultdict
import random

def generate_genotype_data(loci, alleles, Nm_min, Nm_max, Nf_min, Nf_max, seed=None):
    """
    Generate all possible genotypes given loci and alleles, with random fitness values,
    and specified ranges for the number of males and females.

    Parameters:
    loci (int): The number of loci.
    alleles (int): The number of alleles per locus.
    Nm_min (int): The minimum number of males for each genotype.
    Nm_max (int): The maximum number of males for each genotype.
    Nf_min (int): The minimum number of females for each genotype.
    Nf_max (int): The maximum number of females for each genotype.
    seed (int, optional): Random seed for reproducibility.

    Returns:
    dict: Dictionary with all possible genotypes and properties for 'male', 'female', and 'fitness'.
    """
    if seed is not None:
        random.seed(seed)

    loci_letters = [chr(ord('A') + i) for i in range(loci)]
    alleles_numbers = [f"{loci_letters[i]}{j+1}" for i in range(loci) for j in range(alleles)]

    def get_combinations(alleles):
        return list(itertools.combinations_with_replacement(alleles, 2))

    all_locus_combinations = [get_combinations(alleles_numbers[i*alleles:(i+1)*alleles]) for i in range(loci)]

    genotypes = list(itertools.product(*all_locus_combinations))
    
    genotype_data = defaultdict(lambda: {
        'male': random.randint(Nm_min, Nm_max), 
        'female': random.randint(Nf_min, Nf_max), 
        'fitness': round(random.uniform(0, 1), 1)
    })

    for genotype in genotypes:
        sorted_genotype = tuple(tuple(sorted(pair)) for pair in genotype)
        genotype_data[sorted_genotype]

    # Set fitness to 1 for a random genotype to emulate relative fitness
    random_genotype = random.choice(list(genotype_data.keys()))
    genotype_data[random_genotype]['fitness'] = 1.0

    return dict(genotype_data)