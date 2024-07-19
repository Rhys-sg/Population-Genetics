import random
from normalize_genotype_freq import normalize_genotype_freq

def adj_by_drift(genotype_freqs, drift):
    # Adjust each frequency by drift
    adj = {key: genotype_freqs[key] * random.uniform(1-drift, 1) for key in genotype_freqs}
    
    return normalize_genotype_freq(adj)
