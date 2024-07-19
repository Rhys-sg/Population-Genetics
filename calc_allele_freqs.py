def calc_allele_freqs(genotype_freqs):
    """
    Calculate allele frequencies for multiple loci with given genotype frequencies.

    Args:
    - genotype_freqs: A dictionary with genotype frequencies for all loci.

    Returns:
    - A list of dictionaries, where each dictionary contains allele frequencies for a locus.
    """
    # Initialize dictionaries to keep track of allele counts for each locus
    allele_counts = [{} for _ in range(len(next(iter(genotype_freqs.keys()))))]
    total_alleles = [0] * len(allele_counts)
    
    # Loop through each genotype and its frequency
    for genotype, freq in genotype_freqs.items():
        for i, locus in enumerate(genotype):
            for allele in locus:
                if allele not in allele_counts[i]:
                    allele_counts[i][allele] = 0
                allele_counts[i][allele] += freq
        
            # Update total alleles for each locus
            total_alleles[i] += len(locus) * freq
    
    # Calculate allele frequencies for each locus
    allele_freqs = [
        {allele: count / total_alleles[i] for allele, count in locus_counts.items()}
        for i, locus_counts in enumerate(allele_counts)
    ]
    
    return allele_freqs

# genotype_freqs = {
#     (('A1', 'A2'), ('B1', 'B1')): 0.1250,
#     (('A1', 'A2'), ('B1', 'B2')): 0.2500,
#     (('A1', 'A2'), ('B2', 'B2')): 0.1250, 
#     (('A2', 'A2'), ('B1', 'B1')): 0.0625,
#     (('A2', 'A2'), ('B1', 'B2')): 0.1250,
#     (('A2', 'A2'), ('B2', 'B2')): 0.0625, 
#     (('A1', 'A1'), ('B1', 'B1')): 0.0625,
#     (('A1', 'A1'), ('B1', 'B2')): 0.1250,
#     (('A1', 'A1'), ('B2', 'B2')): 0.0625
# }

# print(calc_allele_freqs(genotype_freqs)) # Expected: [{'A1': 0.25, 'A2': 0.75}, {'B1': 0.375, 'B2': 0.625}]