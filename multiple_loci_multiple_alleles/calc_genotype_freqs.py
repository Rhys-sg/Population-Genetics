from calc_N import calc_N

def calc_genotype_freqs(genotype_data):
    """
    Calculate genotype frequencies from genotype counts.
    """
    N = calc_N(genotype_data)

    return {genotype: (data['Nm'] + data['Nf']) / N for genotype, data in genotype_data.items()}
