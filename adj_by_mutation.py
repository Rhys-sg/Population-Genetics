def adj_by_mutation(allele_freq, mutations):
    """
    Adjust allele frequencies by mutating one allele into another, given a frequency.

    Parameters:
    allele_freq (list): A list of dictionaries representing allele frequencies.
    mutations (list): A list of dictionaries representing mutations.

    Returns:
    list: A list of dictionaries representing adjusted allele frequencies

    """
    for i, mutation in enumerate(mutations):
        for key, value in mutation.items():
            rate = allele_freq[i][key[0]] * value
            allele_freq[i][key[0]] += rate
            allele_freq[i][key[1]] -= rate
    return allele_freq
