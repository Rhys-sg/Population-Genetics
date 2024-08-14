import itertools

def calc_next_genotype_freqs(allele_frequencs, covariance):
    """
    Calculate genotype frequencies for multiple loci with given allele frequencies.
    Calculation is based on the Hardy-Weinberg equilibrium and inlcudes covariance 
    between uniting gametes, which varies from:
        -1 (inbreeding avoidance)
         0 (random mating)
        +1 (inbreeding)
        
    HW and convariance formulas are:
        AA = p2 + pqf
        Aa = 2pq(1-f)
        Aa = q2 + pqf
    

    Args:
    - allele_frequencs: A list of dictionaries, where each dictionary contains allele frequencies for a locus.
                          e.g., [{'A1': 0.3, 'A2': 0.4, 'A3': 0.3}, {'B1': 0.2, 'B2': 0.5, 'B3': 0.3}, ...]

    Returns:
    - A dictionary with combined genotype frequencies for all loci.
    """
    # Generate all possible allele combinations for each locus
    locus_genotypes = []
    for locus in allele_frequencs:
        alleles = list(locus.keys())
        genotypes = [tuple(sorted((a1, a2))) for a1 in alleles for a2 in alleles]
        locus_genotypes.append(set(genotypes))  # Use set to remove duplicates

    # Generate all possible combined genotypes across loci
    combined_genotypes = list(itertools.product(*locus_genotypes))

    # Calculate frequencies for each combined genotype
    combined_genotype_freqs = {}
    for combined_genotype in combined_genotypes:
        freq = 1.0
        for idx, (a1, a2) in enumerate(combined_genotype):
            if a1 == a2:
                freq *= allele_frequencs[idx][a1] ** 2 + (allele_frequencs[idx][a1] * (1 - allele_frequencs[idx][a1]) * covariance)
            else:
                freq *= 2 * allele_frequencs[idx][a1] * allele_frequencs[idx][a2] * (1-covariance)
        combined_genotype_freqs[combined_genotype] = round(freq, 6)

    return combined_genotype_freqs