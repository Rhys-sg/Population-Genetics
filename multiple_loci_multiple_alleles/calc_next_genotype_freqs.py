import itertools

def calc_next_genotype_freqs(allele_frequencs):
    """
    Calculate genotype frequencies for multiple loci with given allele frequencies.

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
                freq *= allele_frequencs[idx][a1] ** 2
            else:
                freq *= 2 * allele_frequencs[idx][a1] * allele_frequencs[idx][a2]
        combined_genotype_freqs[combined_genotype] = round(freq, 6)

    return combined_genotype_freqs