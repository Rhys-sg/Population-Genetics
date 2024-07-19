def calc_allele_counts(genotype_counts):
    """
    Calculate allele counts for multiple loci with given genotype counts.

    Args:
    - genotype_counts: A dictionary with genotype counts for all loci.

    Returns:
    - A list of dictionaries, where each dictionary contains allele counts for a locus.
    """
    allele_counts = [{} for _ in range(len(next(iter(genotype_counts.keys()))))]

    for genotype, count in genotype_counts.items():
        for i, locus in enumerate(genotype):
            for allele in locus:
                if allele not in allele_counts[i]:
                    allele_counts[i][allele] = 0
                allele_counts[i][allele] += count

    return allele_counts