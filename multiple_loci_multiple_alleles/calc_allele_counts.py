def calc_allele_counts(genotype_data):
    """
    Calculate allele counts for multiple loci with given the male/female genotype counts.

    """
    allele_counts = [{} for _ in range(len(next(iter(genotype_data.keys()))))]

    for genotype, data in genotype_data.items():
        for i, locus in enumerate(genotype):
            for allele in locus:
                if allele not in allele_counts[i]:
                    allele_counts[i][allele] = 0
                allele_counts[i][allele] += data['Nm'] + data['Nf']

    return allele_counts