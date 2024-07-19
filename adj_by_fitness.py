from normalize_genotype_freq import normalize_genotype_freq

def adj_by_fitness(genotype_freqs, genotype_fitness):
    # Adjust each frequency by it's fitness
    adj = {key: genotype_freqs[key] * genotype_fitness[key] for key in genotype_freqs}
    
    return normalize_genotype_freq(adj)
