def adj_by_mutation(allele_counts, mutations):
    """
    Adjust allele counts by mutating one allele into another, given a frequency.
    Rounds the rate to the nearest whole number becuase you can't have a fraction of an allele.

    Parameters:
    - allele_counts (list): A list of dictionaries representing allele counts.
    - mutations (list): A list of dictionaries representing the rate at which a given genotype mutates into another given genotype.

    Returns:
    - list: A list of dictionaries representing adjusted allele counts

    """
    for i, mutation in enumerate(mutations):
        for key, value in mutation.items():
            rate = round(allele_counts[i][key[0]] * value)
            allele_counts[i][key[0]] += rate
            allele_counts[i][key[1]] -= rate
    return allele_counts
