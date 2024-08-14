def calc_allele_freqs(allele_counts):
    """
    Calculate allele frequencies for multiple loci with given allele counts.

    Args:
    - allele_counts: A list of dictionaries, where each dictionary contains allele counts for a locus.

    Returns:
    - A list of dictionaries, where each dictionary contains allele frequencies for a locus.
    """
    allele_freqs = []
    for locus_counts in allele_counts:
        total_alleles = sum(locus_counts.values())
        locus_freqs = {allele: count / total_alleles for allele, count in locus_counts.items()}
        allele_freqs.append(locus_freqs)

    return allele_freqs