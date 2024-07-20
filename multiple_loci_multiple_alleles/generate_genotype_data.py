import random
import itertools

def generate_alleles(num_alleles, loci_names):
    return {locus: [f"{locus}{i+1}" for i in range(num_alleles)] for locus in loci_names}

def generate_genotype_combinations(alleles):
    loci = list(alleles.keys())
    allele_pairs = {locus: list(itertools.combinations_with_replacement(alleles[locus], 2)) for locus in loci}
    all_combinations = list(itertools.product(*[allele_pairs[locus] for locus in loci]))
    return all_combinations

def generate_genotype_data(num_loci, num_alleles, population_size, loci_names=None, random_seed=0):
    random.seed(random_seed)

    if not loci_names:
        loci_names = [chr(i) for i in range(65, 65 + num_loci)]
    
    alleles = generate_alleles(num_alleles, loci_names)
    genotype_combinations = generate_genotype_combinations(alleles)
    
    genotype_counts = {}
    genotype_fitness = {}
    
    for genotype in genotype_combinations:
        count = random.randint(1, population_size // len(genotype_combinations))
        fitness = round(random.uniform(0.8, 1.0), 1)
        genotype_counts[genotype] = count
        genotype_fitness[genotype] = fitness
    
    return genotype_counts, genotype_fitness